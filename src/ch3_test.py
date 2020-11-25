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
        },
        {
            'input': {'a': 1, 'b': 2},
            'output': {'a': 1, 'b': 2},
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
        'output': '',
    },
    {
        'input': 1,
        'output': 2,
    },

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


def test_most_repeating_word():
    test_cases = [
        {
            'input': ['this', 'is', 'an', 'elementary', 'test', 'example'],
            'output': 'elementary'
        },
        {
            'input': [],
            'output': '',
        }
    ]

    for case in test_cases:
        got = ch3.most_repeating_word(case['input'])
        assert got == case['output'], f'{got} != {case["output"]}'


def test_format_sort_records():
    '''
    test ch3.format_sort_records()
    '''
    testcases = [
        {
            'input': [
                ('Joe', 'Shmoe', 7.85),
                ('Bo', 'Shmoe', 3.626),
                ('George', 'Martini', 10),
                ('Dexter', 'Boomhauer', 2.1),
                ('Albert', 'X', 17),
            ],
            'expected': [
                'Boomhauer Dexter    2.10',
                'Martini   George    10.00',
                'Shmoe     Bo        3.63',
                'Shmoe     Joe       7.85',
                'X         Albert    17.00',
            ],
        },
    ]

    for case in testcases:
        output = []

        ch3.print = lambda s: output.append(s)

        ch3.format_sort_records(case['input'])
        assert output == case['expected'], f'{output} != {case["expected"]}'
