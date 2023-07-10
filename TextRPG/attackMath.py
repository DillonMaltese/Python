#When importing it into TextRPG file, won't run whole file
from random import randint

if __name__ == "__main__":

    
    def doubleAttacks(doubleAttackPerc, doubleAttackAns, doubleAttack):
        doubleAttackAns = randint(1, 100)
        if doubleAttackAns <= doubleAttackPerc:
            print('Double Attack has been inflicted for ')

    def attack(mainWeaponDamage, doubleAttackPerc, doubleAttackAns, eHP, pHP):

