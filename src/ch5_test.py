#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 5 Tests
'''

import ch5


def test_get_final_line():
    '''
    test ch5.get_final_line()
    '''
    testcases = [
        {
            'file_name': 'testdata/passwd',
            'expected': 'sabayon:x:86:86:Sabayon user:/home/sabayon:/sbin/nologin',
        },
        {
            'file_name': 'testdata/manifesto.txt',
            'expected': "I am a hacker, and this is my manifesto. You may stop this individual, but you can't stop us all... after all, we're all alike.",
        },
        {
            'file_name': 'testdata/time_machine_chapter1.txt',
            'expected': "he winked at me solemnly."
        },
    ]
    for case in testcases:
        got = ch5.get_final_line(case['file_name'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_passwd_to_dict():
    '''
    test ch5.passwd_to_dict()
    '''
    testcases = [
        {
            'file_name': 'testdata/small_passwd',
            'expected': {'nobody': '-2', 'root': '0', 'daemon': '1'},
        },
    ]
    for case in testcases:
        got = ch5.passwd_to_dict(case['file_name'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_wordcount():
    '''
    test ch5.wordcount()
    '''
    testcases = [
        {
            'file_name': 'testdata/wcfile.txt',
            'expected': 'words: 28 unique: 20 chars: 165 lines: 11',
        },
    ]
    for case in testcases:
        got = ch5.wordcount(case['file_name'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_find_longest_word():
    '''
    test ch5.find_longest_word()
    '''
    testcases = [
        {
            'file_name': 'testdata/manifesto.txt',
            'expected': 'incompetencies',
        },
        {
            'file_name': 'testdata/passwd',
            'expected': 'console',
        },
        {
            'file_name': 'testdata/small_passwd',
            'expected': 'sample',
        },
        {
            'file_name': 'testdata/time_machine_chapter1.txt',
            'expected': 'representations',
        },
        {
            'file_name': 'testdata/wcfile.txt',
            'expected': 'different',
        },
    ]
    for case in testcases:
        got = ch5.find_longest_word(case['file_name'])
        assert got == case['expected'], f'{got} != {case["expected"]}'


def test_find_all_longest_words():
    '''
    test ch5.test_find_all_longest_words()
    '''
    testcases = [
        {
            'path': 'testdata/',
            'expected': {'time_machine_chapter1.txt': 'representations', 'manifesto.txt': 'incompetencies', 'passwd': 'console', 'wcfile.txt': 'different', 'small_passwd': 'sample'},
        },
    ]
    for case in testcases:
        got = ch5.find_all_longest_words(case['path'])
        assert got == case['expected'], f'{got} != {case["expected"]}'
