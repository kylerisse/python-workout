'''
Chapter 2: Strings
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


def ubbi_dubbi(word):
    '''
    ubbi_dubbi() translates a word into ubbi dubbi
    '''
    out = []
    for letter in word:
        if letter in vowels:
            out.append('ub')
        out.append(letter)
    return ''.join(out)


def strsort(word):
    '''
    strsort() sorts the characters in a string
    '''
    return ''.join(sorted(word))
