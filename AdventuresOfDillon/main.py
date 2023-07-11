from random import randint
import player as playa
import enemy1 as bigboypants

choseClass = False
answer1 = True

print('Welcome to the Adventures of Dillon. First we need you to pick a class.')
print('The classes are Berserk: Where you get a sword that does 30 damage, 5 speed, and an ability that lets you deal 2x damage for 3 turns.')
print('Mage: Where you get a staff that does 25 damage, 10 speed, and an ability that lets you set the enemy on fire, dealing 5 damage until either them or you are dead.')
print('Rogue: Where you get a dagger that does 15 damage, 45 speed, and an ability that lets you dodge the enemy attacks')
print('Archer: Where you get a bow that does 20 damage, 8 speed, and an ability that lets you shot 2 arrows at once with your bow fully charged back')

while choseClass == False:
    classInt = int(input('So what will it be. 1 for Berserk, 2 for Mage, 3 for rogue, or 4 for archer '))
    if classInt == 1:
        Player = playa.player("Berserk", "GO BERSERK", 5, 30, "Starter Sword", 200)
        choseClass = True
    elif classInt == 2:
        Player = playa.player("Mage", "Fire", 10, 25, "Starter Staff", 150)
        choseClass = True
    elif classInt == 3:
        Player = playa.player("Rogue", "Avoid Attack", 45, 15, "Starter Dagger", 125)
        choseClass = True
    elif classInt == 4:
        Player = playa.player("Archer", "double shot at full charge", 5, 20, "Starter Bow", 165)
        choseClass = True
    else:
        print("That is not an option.")

print("You encounter your first boss. You can click: \n1 to attack,\n2 to block, \n3 to use an item, \n 4 to attempt to run.")
while answer1:
    answer = int(input('What shall you do? '))
    if answer == 1:
        answer1 = False
    elif answer == 2:
        answer1 = False
    elif answer == 3:
        answer1 = False
    elif answer == 4:
        answer1 = False
    else:   
        print('This is not an option')

