'''
Chapter 2
'''

vowels = ['a', 'e', 'i', 'o', 'u']


def pig_latin(word):
    '''
    pig_latin() translates a string into pig latin
    '''
    if word[0] in vowels:
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'
