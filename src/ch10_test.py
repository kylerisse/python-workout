#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 10 Tests
'''

import hashlib
import time

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


def test_dir_file_lines():
    '''
    test ch10.dir_file_lines()
    '''
    expected = 'f2af1680c9b0a527a5448f873da33ff980db686680dd10ff4e0beac672738db3'
    gotstr = ''.join(line
                        for line in sorted(ch10.dir_file_lines('testdata/')))
    gotbyt = bytes(gotstr, 'utf-8')
    got = hashlib.sha256(gotbyt).hexdigest()
    assert got == expected


def test_elapsed_since():
    '''
    test ch10.elapsed_since()
    '''
    test_cases = [
        {
            'input': 'abcd',
            'expected': ['a', 'b', 'c', 'd'],
            'sleep': 0.0001,
        },
        {
            'input': [1, 2, 3, 4, 5],
            'expected': [1, 2, 3, 4, 5],
            'sleep': 0.04,
        },
        {
            'input': 'yz',
            'expected': ['y', 'z'],
            'sleep': 1,
        },
    ]
    for case in test_cases:
        for i, tup in enumerate(ch10.elapsed_since(case['input'])):
            time.sleep(case['sleep'])
            if i == 0:
                assert tup[0] == 0, f'{tup[0]} should be 0'
            else:
                assert tup[0] > case['sleep'], f'{tup[0]} should be greater than {case["sleep"]}'
            assert tup[1] == case['expected'][i], f'{tup[1]} should be {case["expected"]}'


def test_mychain():
    '''
    test ch10.mychain()
    '''
    test_cases = [
        {
            'func': ch10.mychain('abc', [1, 2, 3], {'a': 1, 'b': 2}),
            'expected': ['a', 'b', 'c', 1, 2, 3, 'a', 'b'],
        },
        {
            'func': ch10.mychain(('b', None), [8, 4], 'test', (1, 2, 3), {'test': 1, 'test_again': 2}),
            'expected': ['b', None, 8, 4, 't', 'e', 's', 't', 1, 2, 3, 'test', 'test_again'],
        },
        {
            'func': ch10.mychain(range(0, 3)),
            'expected': [0, 1, 2],
        },
    ]
    for case in test_cases:
        got = []
        for i in case['func']:
            got.append(i),
        assert got == case['expected'], f'{got} != {case["expected"]}'
