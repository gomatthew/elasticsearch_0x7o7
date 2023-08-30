"""
Entry of the Flask
"""
import os

from flask import Flask
from flask_redis import FlaskRedis
from flask_rq2 import RQ
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
from app.main.config import get_config_by_name
from app.main.util.redis_lock import Redlock
from app.main.util.flask_elasticsearch import FlaskElasticsearch


db = SQLAlchemy()
redis_store = FlaskRedis(decode_responses=True)
redis_lock = Redlock(redis_store)
rq = RQ()
scheduler = APScheduler()
es = FlaskElasticsearch()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

app = Flask(__name__, template_folder=BASE_DIR + '/templates', static_folder=BASE_DIR + '/static')

# from app.main.model.person_info_model import PersonInfo
from app.main.model.task_model import TaskRecord
from app.main.model.tag_dict_model import TagDict

def create_app(config_name, tenant=None):
    """
    Flask App
    """
    app.config.from_object(get_config_by_name(config_name, tenant))
    app.logger.setLevel(app.config['LOG_LEVEL'])
    redis_store.init_app(app)
    rq.init_app(app)
    db.init_app(app)
    db.app = app
    es.init_app(app)
    return app
