class weapon:
    def __init__(weapon, type, damage):
        weapon.type = type
        weapon.damage = damage


    def __str__(weapon):
        return f"Type: {weapon.type}, Damage: {weapon.damage}"