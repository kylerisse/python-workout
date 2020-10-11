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


def test_pl_sentence():
    '''
    test ch2.pl_sentence()
    '''
    test_cases = {
        'this is a test translation': 'histay isway away esttay ranslationtay',
        'hi there friend nice to see you': 'ihay heretay riendfay icenay otay eesay ouyay',
    }

    for k, v in test_cases.items():
        got = ch2.pl_sentence(k)
        assert got == v, f'{got} != {v}'


def test_ubbi_dubbi():
    '''
    test ch2.ubbi_dubbi()
    '''
    test_cases = {
        'milk': 'mubilk',
        'program': 'prubogrubam',
        'octopus': 'uboctubopubus',
        'elephant': 'ubelubephubant',
    }

    for k, v in test_cases.items():
        got = ch2.ubbi_dubbi(k)
        assert got == v, f'{got} != {v}'


def test_strsort():
    '''
    test ch2.strsort()
    '''
    test_cases = {
        'aieuo': 'aeiou',
        'cbad': 'abcd',
        'shorts': 'horsst',
    }

    for k, v in test_cases.items():
        got = ch2.strsort(k)
        assert got == v, f'{got} != {v}'
