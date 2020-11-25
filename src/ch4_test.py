#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 4 Tests
'''

import ch4


def test_restaurant():
    '''
    test ch4.restaurant()
    '''
    testcases = [
        {
            'user_input': [
                '',
            ],
            'expected': [
                'Welcome to Restaurant:',
                'taco $2',
                'burrito $5',
                'quesadilla $4',
                'soda $1',
                'salsa $1',
                'what would you like? ',
                "That'll be $0",                
            ],
        },
        {
            'user_input': [
                'taco',
                '',
            ],
            'expected': [
                'Welcome to Restaurant:',
                'taco $2',
                'burrito $5',
                'quesadilla $4',
                'soda $1',
                'salsa $1',
                'what would you like? ',
                'what would you like? ',
                "That'll be $2",                
            ],
        },
        {
            'user_input': [
                'taco',
                'burrito',
                'quesadilla',
                'tamale',
                'salsa',
                'soda',
                'taco',
                '',
            ],
            'expected': [
                'Welcome to Restaurant:',
                'taco $2',
                'burrito $5',
                'quesadilla $4',
                'soda $1',
                'salsa $1',
                'what would you like? ',
                'what would you like? ',
                'what would you like? ',
                'what would you like? ',
                "we don't have that",
                'what would you like? ',
                'what would you like? ',
                'what would you like? ',
                'what would you like? ',
                "That'll be $15",                
            ],
        },
    ]

    for case in testcases:
        output = []

        def mock_input(s):
            output.append(s)
            return case['user_input'].pop(0)
        
        ch4.input = mock_input
        ch4.print = lambda s: output.append(s)

        ch4.restaurant()
        assert output == case['expected'], f'{output} != {case["expected"]}'


def test_get_rainfall():
    '''
    test ch4.rainfall()
    '''
    testcases = [
        {
            'user_input': [
                'dallas',
                '10',
                'dallas',
                '2',
                'houston',
                'x',
                '5',
                '',
            ],
            'expected': [
                'city: ',
                'rainfall: ',
                'city: ',
                'rainfall: ',
                'city: ',
                'rainfall: ',
                'x is not a valid integer',
                'rainfall: ',
                'city: ',
                'results:',
                'dallas: 12',
                'houston: 5',
            ]
        },
    ]

    for case in testcases:
        output = []

        def mock_input(s):
            output.append(s)
            return case['user_input'].pop(0)
        
        ch4.input = mock_input
        ch4.print = lambda s: output.append(s)

        ch4.get_rainfall()
        assert output == case['expected'], f'{output} != {case["expected"]}'


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
