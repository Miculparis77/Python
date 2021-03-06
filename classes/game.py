import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk +10
        self.df = df
        self.magic = magic
        self.items = items
        self.action = ["Attack", "Magic", "Use item" ]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -=dmg
        if self.hp<0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_maxmp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -=cost

    def chose_action(self):
        print ("\nACTIONS")
        i=1
        for item in self.action:
            print("    "+str(i) + ".", item)
            i +=1

    def chose_magic(self):
        print("\nMAGIC")
        i=1
        for spell in self.magic:
            print ("    "+str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i = i+1

    def chose_item(self):
        print ("\nItem")
        i=1
        for item in self.items:
            print ("    "+str(i)+ ":", item.name, ':', item.description, "(x5)")
            i+=1



