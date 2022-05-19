import random
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, level):
        self.hp = 0
    #add defense later
    #add item slot later
    pass

class Player (Character):
    def __init__(self):
        super().__init__(name, level)
        self.level = 1
        self.hp = level * 10
        self.attack = level * 3
        self.exp = 0

    #level up method
        # player levels up every time they increase exp by 2, scales so you never have to beat more than 5 enemies to level up
        # exp gained is based on current level x enemy level bonus

class Enemy (Character):

    def __init__(self):
        super().__init__(level)
        self.level = level
        self.hp = level * random.randint(7,12)
        self.attack = level * random.randit(3)

        enemy_types = ['ゴキブリ','へび','ウルフ','ヒューマン','さる','ゴリラ','サメ','白クマ','カバ']
        self.name=enemy_types[level]

        if hp < level * 9:
            self.title = '弱い'
            self.exp = attack + (attack * .7)
        elif hp >= level * 11:
            self.title = '強い'
            self.exp = attack + (attack * 1.3)
        else:
            self.title = '普通'
        #items?




    def attack():
        pass

# item info generator method

#level_up method
# level up multiplies all stats by 1.5 and
# level up lowers enemy stat ratiomkk


# victory bonus exp

# loss penalty exp

# the more fights the player says yes to, the more difficult the enemy's level ratio becomes
# and vice versa

# character data can be saved to text file

def start_game():
    player = Player()
    while True:
        enemy = Enemy(player.level)
        cmd = input('{} {}が来ました！戦おうとしてるらしい、どうしますか？\n'
                '攻撃「A」　　　　逃げる「R」      やめる 「Q」\n'.format(enemy.title, enemy.name))
        if cmd.lower() == 'a':
            fight(player, enemy)

        elif cmd.lower() == 'r':
            print('ギリギリ逃げた！よかったね\n')
            continue

        elif cmd.lower() == 'q':
            break

        else: print('{} は選択に入ってません。また入力してください'.format(cmd))

#def attack(Player, Enemy):

def fight(player, enemy):
    print('戦いが始まりました！')
    turn = 1
    while player.hp > 0 and enemy.hp > 0:
        if turn % 2 == 1:
            print('あなたが攻撃しました！')
            enemy.hp -= player.attack
            turn += 1
        if turn % 2 == 1:
            print('{}が{}攻撃をしました！'.format(enemy.name, enemy.title))
            player.hp -= enemy.attack
            turn += 1

    if enemy.hp == 0:
        print('{}{}を倒しました！{}expをもらいました。次のレベルは後{}expだけです！'.format(enemy.title, enemy.name, enemy.exp))