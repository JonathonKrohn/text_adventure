from Person import Person


class Enemy(Person):

    def __init__(self, name: str, health: int, exp: int, coins: int, attack: int):
        super().__init__(name, health, exp, coins, attack)
