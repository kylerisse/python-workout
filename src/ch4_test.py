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


def get_rainfall():
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
