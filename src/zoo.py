'''
Chapter 9 (Objects): Zoo
'''
#pylint: disable=too-few-public-methods

from dataclasses import dataclass


@dataclass
class Animal():
    '''
    Animal basic class
    '''
    species: str
    color: str
    number_of_legs: int

    def __repr__(self):
        return f'{self.color.capitalize()} {self.species}, {self.number_of_legs} legs'


class Sheep(Animal):
    '''
    Sheep
    '''
    def __init__(self, color):
        super().__init__(
            species='sheep',
            color=color,
            number_of_legs=4,
        )


class Wolf(Animal):
    '''
    Wolf
    '''
    def __init__(self, color):
        super().__init__(
            species='wolf',
            color=color,
            number_of_legs=4,
        )


class Snake(Animal):
    '''
    Snake
    '''
    def __init__(self, color):
        super().__init__(
            species='snake',
            color=color,
            number_of_legs=0,
        )


class Parrot(Animal):
    '''
    Parrot
    '''
    def __init__(self, color):
        super().__init__(
            species='parrot',
            color=color,
            number_of_legs=2,
        )


class Cage():
    '''
    Cage for animals
    '''
    def __init__(self, cage_id):
        self.cage_id = cage_id
        self.animals = []


    def __repr__(self):
        animals = ", ".join(f'({str(animal)})'
                            for animal in self.animals)
        return f'{self.cage_id}: {animals}'


    def add_animals(self, *animals):
        '''
        add animals to cage
        '''
        for animal in animals:
            self.animals.append(animal)


class Zoo():
    '''
    Zoo
    '''
    def __init__(self):
        self.cages = {}


    def __repr__(self):
        return '\n'.join(f'{str(cage)}'
                            for cage in self.cages.values())


    def add_cages(self, *cages):
        '''
        add cages to zoo
        '''
        for cage in cages:
            self.cages[cage.cage_id] = cage


    def animals_by_color(self, color):
        '''
        get all zoo animals of a specific color
        '''
        return [animal
                for cage in self.cages.values()
                    for animal in cage.animals
                    if animal.color == color]


    def animals_by_legs(self, legs):
        '''
        get all zoo animals with specific number of legs
        '''
        return [animal
                for cage in self.cages.values()
                    for animal in cage.animals
                    if animal.number_of_legs == legs]


    def number_of_legs(self):
        '''
        get total number of legs of all animals in zoo
        '''
        return sum(animal.number_of_legs
                    for cage in self.cages.values()
                        for animal in cage.animals)
