'''
Chapter 7
'''

import ch2


def join_numbers(val):
    '''
    join numbers from 0 to val as comma seperated string
    '''
    return ','.join(str(x) for x in range(val))


def sum_numbers(word):
    '''
    sum all castable numbers in a space seperated string
    '''
    return sum(int(x) for x in word.split() if x.isdigit())


def flatten_recursive(items):
    '''
    flatten list(s), recursive with state
    '''
    ret = []
    for item in items:
        if isinstance(item, list):
            for sub_item in flatten_recursive(item):
                ret.append(sub_item)
        else:
            ret.append(item)
    return ret


def flatten_comprehension(items):
    '''
    flatten solution from the book
    '''
    return [element
            for sub_element in items
                for element in sub_element]


def pig_latin_file(path):
    '''
    convert contents of file to pig latin
    '''
    return ' '.join(ch2.pig_latin(word)
                for line in open(path, 'r')
                for word in line.split())


def flip_dict(dic):
    '''
    flip keys and values in dict
    '''
    return {val: key
                for key, val in dic.items()}


def transform_values(func, dic):
    '''
    transform values of dict using func
    '''
    return {key: func(val)
                for key, val in dic.items()}


def get_sv(path):
    '''
    return set containing all words from dictionary
    file that contain all 5 vowels (a, e, i , o, u)
    '''
    return {word.strip()
                for word in open(path, 'r')
                if 'a' in word.lower() and
                    'e' in word.lower() and
                    'i' in word.lower() and
                    'o' in word.lower() and
                    'u' in word.lower()}


def gematria():
    '''
    returns all lowercase letters and their corresponding
    "gematria" values
    '''
    return {chr(val): val - 96
                for val in range(97, 123)}


def gematria_for(word):
    '''
    returns gematria score for a word
    '''
    return sum(gematria()[letter]
                    for letter in word)
