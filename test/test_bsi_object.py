import unittest
import bsi

class TestBsiObject(unittest.TestCase):
    def setUp(self):
        self.bsi_o = bsi.BsiObject()

    def test_bsi_object_can_add_and_get_key_value_pairs(self):
        self.bsi_o.add('key', 'value')
        self.assertEqual(self.bsi_o.get('key'), 'value')

    def test_bsi_object_to_string(self):
        self.bsi_o.add('k1', 'v1')
        self.bsi_o.add('k2', 'v2')

        str_obj = 'k1 = v1\nk2 = v2'

        self.assertEqual(str(self.bsi_o), str_obj)
