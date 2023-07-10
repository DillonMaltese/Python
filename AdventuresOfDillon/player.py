class player:
    def __init__(self, Class, ability, speed, damage, weapon, health):
        self.Class = Class
        self.ability = ability
        self.speed = speed
        self.damage = damage
        self.weapon = weapon
        self.health = health


    def __str__(self):
        return f"Class: {self.Class}, Ability: {self.ability}, Speed: {self.speed}, Rarity: {self.rarity}, Durability: {self.durability}"