#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 7 Tests
'''

import ch7
import hashlib


def test_join_numbers():
    '''
    test ch7.join_numbers()
    '''
    testcases = [
        {
            'input': 15,
            'expected': '0,1,2,3,4,5,6,7,8,9,10,11,12,13,14',
        },
        {
            'input': 0,
            'expected': '',
        },
    ]

    for case in testcases:
        got = ch7.join_numbers(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_sum_numbers():
    '''
    test ch7.sum_numbers()
    '''
    testcases = [
        {
            'input': '10 abc 20 de44 30 55fg 40',
            'expected': 100,
        },
        {
            'input': 'abc aef 24d 27u4 b8d',
            'expected': 0,
        },
        {
            'input': '100 50 20 70 8O 44',
            'expected': 284,
        },
    ]

    for case in testcases:
        got = ch7.sum_numbers(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_flatten_recursive():
    '''
    test ch7.flatten_recursive()
    '''
    testcases = [
        {
            'input': [[1, 2], [3, 4]],
            'expected': [1, 2, 3, 4],
        },
        {
            'input': [1, [2, 3, 4], [1, [2, [3, 4, [5, 6]]]]],
            'expected': [1, 2, 3, 4, 1, 2, 3, 4, 5, 6],
        },
        {
            'input': ['test', [True, False], 'b', 6, 2, 1],
            'expected': ['test', True, False, 'b', 6, 2, 1],
        },
    ]
    
    for case in testcases:
        got = ch7.flatten_recursive(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_flatten_comprehension():
    '''
    test ch7.flatten_comprehension()
    '''
    testcases = [
        {
            'input': [[1, 2], [3, 4]],
            'expected': [1, 2, 3, 4],
        },
    ]
    for case in testcases:
        got = ch7.flatten_comprehension(case['input'])
        assert got == case['expected'], f'{got} !+ {case["expected"]}'


def test_pig_latin_file():
    '''
    test ch7.pig_latin_file()
    '''
    testcases = [
        {
            'input': 'testdata/time_machine_chapter1.txt',
            'checksum': '581f9205bee054da0b1f9e9ddfce6720679a8932900c19637ef6a64f21bb9a69',
        },
        {
            'input': 'testdata/manifesto.txt',
            'checksum': 'eaea19b875fc2cf523404759e8300615ed574ab9a5d05e65bc4a9508f40dd653',
        }
    ]

    for case in testcases:
        gotstr = ch7.pig_latin_file(case['input'])
        gotbyt = bytes(gotstr, 'utf-8')
        got = hashlib.sha256(gotbyt).hexdigest()
        assert got == case['checksum'], f'pig_latin_file({case["input"]}) is unexpected checksum {got}'


def test_flip_dict():
    '''
    test ch7.flip_dict()
    '''
    testcases = [
        {
            'input': {'a': 1, 'b': 2, 'c': 3, 'd': 4,},
            'expected': {1: 'a', 2: 'b', 3: 'c', 4: 'd',},
        }
    ]

    for case in testcases:
        got = ch7.flip_dict(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_transform_values():
    '''
    test ch7.transform_values()
    '''
    testcases = [
        {
            'input': {'a': 1, 'b': 2, 'c': 3, 'd': 4,},
            'func': lambda x: x*x,
            'expected': {'a': 1, 'b': 4, 'c': 9, 'd': 16,},
        },
        {
            'input': {'a': 1, 'b': 2, 'c': 3, 'd': 4,},
            'func': lambda x: x+x,
            'expected': {'a': 2, 'b': 4, 'c': 6, 'd': 8,},
        },
        {
            'input': {'a': 2, 'b': 3, 'c': 4, 'd': 5,},
            'func': lambda x: f'{x} bottles of beer',
            'expected': {
                'a': '2 bottles of beer',
                'b': '3 bottles of beer',
                'c': '4 bottles of beer',
                'd': '5 bottles of beer',
            },
        },
    ]

    for case in testcases:
        got = ch7.transform_values(case['func'], case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_get_sv():
    '''
    test ch7.get_sv()
    '''
    testcases = [
        {
            'file_name': 'testdata/dict/words.txt',
            'expected_count': 6004,
        },
        {
            'file_name': 'testdata/dict/words_small.txt',
            'expected_count': 2,
        },
    ]
    for case in testcases:
        got = ch7.get_sv(case['file_name'])
        assert len(got) == case['expected_count'], f'{got} != {case["expected_count"]}'


def test_gematria():
    '''
    test ch7.gematria()
    '''
    expected = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4,
        'e': 5, 'f': 6, 'g': 7, 'h': 8,
        'i': 9, 'j': 10, 'k': 11, 'l': 12,
        'm': 13, 'n': 14, 'o': 15, 'p': 16,
        'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24,
        'y': 25, 'z': 26,
    }
    got = ch7.gematria()
    assert got == expected, f'{got} !+ {expected}'


def test_gematria_for():
    '''
    test ch7.gematria_for()
    '''
    testcases = [
        {
            'input': 'a',
            'expected': 1,
        },
        {
            'input': 'abc',
            'expected': 6,
        },
        {
            'input': '',
            'expected': 0,
        },
        {
            'input': 'python',
            'expected': 98,
        },
    ]
    
    for case in testcases:
        got = ch7.gematria_for(case['input'])
        assert got == case['expected'], f'{got} != {case["expected"]}'
