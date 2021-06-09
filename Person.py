class Person:
    def __init__(self, name: str, health: int, exp: int, coins: int, attack: int):


        self.name = name
        self.health = health
        self.exp = exp
        self.coins = coins
        self.attack = attack

    def is_dead(self):
        if self.health <= 0:
            return True
        else:
            return False
