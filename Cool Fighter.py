import random
from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, hp, attack, defense):
        self.hp = 0
        self.attack = 0
        self.defense = 0

    #add item slot later
    pass

class Player (Character):
    ZZ#level up method
        # player levels up every time they increase exp by 2, scales so you never have to beat more than 5 enemies to level up
        # exp gained is based on current level x enemy level bonus


# foes class
# enemy hp is based on a range around players attributes
# item generator, use word generator and make a sentence that autofills effects and name for an item. affect is random stat buff/nerf

# item class

# item info generator method

#level_up method
# level up multiplies all stats by 1.5 and
# level up lowers enemy stat ratiomkk


# victory bonus exp

# loss penalty exp

# the more fights the player says yes to, the more difficult the enemy's level ratio becomes
# and vice versa

# character data can be saved to text file