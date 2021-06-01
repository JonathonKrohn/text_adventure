from Character import Character


class UI:
    def display_menu(self):
        res = ""

        while not (res == "a" or res == "A" or res == "b" or res == "B" or res == "c" or res == "C"):
            print("Please choose from the following options:\n")
            print("a - Fight next enemy")
            print("b - Go to shop")
            print("c - Exit game")
            res = input("?: ")
        return res

    def get_name(self):
        name = input("\nPlease name your character: ")
        name = name.upper()
        print("\nHello " + name + "!\n")
        return name

    def character_details(self, character: Character):
        print(character.health)