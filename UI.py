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
        while not (res == "a" or res == "A" or res == "b" or res == "B" or res == "c" or res == "C" or res == "d" or res == "D"):
            print("\n\n\nPlease choose from the following options:\n")
            print("a - Fight next enemy")
            print("b - Go to shop")
            print("c - Check your character")
            print("d - Exit game")
            res = input("?: ")
        return res

    @staticmethod
    def get_name():
        name = input("\nPlease name your character: ")
        name = name.upper()
        print("\nHello " + name + "!")
        return name

    @staticmethod
    def character_details(character: Character):
        print("\nYour health is {}".format(character.health))

    @staticmethod
    def game_over():
        print("\nGAME OVER")
        print("Created by Jonathon Krohn :) and maybe Samuel Krohn")

    # endregion
    #####################################################
    # region Fight Class

    @staticmethod
    def fight_menu():
        res = ""

        while not (res == "a" or res == "A" or res == "b" or res == "B" or res == "c" or res == "C"):
            print("\n\n\nPlease choose from the following options:\n")
            print("a - Attack")
            print("b - Use Potion")
            print("c - Check Health")
            res = input("?: ")
        return res

    @staticmethod
    def attack():
        print("\nYou swing your sword!")

    @staticmethod
    def drink_potion():
        print("\nYou drink a potion!")

    @staticmethod
    def no_potion():
        print("\nYou do not own a potion, silly goose!")

    @staticmethod
    def display_fight_stats(character: Character, enemy: Enemy):
        print("\nYour health is {} and their health is {}".format(character.health, enemy.health))

    @staticmethod
    def you_are_dead():
        print("\nWow, that's rough. You died.")

    @staticmethod
    def you_killed_enemy():
        print("\nYour foe has fallen, YOU WIN!")

    # endregion
    #####################################################
    # region Shop Class

    @staticmethod
    def shop_menu():
        res = ""

        while not (res == "a" or res == "A" or res == "b" or res == "B"):
            print("\n\n\nWould you like to purchase a health potion? (50 HP)\n")
            print("a - YES (3 coins)")
            print("b - NO")
            res = input("?: ")
        return res


    # endregion
    #####################################################