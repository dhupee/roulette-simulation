import random
import time
from player import decide
import matplotlib

from numba import jit

# player states
martingale = False # for Martingale simulation
anti_martingale = False
money = 50000 # amount of money player have
bet = 100 # the money player will bet
round = 50 # how many round bet will happen
tendency = 'all' # for bet choice 'behaviour'

@jit(nopython = True)
def roll_wheel():
    '''Get random int from 0 to 36

    Returns:
        int: The number it will generate
    '''

    roll = random.randint(0, 36)
    
    return roll

win = 0
lost = 0
for i in range(50):
    roll = roll_wheel()
    bet_type, decision = decide()
    print(decision,',', bet_type)
    if bet_type == 'single':
        if roll == decision:
            print('win')
            win += 1
        else:
            print('lost')
            lost += 1
    else:
        if roll in decision:
            print('win')
            win += 1
        else:
            print('lost')
            lost += 1
print('win', win)
print('lost', lost)
    # time.sleep(1) # delay 2 seconds