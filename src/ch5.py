'''
Chapter 5
'''

import re
from os import listdir
from os.path import isfile, join


def get_final_line(file_name):
    '''
    returns the final line of a file
    '''
    final_line = ''
    with open(file_name, 'r') as fil:
        for line in fil:
            final_line = line
    return final_line


def passwd_to_dict(file_name):
    '''
    turn password file into dictionary
    '''
    users = {}
    with open(file_name, 'r') as fil:
        for line in fil:
            if line.startswith('#'):
                continue
            elems = line.split(':')
            user = elems[0]
            uid = elems[2]
            users[user] = uid
    return users


def wordcount(file_name):
    '''
    mimics the basic wc command
    '''
    all_words = {}
    chars = lines = 0
    with open(file_name, 'r') as fil:
        for line in fil:
            lines += 1
            chars += len(line)
            words = line.split()
            for word in words:
                all_words[word] = all_words.get(word, 0) + 1
    words = sum(all_words.values())
    uniq = len(all_words.keys())
    return f'words: {words} unique: {uniq} chars: {chars} lines: {lines}'


def find_longest_word(file_name):
    '''
    find the longest word in a file, if multiple return the first found
    '''
    longest = ''
    with open(file_name, 'r')as fil:
        for line in fil:
            words = line.split()
            clean_words = [clean for clean in words if re.match(r'[^\W\d]*$', clean)]
            for word in clean_words:
                if len(word) > len(longest):
                    longest = word
    return longest


def find_all_longest_words(path):
    '''
    find the longest word in each file in a directory
    '''
    files = {}
    dir_files = [fil for fil in listdir(path) if isfile(join(path, fil))]
    for fil in dir_files:
        files[fil] = find_longest_word(f'{path}/{fil}')
    return files
