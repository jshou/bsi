import unittest
import bsi

class TestBsiObject(unittest.TestCase):
    def setUp(self):
        self.bsi_o = bsi.BsiObject()

    def test_bsi_object_can_add_and_get_key_value_pairs(self):
        self.bsi_o.add('key', 'value')
        self.assertEqual(self.bsi_o.get('key'), 'value')
