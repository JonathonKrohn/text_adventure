from Character import Character
from Enemy import Enemy
from Fight import Fight
from UI import UI
import random


class Game:
    names = ["Joe Schmoe", "Wooly Willie", "Billy Bob"]

    def __init__(self):
        # UI
        name = UI.get_name()
        # character
        self.character = Character(name, 100, 0, 0, 10, False)
        # enemy
        self.enemy = Enemy(
            random.choice(self.names),
            30,
            0,
            0,
            10,
        )

    def start(self):
        playing = True
        while playing:

            res = UI.display_menu()
            if res == "a" or res == "A":
                # Fight
                fight = Fight(self.character, self.enemy)
                fight.start()

                # Test
                UI.character_details(self.character)
            elif res == "b" or res == "B":
                print("hi")
            elif res == "c" or res == "C":
                playing = False

            else:
                print("error")
