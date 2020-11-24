#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 4 Tests
'''

import ch4


def test_restaurant():
    '''
    (this needs a test)
    '''
    pass


def test_get_rainfall():
    '''
    (this needs a test)
    '''
    pass


def test_dictdiff():
    '''
    test ch4.dictdiff()
    '''
    testcases = [
        {
            'd1': {'a': 1, 'b': 2, 'c': 3},
            'd2': {'a': 1, 'b': 2, 'c': 3},
            'expected': {},
        },
        {
            'd1': {'a': 1, 'b': 2, 'c': 3},
            'd2': {'a': 1, 'b': 2, 'c': 4},
            'expected': {'c': [3, 4]},
        },
        {
            'd1': {'a': 1, 'b': 2, 'd': 3},
            'd2': {'a': 1, 'b': 2, 'c': 4},
            'expected': {'c': [None, 4], 'd': [3, None]},
        },
        {
            'd1': {'a':1, 'b':2, 'c':3},
            'd2': {'a':1, 'b':2, 'd':4},
            'expected': {'c': [3, None], 'd': [None, 4]},
        },
    ]
    for case in testcases:
        got = ch4.dictdiff(case['d1'], case['d2'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_how_many_different_numbers():
    '''
    test ch4.how_many_different_numbers()
    '''
    testcases = [
        {
            'input': [1, 3, 4, 2, 3, 1, 4, 2, 3, 4, 2, 1, 2],
            'expected': 4,
        },
        {
            'input': [],
            'expected': 0,
        },
        {
            'input': [22, 17, 44, 63, 82, 11, 22, 97, 41],
            'expected': 8,
        },
        {
            'input': range(-1000, 1000),
            'expected': 2000,
        },
    ]
    for case in testcases:
        got = ch4.how_many_different_numbers(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'
