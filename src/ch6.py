'''
Chapter 6: Functions
'''

from datetime import datetime
from operator import add, mul, sub, truediv
from random import choice, seed


def myxml(tag, content='', **kwargs):
    '''
    myxml generates an xml tag
    '''
    attributes = ''.join([f' {key}="{val}"'
                        for key, val in kwargs.items()])
    return f'<{tag}{attributes}>{content}</{tag}>'


def calc(equation):
    '''
    prefix calculator
    '''
    elems = equation.split()
    if not len(elems) == 3:
        return False
    oper = elems[0]
    arg1 = int(elems[1])
    arg2 = int(elems[2])
    answer = 0
    if oper == '+':
        answer = add(arg1, arg2)
    if oper == '-':
        answer = sub(arg1, arg2)
    if oper == '*':
        answer = mul(arg1, arg2)
    if oper == '/':
        if arg2 == 0:
            return False
        answer = truediv(arg1, arg2)
    if oper == '**':
        answer = pow(arg1, arg2)
    return answer


def create_password_generator(validchars, rngseed=datetime.now()):
    '''
    returns a password generator confined to valid characters
    '''
    def generator(length):
        seed(rngseed)
        valid = list(validchars)
        passw = ''
        for _ in range(0, length):
            passw += choice(valid)
        return passw
    return generator
