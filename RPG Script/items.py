from inventory import Inventory


class Items:
    def __init__(self, name, effect, quantity, description):
        self.name = name
        self.effect = effect
        self.quantity = quantity
        self.description = description

    def use_item(self, item, target):
        # Check if the item can be used (quantity check)
        if self.quantity <= 0:
            print(f"You have no {self.name} left to use.")
            return

        # Apply the effect of the item on the target
        if item.effect == "heal":
            item.apply_healing(item, target)
        elif item.effect == "buff":
            item.apply_buff(item, target)
        elif item.effect == "debuff":
            item.apply_debuff(item, target)
        else:
            print("Isn't working at all")

        # Decrease item quantity after usage
        item.quantity -= 1
        print(f"\n\tUsed {item.name}. Remaining: {item.quantity}")

    def apply_healing(self, item, target):
        match item.name:
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
                print("Some problem with healing.")

    def apply_buff(self, item, target):
        match item.name:
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
                print("Some problem with buffing")

    def apply_debuff(self,item, target):
        match item.name:
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
                print("Some problem with debuffing")

    def __str__(self):
        return f"\t\t{self.name} : {self.description} : x{self.quantity}"
