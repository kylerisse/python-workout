#!/usr/bin/env python3
'''
Chapter 1 Tests
'''

import unittest.mock
import ch1

def test_guessing_game():
    '''
    tests ch1.guessing_game()
    '''
    test_cases = [{
        "seed": 1,
        "user_input": [15, 7, 11, 13, 14],
        "expected": [
            "guess a number between 10 and 30: ",
            "15 is too high",
            "guess a number between 10 and 30: ",
            "7 is too low",
            "guess a number between 10 and 30: ",
            '11 is too low',
            "guess a number between 10 and 30: ",
            '13 is too low',
            "guess a number between 10 and 30: ",
            '14 is 14, correct',
        ],
    },
    {
        "seed": 2,
        "user_input": [15, "x", 7, 11],
        "expected": [
            "guess a number between 10 and 30: ",
            "15 is too high",
            "guess a number between 10 and 30: ",
            "x is not a valid integer",
            "guess a number between 10 and 30: ",
            "7 is too low",
            "guess a number between 10 and 30: ",
            "11 is 11, correct",
        ]
    }]

    for tc in test_cases:
        output = []

        def mock_input(s):
            output.append(s)
            return tc["user_input"].pop(0)


        ch1.input = mock_input
        ch1.print = lambda s: output.append(s) 

        ch1.guessing_game(tc["seed"])
        assert output == tc["expected"]
