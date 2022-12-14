import random
from player import decide
import os
import csv
import matplotlib.pyplot as plt
from numba import jit

@jit(nopython = True)
def roll_wheel():
    '''Get random int from 0 to 36

    Returns:
        int: The number it will generate
    '''

    return random.randint(0, 36)

def run_roulette(sessions, starter_money, rounds, bet_size, tendency, verbose):
    

# create csv folder if doesn't exist
    if not os.path.exists('csv'):
        os.makedirs('csv')

    for i in range(sessions):

        win = 0
        lost = 0
        lasted_rounds = 0

        player_money = starter_money
        house_money = 0 # assume house don't have any money

        results_list = []
        player_money_list = []
        house_money_list = []
        lasted_rounds_list = []

        for _ in range(rounds):
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
                if roll in decision:
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
                if roll in decision:
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
            elif bet_type in ['corner', 'basket']: # payout 8 to 1
                if roll in decision:
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
                if roll in decision:
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
            elif bet_type in ['column', 'dozen']: # payout 2 to 1
                if roll in decision:
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
            elif bet_type in ['odd_or_even', 'red_or_black', 'half']: # payout 1 to 1
                if roll in decision:
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
        print(f'session {i + 1}')
        print('win:', win, '| lost:', lost)
        print("player's money:", player_money)
        print("house's money:", house_money)
        print('\n')

        # plot it
        plt.plot(lasted_rounds_list, player_money_list)
        plt.plot(lasted_rounds_list, house_money_list)

        with open(f'csv/results_{i + 1}.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Round", "Player's Money", "House's Money"])
            writer.writerows(results_list)

    return lasted_rounds, win, lost, player_money, house_money