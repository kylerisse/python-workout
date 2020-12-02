'''
Menu
'''


def menu(**kwargs):
    '''
    Implements a menu of callables
    '''
    keys = '/'.join(sorted(kwargs))
    while command := input(f'enter command {keys}: '):
        if command in kwargs:
            return kwargs.get(command)()
        print('try again')
