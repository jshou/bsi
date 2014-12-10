import unittest
from bsi import BsiArray

class TestBsiArray(unittest.TestCase):
    def test_bsi_array_equality(self):
        self.assertEqual(
            BsiArray([1, 2, 3]),
            BsiArray([1, 2, 3])
        )

        self.assertNotEqual(
            BsiArray([1, 2, 3]),
            BsiArray([1, 2, 4])
        )

    def test_bsi_to_string(self):
        ba = BsiArray([1, 2, 3])

        self.assertEqual(str(ba), '[1 2 3]')
