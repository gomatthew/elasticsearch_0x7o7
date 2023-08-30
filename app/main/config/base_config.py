"""
Base Config
"""


class Config(object):
    """
    Configs that include all the configurable settings
    """

    def __init__(self, environment=None):
        self.environment = environment

    # DB Settings
    SQLALCHEMY_DATABASE_URI = 'mysql://root:xxxx@127.0.0.1:3306/xxxx'
    SQLALCHEMY_BINDS = {
        'xxx': 'xxx',
        'xxxx': 'xxx'
    }
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 200,
        'pool_recycle': 120,
        'pool_pre_ping': True
    }
    SQLALCHEMY_ECHO = False  # echo SQL info

    # Redis Settings
    REDIS_URL = "redis://xx:xx/xx"
    RQ_REDIS_URL = REDIS_URL
    REDIS_DEFAULT_TTL = 86400

    # Logging
    DEBUG = True
    LOG_LEVEL = 'INFO'

    # RQ Settings, must start from 0
    QUEUES = [f'es_worker_queue_{i}' for i in range(10)]
    RQ_MAX_RETRIES = 5
    RQ_QUEUE_PREFIX = "es_worker_queue_"

    # Elastic Search
    ELASTICSEARCH_HOST = "xx.xx.xx.xxx:xx"
    ELASTICSEARCH_HTTP_AUTH = None
    ES_INDEX_PREFIX = 'xxx_'
    ES_DEFAULT_SHARDS = 3
    ES_DEFAULT_REPLICAS = 1
    ES_INDEX = ['person_info']

    MAX_QUERY_RESULTS = 5000
    MAX_RESULT_WINDOW = 1000000
