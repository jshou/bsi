import unittest
import bsi

class TestBsiParser(unittest.TestCase):
    def setUp(self):
        self.parser = bsi.bsi_parser

    def test_bsi_parser_parses_simple_objects(self):
        data = '''
        ip = "127.0.0.1"
        port = 1234
        '''

        obj = self.parser.parse(data)

        self.assertEqual(obj.get('ip'), bsi.BsiString('127.0.0.1'))
        self.assertEqual(obj.get('port'), 1234)

    def test_bsi_parser_parses_arrays(self):
        data = '''
        ports = [123 234 345]
        ids = [1 2 3]
        '''

        obj = self.parser.parse(data)

        self.assertEqual(obj.get('ports'), bsi.BsiArray([123, 234, 345]))
        self.assertEqual(obj.get('ids'), bsi.BsiArray([1, 2, 3]))

