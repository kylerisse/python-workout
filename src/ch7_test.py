#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 7 Tests
'''

import ch7


def test_join_numbers():
    '''
    test ch7.join_numbers()
    '''
    testcases = [
        {
            'input': 15,
            'expected': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14',
        },
        {
            'input': 0,
            'expected': '',
        },
    ]

    for case in testcases:
        got = ch7.join_numbers(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_sum_numbers():
    '''
    test ch7.sum_numbers()
    '''
    testcases = [
        {
            'input': '10 abc 20 de44 30 55fg 40',
            'expected': 100,
        },
        {
            'input': 'abc aef 24d 27u4 b8d',
            'expected': 0,
        },
        {
            'input': '100 50 20 70 8O 44',
            'expected': 284,
        },
    ]

    for case in testcases:
        got = ch7.sum_numbers(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_flatten():
    '''
    test ch7.flatten()
    '''
    testcases = [
        {
            'input': [[1, 2], [3, 4]],
            'expected': [1, 2, 3, 4],
        },
        {
            'input': [1, [2, 3, 4], [1, [2, [3, 4, [5, 6]]]]],
            'expected': [1, 2, 3, 4, 1, 2, 3, 4, 5, 6],
        },
        {
            'input': ['test', [True, False], 'b', 6, 2, 1],
            'expected': ['test', True, False, 'b', 6, 2, 1],
        },
    ]
    
    for case in testcases:
        got = ch7.flatten(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'
