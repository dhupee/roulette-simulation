import matplotlib.pyplot as plt
from game import run_roulette

# TODO: add cli on this states
# player states
starter_money = 1000 # amount of money player have at the beginning
bet_size = 10 # the money player will bet
rounds = 100 # how many rounds bet will happen
sessions = 100 # how many sessionss of roulette
tendency = 'safe'

if __name__ == '__main__':

    lasted_rounds, win, lost, player_money, house_money = run_roulette(
        sessions,
        starter_money, 
        rounds,
        bet_size,
        tendency,
        verbose = False
    )

    plt.xlabel('rounds')
    plt.ylabel('money')
    plt.title(f'{sessions} sessions of roulette simulation with {tendency} tendency')
    plt.savefig(f'roulette sim_{sessions}_{tendency} tendency.png')