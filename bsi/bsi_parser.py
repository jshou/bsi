import ply.yacc as yacc
from bsi_lexer import tokens
from bsi_object import BsiObject

def p_object_pairs(p):
    'obj : pairs'
    p[0] = BsiObject()
    for pair in p[1]:
        p[0].set(pair[0], pair[1])

def p_pairs_pair(p):
    'pairs : pair'
    p[0] = [p[1]]

def p_pairs_pair_pairs(p):
    'pairs : pair pairs'
    p[0] = [p[1]] + p[2]

def p_pair_key_eq_value(p):
    'pair : KEY EQ val'
    p[0] = (p[1], p[3])

def p_val_num(p):
    'val : NUM'
    p[0] = p[1]

def p_val_string(p):
    'val : STRING'
    p[0] = p[1]

def p_error(p):
    print "Syntax error in input!"

bsi_parser = yacc.yacc()
