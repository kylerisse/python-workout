'''
Chapter 10: Iterators and generators
'''
# pylint: disable=too-few-public-methods

from os import listdir
from os.path import join


class MyEnumerateIterator():
    '''
    Iterator for MyEnumerate
    '''
    def __init__(self, data):
        self.data = data
        self.index = 0


    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        vals = (self.index, self.data[self.index])
        self.index += 1
        return vals


class MyEnumerate():
    '''
    MyEnumerate implements simple enumerator
    '''
    def __init__(self, data):
        self.data = data


    def __iter__(self):
        return MyEnumerateIterator(self.data)


class CircleIterator():
    '''
    Iterator for Circle
    '''
    def __init__(self, data, maxx):
        self.data = data
        self.maxx = maxx
        self.index = 0


    def __next__(self):
        if self.index >= self.maxx or len(self.data) < 1:
            raise StopIteration
        tmpi = 0
        if self.index != 0:
            tmpi = self.index % len(self.data)
        vals = (self.index, self.data[tmpi])
        self.index += 1
        return vals


class Circle():
    '''
    Circle iterator type object
    '''
    def __init__(self, data, maxx):
        self.data = data
        self.maxx = maxx


    def __iter__(self):
        return CircleIterator(self.data, self.maxx)


def dir_file_lines(path):
    '''
    dir_file_lines yields each line of every file in path
    '''
    for fil in listdir(path):
        try:
            for line in open(join(path, fil)):
                yield line
        except OSError:
            pass
