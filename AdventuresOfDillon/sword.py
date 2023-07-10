class Sword: 
    def __init__(self, damage, type, rarity, name, durability):
        self.damage = damage
        self.type = type
        self.rarity = rarity
        self.name = name
        self.durability = durability


    def info(self):
        return f"Sword: {self.name}, Damage: {self.damage}, Type: {self.type}"