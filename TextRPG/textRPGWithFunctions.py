#Start menu (1 for start 2 for options etc)
#Inventory Sorting in array (Each item has different value/attributes (Common, Rare, etc))
#Enemy has health + same type of enemy has different stats/attributes
from random import randint
import attackMath as a
global Class, chose, pHP, eHP, mainWeaponDamage, mainWeaponName, mainWeaponSpeed, doubleAttackPerc, specialAttackPerc, enemyAlive, doubleAttackAns, specialAttack, hp
Class = ''
chose = False
pHP = 0
eHP = 0
mainWeaponName = ''
mainWeaponDamage = 1
mainWeaponSpeed = 0
doubleAttackPerc = 0
specialAttackPerc = 25
specialAttack = False
endDamage = 0

enemyAlive = True
doubleAttackAns = 0


def Main(chose, mainWeaponDamage, mainWeaponName, mainWeaponSpeed, pHP, eHP, doubleAttackPerc, enemyAlive, Class, doubleAttackAns, specialAttack):
  
  pickClass(chose, pHP, mainWeaponName, mainWeaponDamage, mainWeaponSpeed)
  doubleAttackPerc = mainWeaponSpeed*2
  Enemy1(eHP, pHP, mainWeaponSpeed, mainWeaponName, mainWeaponDamage, doubleAttackPerc, enemyAlive, Class, doubleAttackAns, specialAttack)

def pickClass(chose, hp, mainWeaponName, mainWeaponDamage, mainWeaponSpeed):
  #Berserk = 200hp
  #Mage = 150hp
  #Rogue = 125hp
  #Archer = 165hp
  while chose == False:
    classInt = int(input('Do you want to start as a berserk, mage, rogue, or archer\nClick 1 for berserk, 2 for mage, 3 for rogue or 4 for archer '))
    if classInt == 1: 
      #Ability to go berserk (Doubles attack for next 3)
      Class = 'b'
      hp = 200 
      mainWeaponName = 'Starter Sword'
      mainWeaponDamage = 30
      mainWeaponSpeed = 3
      chose = True
    elif classInt == 2: 
      #Has chance to set fire damage (Ticks for 5 damage on enemy until they or the player is dead)
      Class = 'm'
      hp = 150
      mainWeaponName = 'Starter Staff'
      mainWeaponDamage = 25
      mainWeaponSpeed = 10
      chose = True
    elif classInt == 3: 
      #Has chance to avoid next attack
      Class = 'r'
      mainWeaponName = 'Starter Dagger'
      mainWeaponDamage = 15
      mainWeaponSpeed = 45
      hp = 125
      chose = True
    elif classInt == 4: 
      #Has chance to shoot 2 arrows at once
      Class = 'a'
      mainWeaponName = 'Starter Bow'
      mainWeaponDamage = 20
      mainWeaponSpeed = 5
      hp = 165
    else: print("That option is not allowed")

    return mainWeaponSpeed, mainWeaponName, mainWeaponDamage, Class, hp

def Enemy1(eHP, pHP, mainWeaponSpeed, mainWeaponName, mainWeaponDamage, doubleAttackPerc, enemyAlive, Class, doubleAttackAns, specialAttack):
    #First enemy = 300hp
    #Player can attack, run, block, use item
    eHP = 300
    print('You encounter your first enemy. He has', eHP, 'and you have', pHP, 'What shall you do?')
    while enemyAlive:
      answer = int(input("Press 1 to attack\nPress 2 to block\nPress 3 to use an item \nPress 4 to attempt to run "))
      if answer == 1: 
        #Go to attack Menu
        print('First in text', mainWeaponDamage)
        eHP, mainWeaponDamage = a.attack(doubleAttackPerc, mainWeaponDamage, eHP, Class, specialAttackPerc, specialAttack)
        print('Second in text', mainWeaponDamage)

      elif answer == 2:
        #Go to block Menu
        print('Block')

      elif answer == 3:
        #Go to item Menu
        print('Item')

      elif answer == 4:
        #Trying to run
        print("You can't run from this battle and lost your turn")

      else:
        print('This is not an option, you lost your turn')

        return eHP, pHP, mainWeaponDamage, mainWeaponName, mainWeaponSpeed, doubleAttackPerc, doubleAttackAns, specialAttack, specialAttack, Class



    



Main(chose, mainWeaponDamage, mainWeaponName, mainWeaponSpeed, pHP, eHP, doubleAttackPerc, enemyAlive, Class, doubleAttackAns, specialAttack)
