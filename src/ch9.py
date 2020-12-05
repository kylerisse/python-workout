'''
Chapter 9: Objects
'''


class Scoop():
    # pylint: disable=too-few-public-methods
    '''
    Ice Cream Scoop
    '''
    def __init__(self, flavor):
        self.flavor = flavor


    def __repr__(self):
        return f'Scoop({self.flavor})'


def create_scoops():
    '''
    creates 3 scoops of ice cream
    '''
    return [Scoop(flavor)
            for flavor in ('chocolate', 'vanilla', 'rocky road')]


class Bowl():
    '''
    Ice Cream Bowl
    '''
    max = 3

    def __init__(self):
        self.scoops = []


    def __repr__(self):
        return ','.join(str(scoop)
                        for scoop in self.scoops)


    def add_scoops(self, *scoops):
        '''
        Add scoops to bowl
        '''
        for scoop in scoops:
            if len(self.scoops) < self.max:
                self.scoops.append(scoop)


class BigBowl(Bowl):
    # pylint: disable=too-few-public-methods
    '''
    Bigger Ice Cream Bowl
    '''
    max = 5


class FlexibleDict(dict):
    '''
    Flexible dict with keys that seemlessly transition
    between int and string
    '''
    def __getitem__(self, key):
        if key in self:
            return dict.__getitem__(self, key)
        if str(key) in self:
            return dict.__getitem__(self, str(key))
        if key.isdigit() and int(key) in self:
            return dict.__getitem__(self, int(key))
        return None
