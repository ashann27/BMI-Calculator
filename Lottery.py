import random
user_wallet =  5000
cash_prize_list = [0,10,50,100,500,1000,5000]
winning_lottery_numbers = set()
user_lottery_numbers = set()
def start_game():
    global user_wallet
    global cash_prize_list
    global winning_lottery_numbers
    print('\nこの宝くじでは、6つの数字があります。マッチすればするほど、お金がもらえます！\n')
    i=0
    while i<=6:
        print('{}番号マッチ　＝　${}　GET！'.format(i, cash_prize_list[i]))
        i+=1
    #populates winning lottery numbers set
    while len(winning_lottery_numbers)<6:
        winning_lottery_numbers.add(random.randint(1,20))
    return winning_lottery_numbers

def buy_ticket():
    global user_wallet
    print('\n今 ${}　を持っています'.format(user_wallet))
    if user_wallet >= 50:
        global user_lottery_numbers

        #reads the user's input and makes a list
        user_lottery_numbers_input = input('好きな番号を1～20の間で6つ入力してください。各番号の間にはスペースを入れてください。 EX:1 8 20 14 15 11\n').split(' ')
        if len(user_lottery_numbers_input) == 6:
            user_lottery_numbers = {int(n) for n in user_lottery_numbers_input}
            user_wallet -= 50
        elif len(user_lottery_numbers_input) < 6:
            print('入力した数字が少ないです! また入力してください。')
            buy_ticket()
        elif len(user_lottery_numbers_input) > 6:
            print('入力した数字が多すぎます! また入力してください。')
            buy_ticket()
    else:
        print('お金は足りないです!')
    return user_lottery_numbers

def lottery_draw(winning_lottery_numbers, user_lottery_numbers):
    global user_wallet
    global cash_prize_list
    matching_numbers = winning_lottery_numbers.intersection(user_lottery_numbers)
    cash_prize = int(cash_prize_list[len(matching_numbers)])
    print('当せん番号は{}. {}つの当選番号をあたりました！ 当せん金は${}'.format(winning_lottery_numbers, len(matching_numbers), cash_prize))
    user_wallet += cash_prize
    user_continue = input('\n続きますか? Y＝はい N＝いいえ')
    if user_continue.lower() == 'y':
        lottery_draw(start_game(), buy_ticket())
    else:
        print('お疲れ様です!')


lottery_draw(start_game(), buy_ticket())