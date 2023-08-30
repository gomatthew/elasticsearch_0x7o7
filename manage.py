"""
Entry
"""
import logging
import os
import traceback
import unittest
import rq_dashboard
import redis
import pymysql
from flask_cors import CORS
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from rq import Connection, Worker
from app.main import create_app, db
from app import blueprint
from app.main.exception_handlers.rq_handlers import rq_retry_handler
from app.main.service.es_service import rebuild_es_mapping


pymysql.install_as_MySQLdb()

app = create_app(os.getenv('RUNTIME_ENV') or 'dev')
app.register_blueprint(blueprint)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq")

app.app_context().push()

CORS(app, supports_credentials=True)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)

# from app.main.service.migration_service import es_migrate_data


@manager.command
def run_worker(queue_name):
    if queue_name not in app.config['QUEUES']:
        app.logger.error("queue not valid {}".format(queue_name))
        # return

    redis_url = app.config['RQ_REDIS_URL']
    redis_connection = redis.from_url(redis_url)
    try:
        with Connection(redis_connection):
            worker = Worker([queue_name], exception_handlers=[rq_retry_handler])
            worker.work(logging_level='INFO')
    except Exception as e:
        redis_connection.close()
        traceback.print_exc()
        app.logger.error(e)


@manager.command
def run():
    app.run(host="0.0.0.0", port=8000)


@manager.command
@manager.option('-i', '--index', dest='index_name', help='index name', default=None)
def build_es_mapping(index_name=None):
    rebuild_es_mapping(index_name)


@manager.command
@manager.option('-i', '--index', dest='index_name', help='index name', default=None)
@manager.option('-u', '--idx', dest='update_only', help='update only', default=False)
@manager.option('-s', '--start_time', dest='start_time', help='start time', default=None)
@manager.option('-e', '--end_time', dest='end_time', help='end time', default=None)
def es_migrate(index_name=None, update_only=False, start_time=None, end_time=None):
    es_migrate_data(index_name, start_time, end_time, update_only)


@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ != '__main__':
    # 如果不是直接运行，则将日志输出到 gunicorn 中
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

if __name__ == '__main__':
    manager.run()
