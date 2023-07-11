class enemy:
        def __init__(enemy, name, damage, health):
            enemy.name = name
            enemy.damage = damage
            enemy.health = health

        def __str__(enemy):
            return f"Name: {enemy.name}, Damage: {enemy.damage}, Health: {enemy.health}"