import random
import time
from player import decide
import os
import csv
import matplotlib.pyplot as plt  

from numba import jit

# player states
starter_money = 1000 # amount of money player have at the beginning
bet_size = 1 # the money player will bet
rounds = 100 # how many rounds bet will happen
session = 100
tendency = 'random'

@jit(nopython = True)
def roll_wheel():
    '''Get random int from 0 to 36

    Returns:
        int: The number it will generate
    '''

    roll = random.randint(0, 36)
    
    return roll

def run_roulette(session, starter_money, rounds, bet_size, tendency, verbose):
    

# create tmp folder if doesn't exist
    if not os.path.exists('tmp'):
        os.makedirs('tmp')

    for i in range(session):

        win = 0
        lost = 0
        lasted_rounds = 0

        player_money = starter_money
        house_money = 0 # assume house don't have any money

        results_list = []
        player_money_list = []
        house_money_list = []
        lasted_rounds_list = []

        for j in range(rounds):
            roll = roll_wheel()
            bet_type, decision = decide(tendency)
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
            lasted_rounds += 1
            result = [lasted_rounds, player_money, house_money]
            results_list.append(result)

            lasted_rounds_list.append(lasted_rounds)
            player_money_list.append(player_money)
            house_money_list.append(house_money)

        # report results
        print('session {}'.format(i+1))
        print('win:', win, '| lost:', lost)
        print("player's money:", player_money)
        print("house's money:", house_money)
        print('\n')

        # plot it
        plt.plot(lasted_rounds_list, player_money_list)
        plt.plot(lasted_rounds_list, house_money_list)

        with open('tmp/results_{}.csv'.format(i+1), 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Round", "Player's Money", "House's Money"])
            writer.writerows(results_list)

    return lasted_rounds, win, lost, player_money, house_money

lasted_rounds, win, lost, player_money, house_money = run_roulette(
    session,
    starter_money, 
    rounds,
    bet_size,
    tendency,
    verbose = False
)

plt.xlabel('rounds')
plt.ylabel('money')
plt.title('{} sessions of roulette simulation with {} tendency'.format(session, tendency))
plt.savefig('tmp/roulette sim_{}_{} tendency.png'.format(session, tendency))