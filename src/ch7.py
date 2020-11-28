'''
Chapter 7
'''


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


def flatten(items):
    '''
    flatten list(s), recursive with state
    '''
    ret = []
    for item in items:
        if isinstance(item, list):
            for sub_item in flatten(item):
                ret.append(sub_item)
        else:
            ret.append(item)
    return ret
