from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# Create Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")


#Create White Magic
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")


# Create some items
potion = Item ("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item ("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotion = Item ("Super-Potion", "potion", "Heals 500 HP", 500)
elixir = Item ("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item ("MegaElixir", "elixir", "Fully restores party HP/MP", 9999)

grenade = Item ("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [potion, hipotion, superpotion, elixir, hielixir, grenade]

#Instantiate People
player = Person (460, 65, 60, 34,player_spells, player_items)
enemy = Person (1200, 65, 45, 25, [], [])

running = True
i=0

print (bcolors.FAIL +bcolors.BOLD + "An enemy attacks!!!" + bcolors.ENDC)

while running:
    print ("=============")
    player.chose_action()
    choice = input ("Chose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print ("Yout attacked for", dmg, "points of damage.")
    elif index ==1:
        player.chose_magic()
        magic_choice = int(input("Chose magic: "))-1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print (bcolors.FAIL + "\nNot Enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)

        if spell.type == "White":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for ", str (magic_dmg), "HP"+bcolors.ENDC)
        elif spell.type == "Black":
            enemy.take_damage(magic_dmg)
            print (bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage"+ bcolors.ENDC)
    elif index == 2:
        player.chose_item()
        item_choice = int (input ("Chose item: ")) - 1

        if item_choice == -1:
            continue

        item = player_items[item_choice]

        if item.type == "potion":
            player.heal(item.prop)
            print ()

    enemy_choice = 1
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy Retaliated for", enemy_dmg, "points of damage.")

    print("-----------------")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp())+ "/"+ str(player.get_maxhp())+bcolors.ENDC)
    print("Your MP:", bcolors.OKGREEN + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC + "\n")
    print("Enemy HP:", bcolors.FAIL + str (enemy.get_hp())+ "/"+str(enemy.get_maxhp())+bcolors.ENDC+ "\n")


    if enemy.get_hp()==0:
        print (bcolors.OKGREEN + "You Win!!!" + bcolors.ENDC)
        running = False
    elif player.get_hp()==0:
        print (bcolors.FAIL + "The Enemy has killed you" + bcolors.ENDC)
        running = False