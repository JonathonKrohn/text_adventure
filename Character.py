from Person import Person


class Character(Person):

    def __init__(self, name: str, health: int, exp: int, coins: int, attack: int, potion: bool):
        super().__init__(name, health, exp, coins, attack)
        self.potion = potion
