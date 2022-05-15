import random

def start_game():
    user_wallet =  5000
    winning_lottery_numbers = set()

    #populates winning lottery numbers set
    while len(winning_lottery_numbers)<5:
        winning_lottery_numbers.add(random.randint(1,20))
    return winning_lottery_numbers

def buy_ticket():
    global user_wallet
    if user_wallet >= 50:
        user_lottery_numbers = set()

        #reads the user's input and makes a list
        user_lottery_numbers_input = input('Please enter 6 lottery numbers between 1-20. Use a space in between each number. EX:1 8 20 14 15 11\n').split(' ')
        if len(user_lottery_numbers_input) == 6:
            user_lottery_numbers = {int(6) for n in user_lottery_numbers_input}
            user_wallet -= 50
        elif len(user_lottery_numbers_input) < 6:
            print('You didn\'t enter enough numbers! Please try again. \n')
            buy_ticket()
        elif len(user_lottery_numbers_input) > 6:
            print('You entered too many numbers! Please try again \n')
            buy_ticket()
    else:
        print('sorry you\'re out of money!\n')