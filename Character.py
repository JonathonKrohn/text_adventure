from Person import Person


class Character(Person):

    def __init__(self, name: str, health: int, exp: int, coins: int, attack: int, has_potion: bool):
        super().__init__(name, health, exp, coins, attack)
        self.has_potion = has_potion

    def drink_potion(self):
        self.health += 50
        self.has_potion = False
