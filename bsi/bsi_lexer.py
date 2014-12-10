import ply.lex as lex
from bsi_string import BsiString

tokens = (
    'KEY',
    'STRING',
    'NUM',
    'EQ',
    'L_SQ_BR',
    'R_SQ_BR',
    'L_BRACE',
    'R_BRACE'
)

t_KEY = r'[a-zA-Z0-9_]+'

def t_STRING(t):
    r'".*"'
    t.value = BsiString(t.value.strip('"'))
    return t

def t_NUM(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

t_EQ = r'='

t_L_SQ_BR = r'\['
t_R_SQ_BR = r'\]'
t_L_BRACE = r'{'
t_R_BRACE = r'}'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t,'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

bsi_lexer = lex.lex()
