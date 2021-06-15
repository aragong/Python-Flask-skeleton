import unittest

from python_module import python_module


class TestPythonModule(unittest.TestCase):
    def test_python_module(self):
        self.response = python_module.hello_world()
        self.assertEqual(type(self.response), dict)
