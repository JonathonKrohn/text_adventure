from Character import Character


class UI:
    def __init__(self):
        pass

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
    def fight_menu():
        res = ""

        while not (res == "a" or res == "A" or res == "b" or res == "B" or res == "c" or res == "c"):

            print("Please choose from the following options:\n")
            print("a - Attack")
            print("b - Use Potion")
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
        print("Your health is " + character.health)

    @staticmethod
    def game_over():
        print("GAME OVER")
        print("Created by Jonathon Krohn :) and maybe Samuel Krohn")

