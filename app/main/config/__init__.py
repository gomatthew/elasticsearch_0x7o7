"""
Application Configs Settings
"""

from .dev_config import DevelopmentConfig
from .unit_test_config import TestingConfig

def get_config_by_name(config_name, environment=None):
    """
    get config by environment config name
    """
    match config_name:
        case 'dev':
            return DevelopmentConfig(environment=environment)
        case 'testing':
            return TestingConfig(environment=environment)
        # case 'production':
        #     return ProductionConfig(environment=environment)
        # case 'unittest':
        #     return UnitTestConfig(environment=environment)
        case _:
            raise Exception('Wrong environment params. check your params again.')
