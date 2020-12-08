#!/usr/bin/env python3
# pylint: disable=all
'''
Chapter 9 Zoo Tests
'''

import zoo


def test_Animals_basic():
    '''
    Test basic functionality of Animal classes
    '''
    test_cases = [
        {
            'animal': zoo.Sheep('blue'),
            'str': 'Blue sheep, 4 legs',
            'species': 'sheep',
            'color': 'blue',
            'legs': 4,
        },
        {
            'animal': zoo.Wolf('orange'),
            'str': 'Orange wolf, 4 legs',
            'species': 'wolf',
            'color': 'orange',
            'legs': 4,
        },
        {
            'animal': zoo.Snake('purple'),
            'str': 'Purple snake, 0 legs',
            'species': 'snake',
            'color': 'purple',
            'legs': 0,
        },
        {
            'animal': zoo.Parrot('green'),
            'str': 'Green parrot, 2 legs',
            'species': 'parrot',
            'color': 'green',
            'legs': 2,
        },
    ]
    for case in test_cases:
        got = case['animal']
        str_got = str(got)
        assert str_got == case['str'], f'got {str_got} but expected {case["str"]}'
        species_got = got.species 
        assert species_got == case['species'], f'got {species_got} but expected {case["species"]}'
        color_got = got.color 
        assert color_got == case['color'], f'got {color_got} but expected {case["color"]}'
        legs_got = got.number_of_legs 
        assert legs_got == case['legs'], f'got {legs_got} but expected {case["legs"]}'


def test_Cage_basic():
    '''
    Test basic functionality of Cage class
    '''
    test_cases = [
        {
            'animals': [
                zoo.Sheep('white'),
                zoo.Wolf('blue'),
                zoo.Snake('orange'),
                zoo.Parrot('black'),
            ],
            'id': 42,
            'length': 4,
            'str': f'42: (White sheep, 4 legs), (Blue wolf, 4 legs), (Orange snake, 0 legs), (Black parrot, 2 legs)'
        }
    ]
    for case in test_cases:
        got = zoo.Cage(case['id'])
        got.add_animals(*case['animals'])
        len_got = len(got.animals)
        assert len_got == case['length'], f'incorrect length, {len_got} != {case["length"]}'
        str_got = str(got)
        assert str_got == case['str'], f'invalid string format, {str_got} != {case["str"]}'


def test_Zoo_basic():
    '''
    Test all functionality of Zoo class
    '''
    a1 = zoo.Snake('red')
    a2 = zoo.Snake('blue')
    a3 = zoo.Sheep('orange')
    a4 = zoo.Wolf('purple')
    a5 = zoo.Parrot('blue')
    a6 = zoo.Sheep('purple')
    a7 = zoo.Snake('red')
    a8 = zoo.Parrot('black')
    a9 = zoo.Wolf('blue')
    a10 = zoo.Sheep('green')
    
    c1 = zoo.Cage(1)
    c1.add_animals(a1, a2)
    c2 = zoo.Cage(12)
    c2.add_animals(a3)
    c3 = zoo.Cage(77)
    c3.add_animals(a4, a5, a6, a7)
    c4 = zoo.Cage(400)
    c4.add_animals(a8, a9)
    c5 = zoo.Cage(6)
    c5.add_animals(a10)

    z1 = zoo.Zoo()
    z1.add_cages(c1)
    z1.add_cages(c2, c3, c4)
    z1.add_cages(c5)

    # animals_by_color
    assert len(z1.animals_by_color('red')) == 2, 'expected 2 red animals in zoo'
    assert len(z1.animals_by_color('turquoise')) == 0, 'expected 0 turquoise animals in zoo'
    assert len(z1.animals_by_color('blue')) == 3, 'expected 3 blue animals in zoo'

    # animals_by_legs
    assert len(z1.animals_by_legs(0)) == 3, 'expected 3 animals with 0 legs'
    assert len(z1.animals_by_legs(2)) == 2, 'expected 2 animals with 2 legs'
    assert len(z1.animals_by_legs(3)) == 0, 'expected 0 animals with 3 legs'
    assert len(z1.animals_by_legs(4)) == 5, 'expected 5 animals with 4 legs'

    # number_of_legs
    assert z1.number_of_legs() == 24, 'expected 20 legs in the zoo'

    # __repr__
    z2 = zoo.Zoo()
    z2.add_cages(c2, c4)
    expected_str = '12: (Orange sheep, 4 legs)\n400: (Black parrot, 2 legs), (Blue wolf, 4 legs)'
    assert str(z2) == expected_str, 'unexpected string format'
