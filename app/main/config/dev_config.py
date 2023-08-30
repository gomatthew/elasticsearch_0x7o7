"""
Development Configurations
"""

from .base_config import Config


class DevelopmentConfig(Config):
    """
    Development Configurations
    """

    # REDIS_URL = "redis://:d39e267e-0cbb-11ed-9bac-fa20bd4fa130@192.168.3.109:16379/7"
    REDIS_URL = "redis://127.0.0.1:6379/7"
    RQ_REDIS_URL = REDIS_URL
    BALANCE_KEY = '0x7o7ES'
    REDIS_PREFIX = 'dev:queue_'
    REDIS_QUEUE = [REDIS_PREFIX + str(i) for i in range(10)]
    # MISSION Settings
    PROCESS_WORKERS = 6
    TASKS = 5000  # 该配置乘2000 即为数据量

    # Mysql Settings
    SQLALCHEMY_DATABASE_URI = 'mysql://root:makemoney@127.0.0.1:3306/test'
    SQLALCHEMY_ECHO = False  # echo SQL info
    SQLALCHEMY_BINDS = {
    }

    # Elastic Search
    ELASTICSEARCH_HOST = ['http://127.0.0.1:19200']
    # ELASTICSEARCH_HTTP_AUTH = 'elastic','7t2h4BdVZboWbc7wDnQl'
    # elasticsearch-password 7t2h4BdVZboWbc7wDnQl
    ES_INDEX_PREFIX = 'dev_'
    ES_INDEX_SHARDS = 3
    ES_INDEX_REPLICAS = 1
    # sqlacodegen --outfile=models2.py mysql+pymysql://root:makemoney@127.0.0.1:3306/temp_duyun
