from Character import Character
from Enemy import Enemy
from UI import UI
import random


class Fight:

    def __init__(self, character: Character, enemy: Enemy):
        self.character = character
        self.enemy = enemy

    def attack(self):
        print("You swing your sword!")
        self.character.health -= self.enemy.attack
        self.enemy.health -= self.character.attack

    def heal(self):
        if self.character.has_potion:
            self.character.drink_potion()
            self.character.health -= self.enemy.attack

        else:
            print("You do not own a potion, silly goose!")

    def start(self):
        fighting = True

        while fighting:
            response = UI.fight_menu()

            if response == "a" or response == "A":
                self.attack()
            elif response == "b" or response == "B":
                self.heal()
            elif response == "c" or response == "C":
                UI.display_fight_stats(self.character, self.enemy)
            if self.character.is_dead():
                print("Wow, that's rough. You died.")
                fighting = False
            elif self.enemy.is_dead():
                print("Your foe has fallen, YOU WIN!")
                fighting = False





