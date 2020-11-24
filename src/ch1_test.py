#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 1 Tests
'''

import ch1


def test_guessing_game():
    '''
    tests ch1.guessing_game()
    '''
    test_cases = [
        {
            'seed': 1,
            'user_input': [15, 7, 11, 13, 14],
            'expected': [
                'guess a number between 10 and 30: ',
                '15 is too high',
                'guess a number between 10 and 30: ',
                '7 is too low',
                'guess a number between 10 and 30: ',
                '11 is too low',
                'guess a number between 10 and 30: ',
                '13 is too low',
                'guess a number between 10 and 30: ',
                '14 is 14, correct',
            ],
        },
        # should exits silently if given no input
        {
            'seed': 2,
            'user_input': [''],
            'expected': [
                'guess a number between 10 and 30: ',
            ]
        },
        # should return invalid integer warning 
        {
            'seed': 2,
            'user_input': [15, 'x', 7, 11],
            'expected': [
                'guess a number between 10 and 30: ',
                '15 is too high',
                'guess a number between 10 and 30: ',
                'x is not a valid integer',
                'guess a number between 10 and 30: ',
                '7 is too low',
                'guess a number between 10 and 30: ',
                '11 is 11, correct',
            ]
        },
    ]

    for case in test_cases:
        output = []

        def mock_input(s):
            output.append(s)
            return case['user_input'].pop(0)


        ch1.input = mock_input
        ch1.print = lambda s: output.append(s)

        ch1.guessing_game(case['seed'])
        assert output == case['expected']


def test_mysum():
    '''
    test ch1.mysum()
    '''
    test_cases = [
        {
            'input': [1, 2, 3],
            'output': 6,
        },
        {
            'input': [200, 300, 400, 500],
            'output': 1400,
        },
        {
            'input': [],
            'output': 0,
        },
        {
            'input': ['test'],
            'output': 0,
        },
        {
            'input': [True, 'test', 4, 5],
            'output': 9,
        },
        {
            'input': [True, 'test', 17.2, 11.4, False],
            'output': 28.6,
        },
        {
            'input': [True, '11.4', 17.2, 11.4, False],
            'output': 40.0,
        },
    ]
    for case in test_cases:
        got = ch1.mysum(*case['input'])
        assert got == case['output'], f'{got} != {case["output"]}'


def test_run_timing():
    '''
    test ch1.run_timing()
    '''
    test_cases = [
        {
            'user_input': [5, 2.2, 11, 6, ''],
            'expected': [
                'Enter 10 km run time: ',
                'Enter 10 km run time: ',
                'Enter 10 km run time: ',
                'Enter 10 km run time: ',
                'Enter 10 km run time: ',
                '6.05',
            ],
        },
        {
            'user_input': [''],
            'expected': [
                'Enter 10 km run time: ',
                0,
            ],
        },
    ]
    for case in test_cases:
        output = []

        def mock_input(s):
            output.append(s)
            return case['user_input'].pop(0)

        ch1.input = mock_input
        ch1.print = lambda s: output.append(s)
        
        got = ch1.run_timing()
        assert output == case['expected']


def test_hex_output():
    '''
    test ch1.hex_output()
    '''
    test_cases = [
        {
            'input': '50',
            'expected': 80,
        }
    ]
    for case in test_cases:
        got = ch1.hex_output(case['input'])
        assert got == case['expected'], f'{got} != {case["output"]}'
