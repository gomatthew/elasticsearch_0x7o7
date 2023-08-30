from flask_testing import TestCase
from app.main.service.es_service import rebuild_es_mapping
from app.main import create_app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        return create_app("unittest")

    def setUp(self):
        pass

    def tearDown(self):
        pass
