import random
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, level):
        self.hp = 0
        self.level = 1
    #add item slot later
    pass

class Player (Character):
    def __init__(self, level):
        super().__init__(level)

        max_hp = level * 10
        self.max_hp = max_hp

        hp = max_hp
        self.hp = hp

        attack = level * 3
        self.attack = attack

        exp = 0
        self.exp = exp

class Enemy (Character):

    def __init__(self, level):
        super().__init__(level)

        low = 7+level
        high = 12+level
        max_hp = level * random.randint(low,high)
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = (level * random.randint(3, 6))

        enemy_types = ['ゴキブリ','へび','ウルフ','ヒューマン','さる','ゴリラ','サメ','白クマ','カバ']
        self.name=enemy_types[level-1]

        if self.hp < level * 9:
            self.title = '弱い'
            self.exp = self.attack + (self.attack * .7)
        elif self.hp >= level * 11 or self.attack==4:
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
        cmd = input('{}{}(HP:{} ATK:{})が来ました！戦おうとしてるらしい、どうしますか？ (自分がさきあに攻撃します）\n'
                    '自分:{} HP  {} ATK\n\n'
                    '攻撃「A」　　　　逃げる「R」      やめる 「Q」\n'.format(enemy.title, enemy.name,enemy.hp,enemy.attack, player.hp, player.attack))
        if cmd.lower() == 'a':
            fight(player, enemy)

        elif cmd.lower() == 'r':
            print('ギリギリ逃げた！よかったね\n')
            continue

        elif cmd.lower() == 'q':
            break

        else: print('{} は選択に入ってません。また入力してください\n'.format(cmd))

#def attack(Player, Enemy):

def fight(player, enemy):
    print('戦いが始まりました！')
    turn = 1
    battling = 1
    while player.hp > 0 and enemy.hp > 0 and battling ==1:
        if turn % 2 == 1:
            enemy.hp -= player.attack
            enemy.hp = round(enemy.hp)
            turn += 1
        elif player.hp - enemy.attack <= 0:
            battling ==0
            break
        elif turn % 2 != 1 and enemy.hp > 0:
            player.hp -= enemy.attack
            turn += 1
            answer = input('ラウンド終了！\n'
                           '     HP　　　　　　　　ATK\n'
                           '自分　{}              {}\n'
                           '敵　　{}              {}\n'
                           '\n [F] = 続く　[R] = ギブアップ(8分の１expゲット)\n'.format(player.hp, player.attack, enemy.hp, enemy.attack))
            thinking = 1
            while thinking == 1:
                if answer.lower() == 'f':
                    thinking = 0
                    continue
                elif answer.lower() == 'r':
                    player.hp = player.max_hp
                    player.exp += round((enemy.max_hp/8), 2)
                    print('逃げました！少しだけの{}expをもらいました\n'.format(enemy.max_hp/8))
                    battling = 0
                    break
                else: answer = input('{} は選択に入ってません。また入力してください\n'.format(answer))
        else: continue

    if  enemy.hp <= 0:
        player.hp = player.max_hp
        player.exp += round((enemy.max_hp/(2*enemy.level)),2)
        player.attack += round(player.exp/10, 2)
        print('{}{}を倒しました！{}expをもらいました.\n'
              '攻撃力が少し増えました！\n'.format(enemy.title, enemy.name, (enemy.max_hp/(2*enemy.level)),2))
    elif player.hp <= 0 or player.hp - enemy.attack <= 0:
        player.hp = player.max_hp
        player.exp += round((enemy.max_hp/4),2)
        print('負けました！でも最後まで頑張ったので{}expをもらいました\n'.format(enemy.max_hp/4))


    if player.exp > player.level*player.max_hp:
        print('レベルアップできました！\n')
        player.level+=1
        player.max_hp = player.level*10
        player.attack = round((player.level * 3)+(player.exp/10),2)
        player.hp = player.max_hp


        return player
    else:
        print('レベルアップは後{}expだけ！\n'.format((player.level*player.max_hp)-player.exp))
        return player

start_game()