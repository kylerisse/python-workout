'''
Chapter 4
'''


def restaurant():
    '''
    simulates a restaurant
    '''
    menu = {
        'taco': 2,
        'burrito': 5,
        'quesadilla': 4,
        'soda': 1,
        'salsa': 1,
    }
    print('Welcome to Restaurant:')
    for food, cost in menu.items():
        print(f'{food} ${cost}')
    total = 0
    while item := input('what would you like? '):
        if item in menu:
            total += menu[item]
        else:
            print("we don't have that")
    print(f"That'll be ${total}")


def get_rainfall():
    '''
    rainfall processing
    '''
    rainfall = {}
    while city := input('city: '):
        while entered := input('rainfall: '):
            try:
                amount = int(entered)
            except ValueError:
                print(f'{entered} is not a valid integer')
                continue
            rainfall[city] = rainfall.get(city, 0) + amount
            break
    print('results:')
    for city_name, rainfall_amount in rainfall.items():
        print(f'{city_name}: {rainfall_amount}')


def dictdiff(dict1, dict2):
    '''
    compare two dictionaries
    '''
    results = {}
    allkeys = dict1.keys() | dict2.keys()
    for key in allkeys:
        d1val = dict1.get(key)
        d2val = dict2.get(key)
        if d1val != d2val:
            results[key] = [d1val, d2val]
    return results


def how_many_different_numbers(items):
    '''
    return count of unique items in a list
    '''
    return len(set(items))
