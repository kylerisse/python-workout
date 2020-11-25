#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 6 Tests
'''

import ch6


def test_myxml():
    '''
    test ch6.myxml()
    '''
    testcases = [
        {
            'func': ch6.myxml('foo'),
            'expected': '<foo></foo>',
        },
        {
            'func': ch6.myxml('foo', 'bar'),
            'expected': '<foo>bar</foo>',
        },
        {
            'func': ch6.myxml('foo', 'bar', a=1, b=2, c=3),
            'expected': '<foo a="1" b="2" c="3">bar</foo>'
        },
    ]
    for case in testcases:
        got = case['func']
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_calc():
    '''
    test ch6.calc()
    '''
    testcases = [
        {
            'func': ch6.calc('+ 5 5'),
            'expected': 10,
        },
        {
            'func': ch6.calc('- 5 5'),
            'expected': 0,
        },
        {
            'func': ch6.calc('* 5 5'),
            'expected': 25,
        },
        {
            'func': ch6.calc('/ 5 5'),
            'expected': 1,
        },
        {
            'func': ch6.calc('/ 5 0'),
            'expected': False,
        },
        {
            'func': ch6.calc('^ 2 2'),
            'expected': False,
        },
        {
            'func': ch6.calc('** 5 3'),
            'expected': 125,
        },
        {
            'func': ch6.calc('+ 5'),
            'expected': False,
        },
    ]    
    for case in testcases:
        got = case['func']
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_create_password_generator():
    '''
    test ch6.create_password_generator
    '''
    testcases = [
        {
            'generator': ch6.create_password_generator('abcdefghijklmnopqrstuvwxyz0123456789', rngseed=1),
            'tests': [
                {
                    'length': 5,
                    'expected': 'ieqh5',
                },
                {
                    'length': 10,
                    'expected': 'ieqh524yng',
                },
            ],
        },
        {
            'generator': ch6.create_password_generator('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()', rngseed=1),
            'tests': [
                {
                    'length': 8,
                    'expected': 'i!eqh524',
                },
                {
                    'length': 16,
                    'expected': 'i!eqh524^yng5by1',
                },
            ],
        },
    ]
    for case in testcases:
        gen = case['generator']
        for test in case['tests']:
            got = gen(test['length'])
            assert got == test['expected'], f'{got} != {test["expected"]}'
