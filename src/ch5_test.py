#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 5 Tests
'''

import hashlib
import os

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


def test_passwd_to_tsv():
    '''
    test ch5.passwd_to_tsv
    '''
    testcases = [
        {
            'in': 'testdata/small_passwd',
            'out': '/tmp/small_passwd.tsv',
            'checksum': '2973af190793a89c5f80b373ba82c4155b1c90fed74e1bf6d4b083c7f6447410',
        },
        {
            'in': 'testdata/passwd',
            'out': '/tmp/passwd.tsv',
            'checksum': '48c26a6adc2e6e8306c79bba47b258565f7b6594507608f8fe6db24ceef75db4',
        },
    ]
    for case in testcases:
        ch5.passwd_to_tsv(case['in'], case['out'])
        with open(case['out'], 'rb') as ofile:
            byts = ofile.read()
            osum = hashlib.sha256(byts).hexdigest()
            os.remove(case['out'])
        assert case['checksum'] == osum, f'{case["out"]} has unexpected checksum {osum}'


def test_summarize_scores():
    '''
    test ch5.summarize_scores
    '''
    testcases = [
        {
            'input': 'testdata/scores',
            'expected': [
                '9b.json',
                '\tmath: min 21, max 93, avg 63.00',
                '\tliterature: min 68, max 100, avg 84.50',
                '\tscience: min 72, max 99, avg 87.67',
                '9a.json',
                '\tmath: min 65, max 100, avg 85.00',
                '\tliterature: min 78, max 98, avg 83.60',
                '\tscience: min 75, max 97, avg 86.40',
            ],
        },
    ]
    for case in testcases:
        output = []

        ch5.print = lambda s: output.append(s)

        ch5.summarize_scores(case['input'])
        assert output == case['expected'], f'{output} != {case["expected"]}'
