#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 2 Tests
'''

import ch2


def test_pig_latin():
    '''
    test ch2.pig_latin()
    '''
    test_cases = {
        'air': 'airway',
        'eat': 'eatway',
        'python': 'ythonpay',
        'computer': 'omputercay',
    }

    for k, v in test_cases.items():
        got = ch2.pig_latin(k)
        assert got == v, f'{got} != {v}'
