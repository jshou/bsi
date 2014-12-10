import unittest
import bsi

class TestBsiParser(unittest.TestCase):
    def setUp(self):
        self.parser = bsi.bsi_parser

    def test_bsi_parser_parses_simple_objects(self):
        data = '''
        ip = "127.0.0.1"
        '''

        bsi_pair = self.parser.parse(data)

        self.assertEqual(bsi_pair.k, 'ip')
