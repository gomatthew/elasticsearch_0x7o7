from flask_restx import Namespace

from app.main.dto import get_parser, return_value_dto


class Dummy(object):

    api = Namespace('Dummy', description='for test only')
    parser = get_parser(api)
    return_value = return_value_dto(api)
