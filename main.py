from classes.game import Person, Bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


# Create Black magic
fire = Spell("Fire", 20, 600, "black")
thunder = Spell("Thunder", 20, 600, "black")
blizzard = Spell("Blizzard", 20, 600, "black")
meteor = Spell("Meteor", 40, 1200, "black")
quake = Spell("Quake", 45, 1400, "black")

# Create White magic
cure = Spell("Cure", 25, 620, "white")
cura = Spell("Cura", 35, 1500, "white")

# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "potion", "Heals 500 HP", 1000)
elixer = Item("Elixer", "elixer",
              "Fully restores HP/MP of one party member", 9999)
megaelixer = Item("MegaElixer", "elixer",
                  "Fully restores party's HP/MP", 13000)
grenade = Item("Grenade", "attack", "Deals 500 damage", 900)


player_magic = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": hipotion,
                                                   "quantity": 5},
                {"item": superpotion, "quantity": 5}, {"item": elixer,
                                                       "quantity": 5},
                {"item": megaelixer, "quantity": 2}, {"item": grenade,
                                                      "quantity": 5}]

# Instantiate People
player1 = Person("Shubh:", 4000, 130, 288, 34, player_magic, player_items)
player2 = Person("Valos:", 4600, 140, 250, 34, player_magic, player_items)
player3 = Person("Robot:", 3060, 150, 300, 34, player_magic, player_items)
enemy = Person("Enemy", 12000, 220, 400, 25, [], [])

players = [player1, player2, player3]
running = True

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS" + Bcolors.ENDC)

while running:
    print("================\n\n")
    print("NAME:                 HP                                    MP")
    for player in players:
        player.get_stats()

    print("\n")

    enemy.get_enemy_stats()

    for player in players:
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            player_dmg = player.generate_damage()
            enemy.take_damage(player_dmg)
            print("You attacked for", player_dmg, "damage Points.")

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose Magic: ")) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(Bcolors.FAIL + "\nNot enough MP\n" + Bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(Bcolors.OKBLUE, "\n", spell.name,
                      "Heals for", magic_dmg, "HP", Bcolors.ENDC)

            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(Bcolors.OKGREEN + "\n" + spell.name + " deals", magic_dmg,
                      "points of damage" + Bcolors.ENDC)

        elif index == 2:
            player.choose_items()
            item_choice = int(input("    Choose Item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["quantity"] == 0:
                print(Bcolors.FAIL + "\n" + "There are no more", item.name, "left",
                      Bcolors.ENDC)
                continue

            if item.type == "potion":
                player.heal(item.prop)
                player.items[item_choice]["quantity"] -= 1
                print(Bcolors.OKGREEN, "\n" + item.name, "heals for", item.prop,
                      "HP", Bcolors.ENDC)

            elif item.type == "elixer":

                if item.type == "MegaElixer":
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                player.items[item_choice]["quantity"] -= 1
                print(Bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP"
                      + Bcolors.ENDC)

            elif item.type == "attack":
                enemy.take_damage(item.prop)
                player.items[item_choice]["quantity"] -= 1
                print(Bcolors.FAIL + "\n" + item.name + " deals", item.prop,
                      "points of damage", Bcolors.ENDC)
        else:
            continue

    enemy_choice = 1
    target = random.randrange(0, len(players))

    enemy_dmg = enemy.generate_damage()
    players[target].take_damage(enemy_dmg)
    print("Enemy attacked for", enemy_dmg)

    if player1.get_hp() == 0:
        print(Bcolors.FAIL + "Enemy has defeated you" + Bcolors.ENDC)
        running = False
    elif enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You WIN!" + Bcolors.ENDC)
        running = False
