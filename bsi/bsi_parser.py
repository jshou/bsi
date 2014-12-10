import ply.yacc as yacc
from bsi_lexer import tokens
from bsi_pair import BsiPair

def p_pair_key_eq_value(p):
    'pair : KEY EQ val'
    p[0] = BsiPair(p[1], p[3])

def p_val_num(p):
    'val : NUM'
    p[0] = p[1]

def p_val_string(p):
    'val : STRING'
    p[0] = p[1]

bsi_parser = yacc.yacc()
