#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 8 Tests
'''

import menu


def test_menu():
    '''
    test menu.menu()
    '''

    def func_a():
        return 'A'

    def func_b():
        return 'B'

    def func_c():
        return 'C'

    test_cases = [
        {
            'func': lambda: menu.menu(a=func_a, b=func_b),
            'user_input': ['c', 'a'],
            'expected_output': [
                'enter command a/b: ',
                'try again',
                'enter command a/b: ',
            ],
            'expected_return': 'A'
        },
        {
            'func': lambda: menu.menu(a=func_a, c=func_c, b=func_b),
            'user_input': ['b'],
            'expected_output': [
                'enter command a/b/c: ',
            ],
            'expected_return': 'B'
        },
        {
            'func': lambda: menu.menu(d=func_c, a=func_c, b=func_b),
            'user_input': ['c', 'c', 'd'],
            'expected_output': [
                'enter command a/b/d: ',
                'try again',
                'enter command a/b/d: ',
                'try again',
                'enter command a/b/d: ',
            ],
            'expected_return': 'C'
        },
    ]

    for case in test_cases:
        output = []

        def mock_input(s):
            output.append(s)
            return case['user_input'].pop(0)
        
        menu.input = mock_input
        menu.print = lambda s: output.append(s)

        got = case['func']()
        assert got == case['expected_return'], f'{got} != {case["expected_return"]}'
        assert output == case['expected_output'], f'{output} != {case["expected_output"]}'
