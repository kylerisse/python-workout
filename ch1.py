'''
Chapter 1
'''

import datetime
import random

def guessing_game(randseed=datetime.datetime.now()):
    '''
    guessing_game() starts an interactive guessing game
    '''
    random.seed(randseed)
    number = random.randint(10, 30)
    while sguess := input(f'guess a number between 10 and 30: '):
        try:
            guess = int(sguess)
        except ValueError:
            print(f'{sguess} is not a valid integer')
            continue
        if guess == number:
            break
        if guess > number:
            print(f'{guess} is too high')
        if guess < number:
            print(f'{guess} is too low')
    print(f'{guess} is {number}, correct')


def mysum(*numbers):
    '''
    mysum() returns the sum of any number of input numbers
    '''
    total = 0
    for num in numbers:
        total += num
    return total


def run_timing():
    '''
    run_timing() starts an interactive loop to collect
    run times and return the average
    '''
    count = 0
    total = 0.0
    while time := input(f'Enter 10 km run time: '):
        total += float(time)
        count += 1
    return total/count


def hex_output(hex_num):
    '''
    hex_output() takes a hexidecimal number and returns
    it's decimal equivalent
    '''
    dec = 0
    for power, num in enumerate(reversed(str(hex_num))):
        dec += int(num, 16) * (16 ** power)
    return dec
