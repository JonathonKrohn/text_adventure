import random
from Character import Character
from Enemy import Enemy
from Fight import Fight
from UI import UI
from Shop import Shop


class Game:
    names = ["Joe Schmoe", "Wooly Willie", "Billy Bob", "Bowser Shmowser", "Missi Krissi", "Captain Obvious", "Hook-hand Dan"]

    def __init__(self):
        # UI
        name = UI.get_name()
        # character
        self.character = Character(name, 100, 100, 100, 10, True)
        # enemy
        self.enemy = Enemy(
            random.choice(self.names),
            30,
            0,
            0,
            10,
        )
        self.shop = Shop()
        self.level = 1

    def start(self):
        playing = True
        while playing:

            res = UI.display_menu()
            # Fight
            if res == "a" or res == "A":
                # Fight
                fight = Fight(self.character, self.enemy)
                fight.start()
                if self.character.is_dead():
                    UI.game_over()
                    playing = False
            # Shop
            elif res == "b" or res == "B":
                self.shop.open(self.character)
            # Check Player
            elif res == "c" or res == "C":
                UI.character_details(self.character)
            # Exit Game
            elif res == "d" or res == "D":
                playing = False
            else:
                print("error")
