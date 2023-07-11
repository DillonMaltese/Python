class weapon:
    def __init__(weapon, name, type, damage, durability):
        weapon.name = name
        weapon.type = type
        weapon.damage = damage
        weapon.durability = durability


    def __str__(weapon):
        return f"Name: {weapon.name}, Type: {weapon.type}, Damage: {weapon.damage}, Durability: {weapon.durability}"