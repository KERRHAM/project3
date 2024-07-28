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
        for columns in column:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
        
            return winnings, winning_lines

def spin_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def display_slot_machine(columns):

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
def deposit():
    print(
        '''
        Welcome user are you ready to play the slotmachine??
        To play deposit a minimum of £1 to win yourself some tokens!!
        '''
    )


    while True:
        amount = input("How much would you like to deposit to play? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount