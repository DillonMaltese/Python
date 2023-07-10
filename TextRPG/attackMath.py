#When importing it into TextRPG file, won't run whole file
from random import randint

if __name__ == "__main__":

    
    def attack(doubleAttackPerc, doubleAttack, mainWeaponDamage, eHP, pHP, Class, specialAttackPerc):
        doubleAttackAns = randint(1, 100)
        specialAttackAns = randint(1, 100)
        if doubleAttackAns <= doubleAttackPerc:
            #Special attack goes down to 15
            if specialAttackAns <= specialAttackPerc-10:
                print('Not only did you hit for your double attack, you also hit for your special attack')
                if Class == 'b':
                    print('You did', mainWeaponDamage*4, 'damage and will now do 2x damage for the next 2 turns')
                    eHP = eHP - mainWeaponDamage*4
                elif Class == 'm':
                    print('You did', mainWeaponDamage*2, 'damage and will now do 5 damage at the end of every turn because you set the enemy on fire')
                    eHP = eHP - mainWeaponDamage*2
                elif Class == 'r':
                    print('You did', mainWeaponDamage*2, "damage and avoided the enemy's next attack")
                    eHP = eHP - mainWeaponDamage*2
                else:
                    print('You did', mainWeaponDamage*8, 'damage because you shot 2 arrows at once and freely fully charged back')
                    eHP = eHP - mainWeaponDamage*8

            else:
                print('Double Attack has been inflicted for', mainWeaponDamage*2, 'damage')
                eHP = eHP - mainWeaponDamage*2



        else:
            #Special Attack stays at 25
            if specialAttackAns <= specialAttackPerc-10:
                if Class == 'b':
                    print('You did', mainWeaponDamage*2, 'damage and will now do 2x damage for the next 2 turns')
                    eHP = eHP - mainWeaponDamage*2
                elif Class == 'm':
                    print('You did', mainWeaponDamage, 'damage amd will now do 5 damage at the end of every turn because you set the enemy on fire')
                    eHP = eHP - mainWeaponDamage
                elif Class == 'r':
                    print('You did', mainWeaponDamage, "damage and avoided the enemy's next attack")
                    eHP = eHP - mainWeaponDamage
                else:
                    print('You did', mainWeaponDamage*4, 'damage because you shot 2 arrows at once and freely fully charged back')
                    eHP = eHP - mainWeaponDamage*4

            else:
                print('You hit the enemy for', mainWeaponDamage, 'damage')
                eHP = eHP - mainWeaponDamage

            