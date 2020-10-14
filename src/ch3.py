'''
Chapter 3
'''

import operator
from collections.abc import Iterable


def firstlast(seq):
    '''
    firstlast() returns the first and last elements of a sequence
    '''
    if not isinstance(seq, Iterable):
        return seq
    if len(seq) < 2:
        return seq
    if isinstance(seq, list):
        return [seq[0], seq[-1]]
    if isinstance(seq, tuple):
        return (seq[0], seq[-1])
    if isinstance(seq, str):
        return f'{seq[0]}{seq[-1]}'
    return seq


def mysum(*sequence):
    '''
    mysum() returns a sequence concatendated
    '''
    if len(sequence) == 0:
        return sequence
    total = sequence[0]
    for seq in sequence[1:]:
        total += seq
    return total


def alphabatize_names(people):
    '''
    alphabatize_names() sorts people by last then first name
    '''
    persons = []
    for person in people:
        persons.append([person['last'], person['first']])

    return sorted(persons, key=operator.itemgetter(0, 1))
