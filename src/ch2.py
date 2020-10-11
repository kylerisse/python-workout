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


def pl_sentence(words):
    '''
    pl_sentence() translates a sentence into pig latin
    '''
    out = []
    for word in words.split(' '):
        out.append(pig_latin(word))
    return ' '.join(out)
