#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 3 Tests
'''

import ch3


def test_firstlast():
    '''
    test ch3.firstlast()
    '''
    test_cases = [
        {
            'input': [1, 2, 3, 4],
            'output': [1, 4],
        },
        {
            'input': (1, 2, 3, 4),
            'output': (1, 4),
        },
        {
            'input': 'abcd',
            'output': 'ad', 
        },
        {
            'input': [],
            'output': [],
        },
        {
            'input': ['h'],
            'output': ['h'],
        },
        {
            'input': ['b', 2, True],
            'output': ['b', True],
        },
        {
            'input': 6,
            'output': 6,
        }
    ]

    for case in test_cases:
        got = ch3.firstlast(case['input'])
        assert got == case['output'], f'{got} != {case["output"]}'


def test_mysum():
    '''
    tests ch3.mysum()
    '''
    test_cases = {
        'input': ['abc', 'def'],
        'output': 'abcdef',
    },
    {
        'input': [[1, 2, 3],[4, 5, 6]],
        'output': [1, 2, 3, 4, 5, 6],
    },
    {
        'input': [1, 2, 3],
        'output': 6,
    },
    {
        'input': '',
        'output': ''
    },
    {
        'input': 1,
        'output': 1,
    }

    for case in test_cases:
        got = ch3.mysum(*case['input'])
        assert got == case['output'], f'{got} != {case["output"]}'


def test_alphabatize_names():
    '''
    tests ch3.alphabatize_names()
    '''
    test_cases = [
        {
            'input': [
                {
                    'first': 'Tom',
                    'last': 'Shmo',
                    'email': 'tomshmo@fake.com',
                },
                {
                    'first': 'Toe',
                    'last': 'Shmo',
                    'email': 'toeshmo@fake.com',
                },
                {
                    'first': 'Harry',
                    'last': 'Algo',
                    'email': 'harry@algofamily.com',
                }
            ],
            'expected': [
                ['Algo', 'Harry'],
                ['Shmo', 'Toe'],
                ['Shmo', 'Tom'],
            ],
        },
    ]

    for case in test_cases:
        got = ch3.alphabatize_names(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'