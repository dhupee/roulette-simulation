import random
import time
from player import decide
import os
import csv
import matplotlib

from numba import jit

# player states
martingale = False # for Martingale simulation
anti_martingale = False
player_money = 1000000 # amount of money player have
house_money = 0 # assume house don't have any money
bet_size = 10 # the money player will bet
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

def run_roulette(player_money, house_money, bet_size, verbose):
    win = 0
    lost = 0
    round = 0

# create tmp folder if doesn't exist
    if not os.path.exists('tmp'):
        os.makedirs('tmp')

    results_list = []

    start = time.perf_counter()
# TODO: add results to csv
    while player_money >= 0: # repeat until player's money empty
        roll = roll_wheel()
        bet_type, decision = decide()
        if verbose == True:
            print(decision,',', bet_type)
    # check if win or lost the best
        if bet_type == 'single': # payout 35 to 1
            if roll == decision:
                payout = 35
                win += 1
                player_money += bet_size*payout
                house_money -= bet_size*payout
                if verbose == True:
                    print('win')
            else:
                lost += 1
                player_money -= bet_size
                house_money += bet_size
                if verbose == True:
                    print('lost')
        elif bet_type == 'split': # payout 17 to 1
            if roll == decision:
                payout = 17
                win += 1
                player_money += bet_size*payout
                house_money -= bet_size*payout
                if verbose == True:
                    print('win')
            else:
                lost += 1
                player_money -= bet_size
                house_money += bet_size
                if verbose == True:
                    print('lost')
        elif bet_type == 'street': # payout 11 to 1
            if roll == decision:
                payout = 11
                win += 1
                player_money += bet_size*payout
                house_money -= bet_size*payout
                if verbose == True:
                    print('win')
            else:
                lost += 1
                player_money -= bet_size
                house_money += bet_size
                if verbose == True:
                    print('lost')
        elif bet_type == 'corner' or bet_type == 'basket': # payout 8 to 1
            if roll == decision:
                payout = 8
                win += 1
                player_money += bet_size*payout
                house_money -= bet_size*payout
                if verbose == True:
                    print('win')
            else:
                lost += 1
                player_money -= bet_size
                house_money += bet_size
                if verbose == True:
                    print('lost')
        elif bet_type == 'double_street': # payout 5 to 1
            if roll == decision:
                payout = 5
                win += 1
                player_money += bet_size*payout
                house_money -= bet_size*payout
                if verbose == True:
                    print('win')
            else:
                lost += 1
                player_money -= bet_size
                house_money += bet_size
                if verbose == True:
                    print('lost')
        elif bet_type == 'column' or bet_type == 'dozen': # payout 2 to 1
            if roll == decision:
                payout = 5
                win += 1
                player_money += bet_size*payout
                house_money -= bet_size*payout
                if verbose == True:
                    print('win')
            else:
                lost += 1
                player_money -= bet_size
                house_money += bet_size
                if verbose == True:
                    print('lost')
        elif bet_type == 'odd_or_even' or bet_type == 'red_or_black' or bet_type == 'half': # payout 1 to 1
            if roll == decision:
                payout = 1
                win += 1
                player_money += bet_size*payout
                house_money -= bet_size*payout
                if verbose == True:
                    print('win')
            else:
                lost += 1
                player_money -= bet_size
                house_money += bet_size
                if verbose == True:
                    print('lost')
        round += 1
        result = [round, player_money, house_money]
        results_list.append(result)
    end = time.perf_counter()

    with open('tmp/results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Round", "Player's Money", "House's Money"])
        writer.writerows(results_list)
    
    time_taken = (end - start)

    return round, win, lost, time_taken, player_money, house_money

round, win, lost, time_taken, player_money, house_money = run_roulette(
    player_money, 
    house_money, 
    bet_size, 
    verbose = False
)

print('\n')
print('win:', win, '| lost:', lost)
print('\n')
print("player's money:", player_money)
print("house's money:", house_money)
print('it lasted {} rounds'.format(round))
print("It takes = {}s".format(time_taken))