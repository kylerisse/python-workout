#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 8 Tests
'''

import freedonia


def test_calculate_tax():
    '''
    test freedonia.calculate_tax
    '''
    test_cases = [
        {
            'price': 500,
            'province': 'Harpo',
            'hour': 12,
            'expected': 625.0,
        },
        {
            'price': 500,
            'province': 'Harpo',
            'hour': 21,
            'expected': 718.75,
        },
        {
            'price': 1700,
            'province': 'Zeppo',
            'hour': 24,
            'expected': False,
        },
        {
            'price': 1700,
            'province': 'Chico',
            'hour': 0,
            'expected': 1700,
        },
        {
            'price': 1700,
            'province': 'Fako',
            'hour': 0,
            'expected': False,
        },
    ]

    for case in test_cases:
        got = freedonia.calculate_tax(case['price'], case['province'], case['hour'])
        assert got == case['expected'], f'{got} != {case["expected"]}'
