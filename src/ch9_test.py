#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 9 Tests
'''

import ch9


def test_create_scoops():
    '''
    test ch9.create_scoops()
    '''
    expected = '[Scoop(chocolate), Scoop(vanilla), Scoop(rocky road)]'
    got = ch9.create_scoops()
    assert str(got) == expected, f'{got} != {expected}'
    for i, flavor in enumerate(['chocolate', 'vanilla', 'rocky road']):
        assert got[i].flavor == flavor, f'{got[i].flavor} != {flavor}'


def test_Bowl_add_scoops_basic():
    '''
    test ch9.Bowl.add_scoops() basic usage
    '''
    expected = 'Scoop(vanilla),Scoop(chocolate),Scoop(avacado)'
    s1 = ch9.Scoop('vanilla')
    s2 = ch9.Scoop('chocolate')
    s3 = ch9.Scoop('avacado')
    b = ch9.Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3)
    got = b
    assert str(got) == expected, f'{got} != {expected}'
    for i, flavor in enumerate(['vanilla', 'chocolate', 'avacado']):
        assert got.scoops[i].flavor == flavor, f'{got.scoops[i].flavor} != {flavor}'


def test_Bowl_add_scoops_max():
    '''
    test ch9.Bowl.add_scoops() max limit
    '''
    expected = 'Scoop(rocky road),Scoop(cookies and cream),Scoop(vanilla)'
    s1 = ch9.Scoop('rocky road')
    s2 = ch9.Scoop('cookies and cream')
    s3 = ch9.Scoop('vanilla')
    s4 = ch9.Scoop('chocolate')
    s5 = ch9.Scoop('avacado')
    b = ch9.Bowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3, s4)
    b.add_scoops(s5)
    got = b
    assert str(got) == expected, f'{got} != {expected}'
    assert len(got.scoops) == 3, f'len should be 3'
    for i, flavor in enumerate(['rocky road', 'cookies and cream', 'vanilla']):
        assert got.scoops[i].flavor == flavor, f'{fot.scoops[i].flavor} != {flavor}'


def test_BigBowl_add_scoops_max():
    '''
    test ch9.Bowl.add_scoops() max limit
    '''
    expected = 'Scoop(cookies and cream),Scoop(rocky road),Scoop(cookie dough),Scoop(chocolate),Scoop(vanilla)'
    s1 = ch9.Scoop('cookies and cream')
    s2 = ch9.Scoop('rocky road')
    s3 = ch9.Scoop('cookie dough')
    s4 = ch9.Scoop('chocolate')
    s5 = ch9.Scoop('vanilla')
    s6 = ch9.Scoop('avacado')
    b = ch9.BigBowl()
    b.add_scoops(s1, s2)
    b.add_scoops(s3, s4)
    b.add_scoops(s5, s6)
    got = b
    assert str(got) == expected, f'{got} != {expected}'
    assert len(got.scoops) == 5, f'len should be 5'
    for i, flavor in enumerate([
        'cookies and cream',
        'rocky road',
        'cookie dough',
        'chocolate',
        'vanilla',
    ]):
        assert got.scoops[i].flavor == flavor, f'{got[i].scoops.flavor} != {flavor}'


def test_FlexibleDict():
    '''
    test ch9.FlexibleDict()
    '''

    # test string as key
    fda = ch9.FlexibleDict()
    fda['a'] = 300
    assert fda['a'] == 300, f"fda['a'] should be 300"

    # test int as key
    fdb = ch9.FlexibleDict()
    fdb[5] = 500
    assert fdb[5] == 500, f'fdb[5] should be 500'

    # test int as key with string as accessor
    fdc = ch9.FlexibleDict()
    fdc[1] = 100
    assert fdc['1'] == 100, f"fdc['1'] should be 100"

    # test string as key with int as accessor
    fdd = ch9.FlexibleDict()
    fdd['1'] = 200
    assert fdd[1] == 200, f'fdd[1] should be 200'

    # test non-existent key
    fde = ch9.FlexibleDict()
    assert fde['nothing'] == None, f"fde['nothing'] should be None"
