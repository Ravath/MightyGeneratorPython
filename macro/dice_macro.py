# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 13:52:47 2022

@author: Ehlion

PLY SITE   : https://www.dabeaz.com/ply/
    GITHUB : https://github.com/dabeaz/ply
    DOC    : https://github.com/dabeaz/ply/blob/master/doc/ply.md

Grammar

    S' -> expr
    expr -> expr PLUS expr
    expr -> expr MINUS expr
    expr -> MINUS expr
    expr -> expr TIMES expr
    expr -> expr DIV expr
    expr -> expr RAND_INTERVAL expr
    rand_expr -> expr RAND_DICE expr
    rand_expr -> rand_expr RAND_DECORATOR expr
    expr -> rand_expr
    expr -> rand_expr POOL_COUNT
    expr -> NUMBER
    expr -> LPAREN expr RPAREN
"""

from macro.ply import lex
import macro.ply.yacc as yacc
import macro.dice as dice
import macro.calc as calc

tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIV',
    'LPAREN',
    'RPAREN',
    'NUMBER',
    'RAND_INTERVAL',
    'RAND_DICE',
    'RAND_DECORATOR',
    'POOL_COUNT',
)

t_ignore = ' \t'

t_PLUS      = r'\+'
t_MINUS     = r'-'
t_TIMES     = r'\*'
t_DIV       = r'/'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_RAND_INTERVAL  = r':'
t_RAND_DICE      = r'd'
t_RAND_DECORATOR = r'h|l|>|<|([aArReE])(>|<)?'
t_POOL_COUNT     = r'c'

def t_NUMBER( t ) :
    r'[0-9]+'
    t.value = int( t.value )
    return t

def t_newline( t ):
    r'\n+'
    t.lexer.lineno += len( t.value )

def t_error( t ):
    print("Invalid Token:",t.value[0])
    t.lexer.skip( 1 )

lexer = lex.lex()

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIV' ),
    # ( 'left', 'RAND' ),
    ( 'nonassoc', 'UMINUS' )
)

def p_add( p ) :
    'expr : expr PLUS expr'
    p[0] = calc.AddOp(p[1], p[3])

def p_sub( p ) :
    'expr : expr MINUS expr'
    p[0] = calc.SubOp(p[1], p[3])

def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'
    p[0] = calc.NegOp(p[2])

def p_mult_div( p ) :
    '''expr : expr TIMES expr
            | expr DIV expr'''

    if p[2] == '*' :
        p[0] = calc.MulOp(p[1], p[3])
    else :
        if p[3] == 0 :
            print("Can't divide by 0")
            raise ZeroDivisionError('integer division by 0')
        p[0] = calc.DivOp(p[1], p[3])

def p_INTERVAL( p ) :
    '''expr : expr RAND_INTERVAL expr'''
    p[0] = dice.Interval(p[1], p[3])

def p_DICE( p ) :
    '''rand_expr : expr RAND_DICE expr'''

    # Check values are strictly positive
    for val in [ p[1], p[3] ] :
        if isinstance(val, int) :
            assert val > 0
        else :
            assert val.value > 0

    # convert operator symbol to implementation
    if p[2] == 'd' :
        p[0] = dice.Pool(p[1], p[3])
    else :
        raise NotImplementedError(f"Not implemented token {p[2]}")

def p_RAND_DECORATOR( p ) :
    '''rand_expr : rand_expr RAND_DECORATOR expr'''

    # convert operator symbol to implementation
    if p[2] == '>' :
        p[0] = dice.FilterDiceValue(p[1], p[3], True)
    elif p[2] == '<' :
        p[0] = dice.FilterDiceValue(p[1], p[3], False)
    elif p[2] == 'h' :
        p[0] = dice.FilterDiceCount(p[1], p[3], True)
    elif p[2] == 'l' :
        p[0] = dice.FilterDiceCount(p[1], p[3], False)
    else :
        operand = p[2][0].lower()
        is_higher = not (len(p[2])>2 and p[2][1] != '<')
        is_upper = operand.upper() == p[2][0]
        if operand == 'a' :
            p[0] = dice.CompoundExplode(p[1], p[3], is_higher, is_upper)
        elif operand == 'e' :
            p[0] = dice.Explode(p[1], p[3], is_higher, is_upper)
        elif operand == 'r' :
            p[0] = dice.ReRoll(p[1], p[3], is_higher, is_upper)
        else :
            raise NotImplementedError(f"Not implemented token {p[2]}")

def p_RAND_SUM( p ) :
    '''expr : rand_expr'''
    p[0] = dice.PoolSum(p[1])

def p_RAND_COUNT( p ) :
    '''expr : rand_expr POOL_COUNT'''
    p[0] = dice.PoolCount(p[1])

def p_expr2NUM( p ) :
    'expr : NUMBER'
    p[0] = p[1]
    # TODO p[0] = dice.Value(p[1]) ?

def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()

#___________________________________________________#
#                                                   #
#                    Convenience                    #
#___________________________________________________#

def get_ValueIf(toconvert) -> calc.ValueIf :
    if isinstance(toconvert, int) :
        return calc.Value(toconvert)
    elif isinstance(toconvert, calc.ValueIf):
        return toconvert
    elif isinstance(toconvert, str) :
        return parser.parse(toconvert)
    else :
        raise ValueError("Argument to convert must be int, str or ValueIf")

#___________________________________________________#
#                                                   #
#                       DEBUG                       #
#___________________________________________________#

if __name__ == '__main__':
    # DEBUG/TEST
    from utils.debug import test, print_log

    def test_roll(roll : str, expected_value:int = -1) :
        pool = parser.parse(roll)
        result = pool.value
        dice = pool.get_results()
        pstr = ""
        for d in dice :
            if d.discarded :
                pstr += '\\'
            pstr+=str(d.get_result())
            pstr+=" "
        print(f"{pool!s:8} : {pstr:15} => {result}")
        if expected_value != -1 :
            test(expected_value, result)

    res = parser.parse("-4*-(3-5)")
    test(-8, res.value)

    res = parser.parse("3:6")
    print(res.value)

    test_roll("2d6c", 2)
    test_roll("2d6")
    test_roll("5d6>3")
    test_roll("5d6<2c")
    test_roll("5d6h3")
    test_roll("5d6l2c", 2)
    test_roll("5d6a3")
    test_roll("5d6A3")
    test_roll("5d6A3c")
    test_roll("5d6e3")
    test_roll("5d6E3")
    test_roll("5d6r3")
    test_roll("5d6R3")
    