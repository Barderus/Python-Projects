from inventory import Inventory

class Items:
    def __init__(self, name, effect, quantity, description):
        self.name = name
        self.effect = effect
        self.quantity = quantity
        self.description = description
        self.inventory = []

    def use_item(self, item, target):
        if not Inventory.check_item(item):
            return

        if self.effect == "healing":
            match self.name:
                case "Healing Potion":
                    target.hp += 100
                case "HI-Potion":
                    target.hp += 250
                case "Ether":
                    target.mp += 50
                case "HI-Ether":
                    target.mp += 100
                case "Elixir":
                    target.hp += 200
                    target.mp += 50
                case "HI-Elixir":
                    target.hp = target.maxhp
                    target.mp = target.maxmp
                case "Phoenix Down":
                    if target.hp > 0:
                        print(f"{target.name} isn't dead.")
                    else:
                        target.hp = target.maxhp * 0.1
                        print(f"{target.name} is back on their feet.")
                case _:
                    print("This item has no effect.")
        elif self.effect == "buff":
            match self.name:
                case "Hermes Shoes":
                    target.speed += 10
                case "Red Fang":
                    target.atk += 10
                case "Protect Coat":
                    target.df += 10
                case "Faerie Bless":
                    target.mgk_atk += 10
                case "Witch's Hat":
                    target.mgk_def += 10
                case _:
                    print("This item has no effect.")
        elif self.effect == "debuff":
            match self.name:
                case "Slug Bomb":
                    target.atk -= 10
                case "Acid":
                    target.df -= 10
                case "Spider Silk":
                    target.speed -= 10
                case "Moonstone":
                    target.mgk_atk -= 10
                case "Dragon Spit":
                    target.mgk_def -= 10
                case _:
                    print("This item has no effect.")
        else:
            print("You got cursed. You are stunned.")

    def __str__(self):
        return f"{self.name} : {self.description}"
