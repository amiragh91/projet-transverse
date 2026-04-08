import unittest

class TestExemple(unittest.TestCase):
    def test_exemple(self):
        self.assertTrue(True)

    def test_addition(self):
        self.assertEqual(2 + 2, 4)