"""
Development Configurations
"""

from urllib.parse import quote_plus
from .base_config import Config


class TestingConfig(Config):
    """
    Development Configurations
    """

    # REDIS_URL = "redis://:d39e267e-0cbb-11ed-9bac-fa20bd4fa130@192.168.3.109:16379/7"
    REDIS_URL = "redis://127.0.0.1:6379/7"
    RQ_REDIS_URL = REDIS_URL
    REDIS_PREFIX = 'unit_test:'

    # MISSION Settings
    PROCESS_WORKERS = 16
    TASKS = 50000  # 该配置乘2000 即为数据量

    # Mysql Settings
    SQLALCHEMY_DATABASE_URI = f'mysql://root:makemoney@127.0.0.1:3306/unittest'
    SQLALCHEMY_ECHO = False  # echo SQL info
    SQLALCHEMY_BINDS = {
    }

    # Elastic Search
    ELASTICSEARCH_HOST = ['http://127.0.0.1:19200']
    # ELASTICSEARCH_HTTP_AUTH = 'elastic','7t2h4BdVZboWbc7wDnQl'
    # elasticsearch-password 7t2h4BdVZboWbc7wDnQl
    ES_INDEX_PREFIX = 'unit_test_'
    ES_INDEX_SHARDS = 3
    ES_INDEX_REPLICAS = 1
    # sqlacodegen --outfile=models2.py mysql+pymysql://root:makemoney@127.0.0.1:3306/temp_duyun

