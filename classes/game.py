import random


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, mag, item):
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atkl = atk-10
        self.atkh = atk+10
        self.df = df
        self.magic = mag
        self.items = item
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_hp(self):
        return self.max_hp

    def get_hp(self):
        return self.hp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print("\n    " + Bcolors.BOLD + self.name + Bcolors.ENDC)
        print(Bcolors.OKBLUE + Bcolors.BOLD + "    ACTIONS:" + Bcolors.ENDC)
        for item in self.actions:
            print("        " + str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + Bcolors.OKBLUE + Bcolors.BOLD + "    MAGIC:" +
              Bcolors.ENDC)
        for item in self.magic:
            print("        " + str(i), ".", item.name, "(costs :",
                  item.cost, ")")
            i += 1

    def choose_items(self):
        i = 1
        print("\n" + Bcolors.OKGREEN + Bcolors.BOLD + "    ITEMS:" +
              Bcolors.ENDC)
        for item in self.items:
            print("        " + str(i) + ".", item["item"].name + ":",
                  item["item"].description, "(x" + str(item["quantity"]) + ")")
            i += 1

    def get_enemy_stats(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 50
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        hplen = str(self.hp)
        if len(hplen) != 5:
            hplen = " " + hplen

        mplen = str(self.mp)
        if len(mplen) != 3:
            mplen = " " + mplen

        print(
            "                     __________________________________________________")
        print(Bcolors.BOLD + self.name + "    " +
              hplen + "/" + str(self.max_hp) + "|" + Bcolors.FAIL +
              hp_bar + Bcolors.ENDC + "|")

    def get_stats(self):
        hp_bar = ""
        mp_bar = ""
        bar_ticks = (self.hp / self.max_hp) * 25
        mp_ticks = (self.mp / self.max_mp) * 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        hplen = str(self.hp)
        if len(hplen) != 4:
            hplen = " " + hplen

        mplen = str(self.mp)
        if len(mplen) != 3:
            mplen = " " + mplen

        print(
            "                      _________________________       "
            "      __________                 ")
        print(Bcolors.BOLD + self.name + "      " +
              hplen + "/" + str(self.max_hp) + "|" + Bcolors.OKGREEN +
              hp_bar + Bcolors.ENDC + Bcolors.BOLD + "|    " +
              mplen + "/" + str(self.max_mp) + "|" + Bcolors.OKBLUE +
              mp_bar + Bcolors.ENDC + "|")