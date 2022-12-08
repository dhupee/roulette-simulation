import random
from numba import jit

# I use https://en.wikipedia.org/wiki/Roulette as my main guidance

@jit(nopython = True)
def single():
    '''Generate random number from 0-36

    Returns:
        int: randomly generated number from 0-36
    '''

    bet_type = 'single'

    decision = random.randint(0, 36)

    return bet_type, decision

@jit(forceobj = True)
def split():

    bet_type = 'split'

    number = random.randint(1, 35)
    
    if (number % 3 == 1 or number % 3 == 2) and number < 33:
        choice = [number + 1, number + 3]
        pair = random.choice(choice)
        decision = [number, pair]
    elif number % 3 == 0 and number <= 33:
        decision = [number, number + 3]
    elif number == 34:
        decision = [number, number + 1]
    elif number == 35:
        decision = [number, number + 1]
    return bet_type, decision

@jit(forceobj = True)
def street():

    bet_type = 'street'

    number = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    choice = random.choice(number) # pick randomly from first column except 34

    decision = list(range(choice, choice + 3)) # get number for street bet

    return bet_type, decision

@jit(forceobj = True)
def corner():

    bet_type = 'corner'

    number = [1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32]
    choice = random.choice(number)

    decision = [choice, choice + 1, choice + 3, choice + 4]

    return bet_type, decision

@jit(forceobj = True)
def basket():

    bet_type = 'basket'

    basket_array = [0, 1, 2, 3]
    decision = basket_array

    return bet_type, decision

@jit(forceobj = True)
def double_street():

    bet_type = 'double_street'

    number = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31]
    choice = random.choice(number) # pick randomly from first column except 34

    decision = list(range(choice, choice + 6)) # get number for double street bet

    return bet_type, decision

@jit(forceobj = True)
def column():

    bet_type = 'column'

    result = random.randint(1, 3)

    first_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    second_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    third_column = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    if result == 1:
        decision = first_column
    elif result == 2:
        decision = second_column
    else:
        decision = third_column

    return bet_type, decision

@jit(forceobj = True)
def dozen():

    bet_type = 'dozen'

    result = random.randint(1, 3)

    if result == 1:
        decision = list(range(1, 13))
    elif result == 2:
        decision = list(range(13, 25))
    else:
        decision = list(range(25, 37))
    
    return bet_type, decision

@jit(forceobj = True)
def odd_or_even():

    bet_type = 'odd_or_even'

    number = list(range(1,37))
    odd = number[1::2]
    even = number[::2]

    choice = ['odd', 'even']
    result = random.choice(choice)

    if result == 'even':
        decision = even
    else:
        decision = odd
    
    return bet_type, decision

@jit(forceobj = True)
def red_or_black():

    bet_type = 'red_or_black'

    number = random.randint(1, 100)
    result = number % 2

    red = [32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16, 1, 14, 9, 18, 7, 12, 3]
    black = [15, 4, 2, 17, 6, 13, 11, 8, 10, 24, 33, 20, 31, 22, 29, 28, 35, 26]

    if result == 0:
        decision = red
    else:
        decision = black
    
    return bet_type, decision

@jit(forceobj = True)
def half():

    bet_type = 'half'

    number = random.randint(1, 100)
    result = number % 2

    if result == 0:
        decision = list(range(1, 19))
    else:
        decision = list(range(19, 37))
    
    return bet_type, decision

@jit(forceobj = True)
def decide():
    '''Generate random bet decision for the player

    Returns:
        string : type of bet it picked
        int | list[int] : number(s) it picked
    '''

    # get the bet types randomly
    number = random.randint(0, 10)
    match number:
        case 0: # single
            bet_type, decision = single()
        case 1: # split
            bet_type, decision = split()
        case 2: # street
            bet_type, decision = street()
        case 3: # corner
            bet_type, decision = corner()
        case 4: # basket
            bet_type, decision = basket()
        case 5: # double_street
            bet_type, decision = double_street()
        case 6: # column
            bet_type, decision = column()
        case 7: # dozen
            bet_type, decision = dozen()
        case 8: # odd_or_even
            bet_type, decision = odd_or_even()
        case 9: # red_or_black
            bet_type, decision = red_or_black()
        case 10: # half
            bet_type, decision = half()
        case _: # else
            bet_type, decision = "something's wrong", 'check it'
    return bet_type, decision