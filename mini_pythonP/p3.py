import random



MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5, 
    "B": 4,
    "C": 3,
    "D": 2
}
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
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
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
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
def deposit():
    while True:
        amount = input("Enter amount the want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print(f"You have deposited ${amount}.")
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Invalid input. Please enter a number.")
    return amount
  
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINE}) :")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINE:
                return lines
            else:
                print(f"Number of lines must be between 1 and {MAX_LINE}.")
        else:
            print("Invalid input. Please enter a number.")
    return lines
def get_bet():
    while True:
        amount = input(f"Enter the bet amount per line (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Invalid input. Please enter a number.")
def main():
    print("Welcome to the Slot Machine!")
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = lines * bet
    if total_bet > balance:
        print(f"You do not have enough balance to bet on {lines} lines. Your current balance is ${balance}.")
        return
    
    print(f"You have bet on {lines} lines with a total balance of ${balance}.")
    print(f"Total bet amount: ${total_bet}")
    # Here you can add the logic for spinning the slot machine and calculating winnings
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"You won ${winnings}!")
    if winning_lines:
        print(f"You won on lines: {', '.join(map(str, winning_lines))}")

main()
