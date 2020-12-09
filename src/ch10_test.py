#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 10 Tests
'''

import hashlib

import ch10

def test_MyEnumerate_class():
    '''
    test ch10.MyEnumerate class
    '''
    test_cases = [
        {
            'input': 'abc',
            'expected': '0: a, 1: b, 2: c',
        },
        {
            'input': range(4),
            'expected': '0: 0, 1: 1, 2: 2, 3: 3',
        },
        {
            'input': '',
            'expected': '',
        }
    ]
    for case in test_cases:
        got = ', '.join(f'{key}: {val}'
                            for key, val in ch10.MyEnumerate(case['input']))
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_Circle_class():
    '''
    test ch10.Circle class
    '''
    test_cases = [
        {
            'input_data': 'abc',
            'input_maxx': 5,
            'expected': '0: a, 1: b, 2: c, 3: a, 4: b',
        },
        {
            'input_data': range(2),
            'input_maxx': 4,
            'expected': '0: 0, 1: 1, 2: 0, 3: 1',
        },
        {
            'input_data': 'A',
            'input_maxx': 7,
            'expected': '0: A, 1: A, 2: A, 3: A, 4: A, 5: A, 6: A',
        },
        {
            'input_data': '',
            'input_maxx': 400,
            'expected': '',
        },
    ]
    for case in test_cases:
        got = ', '.join(f'{key}: {val}'
                            for key, val in ch10.Circle(case['input_data'], case['input_maxx']))
        assert got == case['expected'], f'{got} != {case["expected"]}'


#def test_dir_file_lines():
#    '''
#    test ch10.dir_file_lines()
#    '''
#    expected = '7d81639a316d592170a292bf189d25164118dba96938f797982dd6c353ca2a0f'
#    gotstr = ''.join(line
#                        for line in ch10.dir_file_lines('testdata/'))
#    gotbyt = bytes(gotstr, 'utf-8')
#    got = hashlib.sha256(gotbyt).hexdigest()
#    assert got == expected
