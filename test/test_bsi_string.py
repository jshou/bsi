import unittest
from bsi import BsiString

class TestBsiString(unittest.TestCase):
    def setUp(self):
        self.bsi_string = BsiString('undead')

    def test_to_string(self):
        self.assertEqual(str(self.bsi_string), '"undead"')
