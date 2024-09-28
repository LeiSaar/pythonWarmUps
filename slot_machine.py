import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value ={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}



def create_slots(rows, cols):
    rowList = []
    symbols = []
    for symbol, count in symbol_count.items():
        for _ in range(count):
            symbols.append(symbol)
    # print(symbols)
    for _ in range(rows):
        row = []
        symbol = symbols[:]
        for _ in range(cols):
            value = random.choice(symbol)
            symbol.remove(value)
            row.append(value)
        rowList.append(row)
    return rowList     

""" slots = create_slots(3, 4)
print(slots)   """  


def print_slots(slots):
    for i in range(len(slots)):
        for j in range(len(slots[i])):
            if j < len(slots[i]) - 1: 
               print(slots[i][j], " | ", end = "")
            else:
               print(slots[i][j]) 
        
""" slots = create_slots(3, 4)
print_slots(slots) """

def playGame(rows, cols):
     balance = deposit()
     while True:
            winnings = 0
            answer = input("Would you like to bet? Press enter to continue and 'q' to quit ")
            if answer == 'q':
                break
            lines = get_lines()
            bet = get_bet()
            total_bets = lines * bet
            if balance < total_bets:
                print("Your bet amount is bigger than your balance!")
                continue
            balance -= total_bets
            slots = create_slots(rows, cols)
            print(slots)
            print_slots(slots)
            for i in range(lines):
                symbol = slots[i][0]
                for j in range(len(slots[0])):
                    print(symbol, slots[i][j])
                    if slots[i][j] != symbol:
                        break
                else:
                    """ print("############")
                    print("got something")
                    print(symbol)
                    print("############") """
                    winnings += bet * symbol_value[symbol]
            print(f"You won ${winnings} in this round")
            balance += winnings
            print(f"Your current balance is ${balance}")


def deposit():
   while True:
       amount = input("How much money do you want to deposit? $ ")
       if amount.isdigit():
           amount = int (amount)
           if MIN_BET <= amount <= 100 :
               break
           else:
               print("Please enter a valid amount")
       else:
           print("Please enter a number")
   
   return amount

""" balance = deposit()
print(f'balance is {balance}') """

def get_lines():
    while True:
        lines = input("Please enter the lines you want to bet: from (1 - " + str(MAX_LINE) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                return lines
            else:
                print("Plese enter a valid number of lines")
        else: 
            print("Please enter a number")

""" lines = get_lines()
print(f"Your bet line(s) is {lines} ") """

def get_bet():
    while True:
        bet = input("What would you like to bet in each line? $ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please give a valid bet amount between {MIN_BET} and {MAX_BET}" )
        else:
            print("Please enter a number")
    return bet

# print(f"Your bet for each line is {get_bet()}")

def main():
    playGame(ROWS, COLS)

main()

slots = create_slots(ROWS, COLS)
print_slots(slots)

if "__name__" == "__main__":
    main()