import random

max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, bets, values, lines):
    winnings = 0
    winning_lines = []
    for lines in range(lines):
        symbol = columns[0][line]
        for coloumns in coloumn:
            symbol_to_check = coloumn[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        
            return winnings, winning_lines


