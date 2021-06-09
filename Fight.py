from Character import Character
from Enemy import Enemy
from UI import UI
import random


class Fight:

    def __init__(self, character: Character, enemy: Enemy):
        self.character = character
        self.enemy = enemy

    def attack(self):
        UI.attack()
        self.character.health -= self.enemy.attack
        self.enemy.health -= self.character.attack

    def heal(self):
        if self.character.has_potion:
            self.character.drink_potion()
            self.character.health -= self.enemy.attack
            UI.drink_potion()
        else:
            UI.no_potion()

    def start(self):
        fighting = True

        while fighting:
            response = UI.fight_menu()

            # Checks for user response
            if response == "a" or response == "A":
                self.attack()
            elif response == "b" or response == "B":
                self.heal()
            elif response == "c" or response == "C":
                UI.display_fight_stats(self.character, self.enemy)

            # Death check on player and enemy
            if self.character.is_dead():
                UI.you_are_dead()
                fighting = False
            elif self.enemy.is_dead():
                UI.you_killed_enemy()
                fighting = False





