import unittest
import bsi

class TestBsiObject(unittest.TestCase):
    def setUp(self):
        self.bsi_o = bsi.BsiObject()

    def test_bsi_object_can_set_and_get_key_value_pairs(self):
        self.bsi_o.set('key', 'value')
        self.assertEqual(self.bsi_o.get('key'), 'value')

    def test_bsi_object_to_string_primitive_values(self):
        self.bsi_o.set('k1', 1)
        self.bsi_o.set('k2', bsi.BsiString('v2'))

        str_obj = 'k1 = 1\nk2 = "v2"'

        self.assertEqual(str(self.bsi_o), str_obj)

    def test_bsi_object_to_string_arrays(self):
        self.bsi_o.set('k1', bsi.BsiArray([1, 2, 3]))

        str_obj = 'k1 = [1 2 3]'

        self.assertEqual(str(self.bsi_o), str_obj)

    def test_bsi_object_to_string_nested_objects(self):
        zombie1 = bsi.BsiObject()
        zombie1.set('name', bsi.BsiString("Dead Bob"))

        nested = bsi.BsiObject()
        nested.set('zombie1', zombie1)
        nested.set('zombie2', bsi.BsiString('double dead'))

        self.bsi_o.set('k1', 2)
        self.bsi_o.set('zombies', nested)

        str_obj = '''k1 = 2
zombies = {
\tzombie1 = {
\t\tname = "Dead Bob"
\t}
\tzombie2 = "double dead"
}'''

        self.assertEqual(str(self.bsi_o), str_obj)
