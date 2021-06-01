from Character import Character
from Enemy import Enemy


class Fight:

    def __init__(self, character: Character, enemy: Enemy):


    def attack(self, character: Character, enemy: Enemy):
        print("You swing your sword!")
        character.health -= enemy.attack
        enemy.health -= character.attack

    def fight(self):
        fighting = True
        while fighting:
