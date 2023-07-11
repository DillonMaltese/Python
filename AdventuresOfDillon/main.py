from random import randint
import player as playa
import enemy1 as bigboypants
import weapons as wepawn

choseClass = False
answer1 = False
answer2 = False
specialAttack = False

sword = wepawn.weapon("Starter Sword", "Sword", 7, 100)
staff = wepawn.weapon("Starter Staff", "Staff", 7, 100)
dagger = wepawn.weapon("Starter Dagger", "Dagger", 7, 100)
bow = wepawn.weapon("Starter Bow", "Bow", 7, 100)

print('Welcome to the Adventures of Dillon. First we need you to pick a class.')
print('The classes are Berserk: Where you get a sword that does 30 damage, 5 speed, and an ability that lets you deal 2x damage for 3 turns.')
print('Mage: Where you get a staff that does 25 damage, 10 speed, and an ability that lets you set the enemy on fire, dealing 5 damage until either them or you are dead.')
print('Rogue: Where you get a dagger that does 15 damage, 45 speed, and an ability that lets you dodge the enemy attacks')
print('Archer: Where you get a bow that does 20 damage, 8 speed, and an ability that lets you shot 2 arrows at once with your bow fully charged back')
print("The speed gives a chance for a double attack for all of the classes except rogue does a triple attack")

while choseClass == False:
    classInt = int(input('So what will it be. 1 for Berserk, 2 for Mage, 3 for rogue, or 4 for archer '))
    if classInt == 1:
        player = playa.player("Berserk", "GO BERSERK", 5, 30, sword, 160)
        choseClass = True
    elif classInt == 2:
        player = playa.player("Mage", "Fire", 10, 25, staff, 150)
        choseClass = True
    elif classInt == 3:
        player = playa.player("Rogue", "Avoid Attack", 45, 15, dagger, 125)
        choseClass = True
    elif classInt == 4:
        player = playa.player("Archer", "double shot at full charge", 5, 20, bow, 165)
        choseClass = True
    else:
        print("That is not an option.")

print("You encounter your first boss. You can click: \n1 to attack,\n2 to block, \n3 to use an item, \n4 to attempt to run.")
enemy1 = bigboypants.enemy1("Eldredge Dragon", 10, 300)

while not answer1:
    while not answer2:
        answer = int(input('What shall you do? '))
        if answer == 1:
            enemy1.health = player.attackMath(enemy1.health, specialAttack)
            answer2 = True
        elif answer == 2:
            answer2 = True 
        elif answer == 3:
            answer2 = True
        elif answer == 4:
            print('You failed to run and lost your turn.')
            answer2 = True
        else:   
            print('This is not an option')
    if enemy1.health <= 0:
        answer1 = True
        break
    
    if player.specialMove(enemy1.health, specialAttack) == 0:
        player.health = enemy1.enemyAttack(player.health)
        
    if player.health <= 0:
        answer1 = True
    else:
        answer2 = False
    

