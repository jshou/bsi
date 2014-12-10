import unittest
import bsi

class TestBsiObject(unittest.TestCase):
    def setUp(self):
        self.bsi_o = bsi.BsiObject()

    def test_bsi_object_can_set_and_get_key_value_pairs(self):
        self.bsi_o.set('key', 'value')
        self.assertEqual(self.bsi_o.get('key'), 'value')

    def test_bsi_object_to_string(self):
        self.bsi_o.set('k1', 1)
        self.bsi_o.set('k2', bsi.BsiString('v2'))

        str_obj = 'k1 = 1\nk2 = "v2"'

        self.assertEqual(str(self.bsi_o), str_obj)
