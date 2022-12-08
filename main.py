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
def get_result():
    '''Get random int from 0 to 36

    Returns:
        int: The number it will generate
    '''

    result = random.randint(0, 36)
    
    return result

while True:
    # result = get_result()
    bet_type, decision = decide()
    print(decision,',', bet_type)
    # print(result)
    print('\n')
    time.sleep(1) # delay 2 seconds