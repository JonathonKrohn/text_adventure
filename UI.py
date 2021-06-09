from Character import Character
from Enemy import Enemy


class UI:

    def __init__(self):
        pass

    #####################################################
    # region Game Class

    @staticmethod
    def display_menu():
        res = ""
        while not (res == "a" or res == "A" or res == "b" or res == "B" or res == "c" or res == "C"):
            print("Please choose from the following options:\n")
            print("a - Fight next enemy")
            print("b - Go to shop")
            print("c - Exit game")
            res = input("?: ")
        return res

    @staticmethod
    def get_name():
        name = input("\nPlease name your character: ")
        name = name.upper()
        print("\nHello " + name + "!\n")
        return name

    @staticmethod
    def character_details(character: Character):
        print("Your health is {}".format(character.health))

    @staticmethod
    def game_over():
        print("GAME OVER")
        print("Created by Jonathon Krohn :) and maybe Samuel Krohn")

    # endregion
    #####################################################
    # region Fight Class

    @staticmethod
    def fight_menu():
        res = ""

        while not (res == "a" or res == "A" or res == "b" or res == "B" or res == "c" or res == "c"):
            print("\nPlease choose from the following options:\n")
            print("a - Attack")
            print("b - Use Potion")
            print("c - Check Health")
            res = input("?: ")
        return res

    @staticmethod
    def attack():
        print("You swing your sword!")

    @staticmethod
    def drink_potion():
        print("You drink a potion!")

    @staticmethod
    def no_potion():
        print("You do not own a potion, silly goose!")

    @staticmethod
    def display_fight_stats(character: Character, enemy: Enemy):
        print("Your health is {} and their health is {}".format(character.health, enemy.health))

    @staticmethod
    def you_are_dead():
        print("Wow, that's rough. You died.")

    @staticmethod
    def you_killed_enemy():
        print("Your foe has fallen, YOU WIN!")

    # endregion
    #####################################################
