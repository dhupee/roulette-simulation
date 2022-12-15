# roulette-simulation

My simulation of a Roulette Casino's profit, run in Python 3.10

- [roulette-simulation](#roulette-simulation)
  - [Installing Dependencies](#installing-dependencies)
  - [Usage](#usage)
  - [bet-odds-table](#bet-odds-table)

## Installing Dependencies

I use Python 3.10 for this program.

`pip install -r requirements.txt`

## Usage

```sh
usage: main.py [-h] -sm STARTER_MONEY [-b BET_SIZE] [-r ROUNDS] [-s SESSIONS] [-t {random,safe,dangerous}]

A monte carlo simulation of a roulette

options:
  -h, --help            show this help message and exit
  -sm STARTER_MONEY, --starter_money STARTER_MONEY
                        the money player will have initially
  -b BET_SIZE, --bet_size BET_SIZE
                        The amount of bet player will place
  -r ROUNDS, --rounds ROUNDS
                        How many rounds of bettings of each session
  -s SESSIONS, --sessions SESSIONS
                        How many sessions the simulation will run
  -t {random,safe,dangerous}, --tendency {random,safe,dangerous}
                        Tendency of player of betting choice

```

## bet-odds-table

Source: [Bet Odds Tabel (Wikipedia)]([https://](https://en.wikipedia.org/wiki/Roulette#Bet_odds_table))
