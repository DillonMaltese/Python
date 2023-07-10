class Sword: 
    def __init__(self, name, damage, type, rarity, durability):
        self.damage = damage
        self.type = type
        self.rarity = rarity
        self.name = name
        self.durability = durability


    def __str__(self):
        return f"Sword: {self.name}, Damage: {self.damage}, Type: {self.type}, Rarity: {self.rarity}, Durability: {self.durability}"