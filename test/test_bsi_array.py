import unittest
from bsi import BsiArray
import bsi

class TestBsiArray(unittest.TestCase):
    def test_bsi_array_equality(self):
        self.assertEqual(
            BsiArray([bsi.BsiNumber(1), bsi.BsiNumber(2), bsi.BsiNumber(3)]),
            BsiArray([bsi.BsiNumber(1), bsi.BsiNumber(2), bsi.BsiNumber(3)])
        )

        self.assertNotEqual(
            BsiArray([bsi.BsiNumber(1), bsi.BsiNumber(2), bsi.BsiNumber(3)]),
            BsiArray([bsi.BsiNumber(1), bsi.BsiNumber(2), bsi.BsiNumber(4)])
        )

    def test_bsi_to_string(self):
        ba = BsiArray([bsi.BsiNumber(1), bsi.BsiNumber(2), bsi.BsiNumber(3)])

        self.assertEqual(str(ba), '[ 1 2 3 ]')
