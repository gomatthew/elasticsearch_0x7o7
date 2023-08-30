"""
Test Cases for Util

"""
import unittest

from app.main.util.Util import camel_to_snake
from app.test.base import BaseTestCase


class TestUtil(BaseTestCase):
    """
    Utils
    """

    def test_camel_to_snake(self):
        camel_str = "testCamel"
        self.assertEqual("test_camel", camel_to_snake(camel_str))

        camel_str = "testCamelCamelcamel"
        self.assertEqual("test_camel_camelcamel", camel_to_snake(camel_str))


if __name__ == '__main__':
    unittest.main()
