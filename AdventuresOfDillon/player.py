from random import randint

class player:
    def __init__(self, Class, ability, speed, damage, weapon, health):
        self.Class = Class
        self.ability = ability
        self.speed = speed
        self.damage = damage
        self.weapon = weapon
        self.health = health


    def __str__(self):
        return f"Class: {self.Class}, Ability: {self.ability}, Speed: {self.speed}, Damage: {self.damage}, Weapon: {self.weapon}, Health: {self.health}"
    
    def attackMath(self, enemy1Health, specialAttack):
    #Double attack = Speed x 2
    #Special attack = 35 without double attack happening
    #Special attack = 20 with double attack happening
    #sPA = Special Attack
    #sPAWD = Special Attack with Double Attack
        doubleAttackAns = randint(1, 100)
        specialAttackAns = randint(1, 100)
        doubleAttackPerc = self.speed*2
        sPAWD = 20
        sPA = 35
        if doubleAttackAns <= doubleAttackPerc:
            #Double attack happens
            if specialAttackAns <= sPAWD:
                #Double attack + special attack happens
                if self.Class == "Berserk":
                    damage = self.damage*4
                    print("You went Berserk and hit the enemy for 2x damage with a double attack too. This hit him for", damage, "and you will also hit him for 2x damage for the next 2 turns")
                    enemy1Health -= damage
                    print("The enemy is at", enemy1Health, "health")
                elif self.Class == "Mage":
                    damage = self.damage*2
                    print("You used your set fire ability and double attack in the same move. This hit him for", damage, "and now he will take 5 damage every turn because you set him on fire")
                    enemy1Health -= damage
                    print("The enemy is at", enemy1Health, "health")
                elif self.Class == "Rogue":
                    damage = self.damage*3
                    print("You used your triple attack and your special dodge move in the same turn. This hit him for", damage, "you will now dodge his next turn")
                    enemy1Health -= damage
                    print("The enemy is at", enemy1Health, "health")
                elif self.Class == "Archer":
                    damage = self.damage*3
                    print("You used your double attack and special move to freely full charge back. This hit the enemy for", damage)
                    enemy1Health -= damage
                    print("The enemy is at", enemy1Health)

            else:
                #Just double attack happens
                damage = self.damage*2


        else:
            #No double attack
            if specialAttackAns <= sPA:
                #Special attack happens
                if self.Class == "Berserk":
                    damage = self.damage*2
                    print("You went Berserk and hit the enemy for 2x damage. This hit him for", damage, "and you will also hit him for 2x damage for the next 2 turns")
                    enemy1Health -= damage
                    print("The enemy is at", enemy1Health, "health")
                elif self.Class == "Mage":
                    damage = self.damage
                    print("You used your set fire ability. This hit him for", damage, "and now he will take 5 damage every turn because you set him on fire")
                    enemy1Health -= damage
                    print("The enemy is at", enemy1Health, "health")
                elif self.Class == "Rogue":
                    damage = self.damage
                    print("You used your special dodge move. This hit him for", damage, "you will now dodge his next turn")
                    enemy1Health -= damage
                    print("The enemy is at", enemy1Health, "health")
                elif self.Class == "Archer":
                    damage = self.damage*1.5
                    print("You used your special move to freely full charge back. This hit the enemy for", damage)
                    enemy1Health -= damage
                    print("The enemy is at", enemy1Health)

            else:
                #Normal attack happens
                damage = self.damage
