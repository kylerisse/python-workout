'''
Freedonia
'''

PROVINCES = {
    'Chico': 50,
    'Groucho': 70,
    'Harpo': 50,
    'Zeppo': 40,
}


def calculate_tax(price, province, hour):
    '''
    Calculates the tax rate in Freedonia
    '''
    if province not in PROVINCES:
        return False
    if hour not in range(0, 24):
        return False
    return price + (price * (PROVINCES[province]/100) * hour/24)
