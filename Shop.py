from Character import Character
from UI import UI

class Shop:

    def open(self, character: Character):
        res = UI.shop_menu()
        if res == "a" or res == "A":
            if character.coins >= 3:
                character.coins -= 3
                character.has_potions = True
                print("Thank you for your purchase!")
            else:
                print("You do not have enough coins.")
