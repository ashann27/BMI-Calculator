import random
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, level):
        self.hp = 0
        self.level = 1
        self.max_hp = level*10
    #add item slot later
    pass

class Player (Character):
    def __init__(self, level):
        super().__init__(level)

        max_hp = level * 10
        self.max_hp = max_hp

        current_hp = max_hp
        self.current_hp = current_hp

        attack = level * 3
        self.attack = attack

        exp = 0
        self.exp = exp

class Enemy (Character):

    def __init__(self, level):
        super().__init__(level)

        max_hp = level * random.randint(7,12)
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = level * 3

        enemy_types = ['ゴキブリ','へび','ウルフ','ヒューマン','さる','ゴリラ','サメ','白クマ','カバ']
        self.name=enemy_types[level]

        if self.hp < level * 9:
            self.title = '弱い'
            self.exp = self.attack + (self.attack * .7)
        elif self.hp >= level * 11:
            self.title = '強い'
            self.exp = self.attack + (self.attack * 1.3)
        else:
            self.title = '普通'


# item info generator method?

# the more fights the player says yes to, the more difficult the enemy's level ratio becomes
# and vice versa

def start_game():
    player = Player(1)
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
        elif turn % 2 != 1:
            print('{}が{}攻撃をしました！'.format(enemy.name, enemy.title))
            player.hp -= enemy.attack
            turn += 1

    if enemy.hp == 0:
        player.hp = player.max_hp
        player.exp += enemy.max_hp
        print('{}{}を倒しました！{}expをもらいました.'.format(enemy.title, enemy.name, enemy.exp))
    elif player.hp == 0:
        player.hp = player.max_hp
        player.exp += (enemy.max_hp/2)
        print('負けました！半分ぐらいの{}expをもらいました')


    if player.exp > player.max_hp:
        print('レベルアップできました！')
        new_level = player.level+1

        return player
    else:
        return player

start_game()