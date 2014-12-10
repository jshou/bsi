from .bsi_lexer import bsi_lexer
from .bsi_object import BsiObject
from .bsi_parser import bsi_parser
from .bsi_string import BsiString

parser = bsi_parser

def bsi_parse(data):
    return bsi_parser.parse(data)
