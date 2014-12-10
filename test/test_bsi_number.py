import unittest
from bsi import BsiNumber

class TestBsiNumber(unittest.TestCase):
    def test_bsi_number_equality(self):
        self.assertEqual(BsiNumber(3), BsiNumber(3))

    def test_bsi_number_to_string(self):
        self.assertEqual(str(BsiNumber(3)), '3')
        self.assertEqual(str(BsiNumber(3.2)), '3.2')
