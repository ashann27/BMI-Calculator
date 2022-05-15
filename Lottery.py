import random
user_wallet =  5000
cash_prize_list = [0,10,50,100,500,1000,5000]
winning_lottery_numbers = set()
user_lottery_numbers = set()
def start_game():
    global user_wallet
    global cash_prize_list
    global winning_lottery_numbers
    print('In this game there are 6 numbers. The more you match, the more money you get!')
    i=0
    while i<=6:
        print('{} match(es) gets you ${}'.format(i, cash_prize_list[i]))
        i+=1
    #populates winning lottery numbers set
    while len(winning_lottery_numbers)<6:
        winning_lottery_numbers.add(random.randint(1,20))
    return winning_lottery_numbers

def buy_ticket():
    global user_wallet
    print('You currently have ${}\n'.format(user_wallet))
    if user_wallet >= 50:
        global user_lottery_numbers

        #reads the user's input and makes a list
        user_lottery_numbers_input = input('Please enter 6 lottery numbers between 1-20. Use a space in between each number. EX:1 8 20 14 15 11\n').split(' ')
        if len(user_lottery_numbers_input) == 6:
            user_lottery_numbers = {int(n) for n in user_lottery_numbers_input}
            user_wallet -= 50
        elif len(user_lottery_numbers_input) < 6:
            print('You didn\'t enter enough numbers! Please try again. \n')
            buy_ticket()
        elif len(user_lottery_numbers_input) > 6:
            print('You entered too many numbers! Please try again \n')
            buy_ticket()
    else:
        print('sorry you do not have enough money!\n')
    return user_lottery_numbers

def lottery_draw(winning_lottery_numbers, user_lottery_numbers):
    global user_wallet
    global cash_prize_list
    matching_numbers = winning_lottery_numbers.intersection(user_lottery_numbers)
    cash_prize = int(cash_prize_list[len(matching_numbers)])
    print('The winning numbers are {}. You got {} numbers right! Your cash prize is ${}'.format(winning_lottery_numbers, len(matching_numbers), cash_prize))
    user_wallet += cash_prize
    user_continue = input('Try again? Please enter Y for yes or N for no')
    if user_continue.lower() == 'y':
        lottery_draw(start_game(), buy_ticket())
    else:
        print('Thanks for playing!')


lottery_draw(start_game(), buy_ticket())