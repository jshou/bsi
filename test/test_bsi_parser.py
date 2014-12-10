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
        self.assertEqual(obj.get('port'), bsi.BsiNumber(1234))

    def test_bsi_parser_parses_arrays(self):
        data = '''
        ports = [123 234 345]
        ids = [
          1
          2
          3
        ]
        '''

        obj = self.parser.parse(data)

        self.assertEqual(obj.get('ports'), bsi.BsiArray([bsi.BsiNumber(123), bsi.BsiNumber(234), bsi.BsiNumber(345)]))
        self.assertEqual(obj.get('ids'), bsi.BsiArray([bsi.BsiNumber(1), bsi.BsiNumber(2), bsi.BsiNumber(3)]))

    def test_bsi_parser_parses_nested_objects(self):
        data = '''
        player_ids = {
            Bob = 1
            Carly = 2
        }
        zombie_ids = {
            DeadBob = 3
            DeadCarly = 4
        }
        '''

        obj = self.parser.parse(data)

        self.assertEqual(obj.get('player_ids').get('Bob'), bsi.BsiNumber(1))
        self.assertEqual(obj.get('zombie_ids').get('DeadBob'), bsi.BsiNumber(3))
