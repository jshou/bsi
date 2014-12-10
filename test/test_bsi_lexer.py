import unittest
import bsi

class TestBsiLexer(unittest.TestCase):
    def setUp(self):
        self.lex = bsi.bsi_lexer
        self.data = '''
        ip = "127.0.0.1"
        float = 1337.3
        number = -3
        '''
        self.tokens = [
            ('KEY', 'ip'),
            ('EQ', '='),
            ('STRING', bsi.BsiString('127.0.0.1')),
            ('KEY', 'float'),
            ('EQ', '='),
            ('NUM', bsi.BsiNumber(1337.3)),
            ('KEY', 'number'),
            ('EQ', '='),
            ('NUM', bsi.BsiNumber(-3))
        ]

    def test_tokenizer_tokenizes_correctly(self):
        self.lex.input(self.data)

        token_data = [(t.type, t.value) for t in self.lex]

        self.assertEqual(token_data, self.tokens)
