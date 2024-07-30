import random

# Variable for declaring maximum lines to chose from (3)
MAX_LINES = 3
# Variable for declaring Maximum bet for a user to deposit(£100)
MAX_BET = 100
# Variable for decalaring Minimum bet for a user to deposit(£1)
MIN_BET = 1
# Variable for number of rows in game (3)
rows = 3
# Variable for number of columns in game (3)
cols = 3

# Dicitionary for number of symbols to generate
# 2 A's, 4 B's, 6 C's & 8 D's
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
# Dictionary for storing Value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function for checking the rows for a sequence of 3 of the same symbols and
# adding the number of winning lines to a list and calculating winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)


    return winnings, winning_lines

# Function for generating random rows/columns of symbols
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

# Function for displaying game board
# Empty print() used to start newline after board is displayed for vertical spacing
def display_slot_machine(columns):

    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()

# Function for Depositing funds from the user to play the game and
# for checking deposit entered is > 0 and is a number(Integer)
def deposit():
    print(
        '''
        Welcome user are you ready to play the slotmachine??
        To play deposit a minimum of £1 to win yourself some tokens!!
        '''
    )


    while True:
        amount = input("How much would you like to deposit to play? £\n")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# Function for declaring number of lines wanted by user and for checking
# number of lines is between 1-3 and a number(integer)
def get_number_of_lines():

    while True:
        lines = input("Please enter the number of lines you would like to deposit your money on? (1-" + str(MAX_LINES) + ")?\n ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

# Function for user to input what funds they wish to deposit on lines chosen,
# Function also checks if funds deposited is between 1-100 and checks if input is 
# a number(Integer)
def get_bet():

    print(
        '''
        The slot machine has 3 lines with 4 Symbols, A B C D
        Value A will Multiply your bet by 5
        Value B will Multiply your bet by 4
        Value C will Multiply your bet by 3
        Value D will Multiply your bet by 2
        '''
    )
    while True:
        amount = input("How much would you like to deposit on each line? £\n")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET <=100:
                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

# Function for informing user how much they have deposited on lines requested and total bet to play,
# Function checks to see if users next deposit is less than or equal to users balance,
# After the game is run,the function will display number of tokens/number of lines won
def spin(balance):
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You dont have enough funds to place this bet, Your current balance is: £{balance}")
        else:
            break
    
    print(f"you are betting £{bet} on {lines} lines, your total bet is equal to: £{total_bet}")

    slot = spin_slot_machine(rows, cols, symbol_count) 
    display_slot_machine(slot)
    winnings, winning_lines = check_winnings(slot, lines, bet, symbol_value)
    print(f"You won {winnings} Tokens!!.")
    print(f"you won on lines:", *winning_lines)
    return winnings - total_bet

# Function will run while balance is more than or equal to 1,
# If balance is less than 1 the program will terminate, The user
# will be informed of how many tokens won and how to play again
def main():
    balance = deposit()
    while balance >= 1:
        print(f"Current balance is £{balance}")
        result = input("Press enter to Play (Press q to quit) ")
        if result == "q":
            break
        balance += spin(balance)
    
    print(f"You left with {balance} Token's")
    print("To play again, Click run to deposit more funds!!")
    
main()