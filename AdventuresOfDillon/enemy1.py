from random import randint

class enemy1:
    def __init__(enemy, name, damage, health):
        enemy.name = name
        enemy.damage = damage
        enemy.health = health

    def __str__(enemy):
        return f"Name: {enemy.name}, Damage: {enemy.damage}, Health: {enemy.health}"
        
    def enemyAttack(enemy, playerHealth):
        #Enemy has normal + super attack (Has chance to one shot player)
        specialAttack = 100
        normalAttack = 30
        specialAttackPerc = randint(1, 100)
        print("Enemy Special Attack Number:", specialAttackPerc)
        if specialAttackPerc <= 7:
            #Special Attack happens
            print("You were hit by the enemy's special attack for", specialAttack, "damage")
            playerHealth-=specialAttack
    
        else:
            #Normal attack happens
            print("You were hit by the enemy's attack for", normalAttack, "damage")
            playerHealth-=normalAttack
        
        if playerHealth <= 0:
            print("You were killed. GG")
            playerHealth = 0

        else:
            print("You are at", playerHealth, "health")

        return playerHealth