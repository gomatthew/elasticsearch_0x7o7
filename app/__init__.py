from flask import Blueprint
from flask_restx import Api

from app.main.config.api_config import api_config

from app.main.controller.v1.test_controller import api as test


# 创建蓝图
blueprint = Blueprint('api', __name__)
api = Api(blueprint, **api_config)

# api.add_namespace(person_info, path='/v1/person_info')
api.add_namespace(test, path='/test')
