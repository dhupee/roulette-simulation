#!/usr/bin/env python 

import argparse
import matplotlib.pyplot as plt
from game import run_roulette

parser = argparse.ArgumentParser(
    description = 'A monte carlo simulation of a roulette',
    add_help = True
)

parser.add_argument('-sm',
                    '--starter_money',
                    type = int,
                    required=True,
                    help='the money player will have initially'
)

parser.add_argument('-b',
                    '--bet_size',
                    type = int,
                    default = 10,
                    help='The amount of bet player will place'
)

parser.add_argument('-r',
                    '--rounds',
                    type = int,
                    default = 100,
                    help='How many rounds of bettings of each session'
)

parser.add_argument('-s',
                    '--sessions',
                    type = int,
                    default = 100,
                    help = 'How many sessions the simulation will run'
)

parser.add_argument('-t',
                    '--tendency',
                    type = str,
                    default = 'random',
                    choices = ['random', 'safe', 'dangerous'],
                    help = 'Tendency of player of betting choice'
)

args = parser.parse_args()

# player states
starter_money = args.starter_money
bet_size = args.bet_size
rounds = args.rounds
sessions = args.sessions
tendency = args.tendency

if __name__ == '__main__':

    lasted_rounds, win, lost, player_money, house_money, avg_profit, avg_loss = run_roulette(
        sessions,
        starter_money, 
        rounds,
        bet_size,
        tendency,
        verbose = False
    )

    print(f'Average Gross Profit is {avg_profit}')
    print(f'Average Gross Loss is {avg_loss}')

    plt.xlabel('rounds')
    plt.ylabel('money')
    plt.title(f'{sessions} sessions of roulette simulation with {tendency} tendency')
    plt.savefig(f'roulette sim_{sessions}_{tendency} tendency.png')