import unittest

from python_module import python_module


class TestPythonModule(unittest.TestCase):
    """Example test"""

    def test_python_module(self):
        self.response = python_module.hello_world()
        self.assertIsNotNone(self.response)
        self.assertEqual(type(self.response), dict)
