from inventory import Inventory
from Colors import bcolors



def check_hp(target, heal, mp_heal):
    if target.hp < 0:
        print(f"{target.name} has perished in battle. They can't be healed.")

    target.hp += heal
    target.mp += mp_heal

    if target.hp > target.maxhp:
        target.hp = target.maxhp
    if target.mp > target.maxmp:
        target.mp = target.maxmp


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
                heal = 100
                mp_heal = 0
                check_hp(target, heal, mp_heal)
            case "HI-Potion":
                heal = 250
                mp_heal = 0

                check_hp(target, heal, mp_heal)
            case "Ether":
                heal = 0
                mp_heal = 50
                check_hp(target, heal, mp_heal)

            case "HI-Ether":
                heal = 0
                mp_heal = 100
                check_hp(target, heal, mp_heal)

            case "Elixir":
                heal = 200
                mp_heal = 50
                check_hp(target, heal, mp_heal)

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
