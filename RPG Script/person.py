class Person:
    def __init__(self, name, health, mp, atk, df, mgk_atk, mgk_def, items, spells, descri):
        self.name = name
        self.health = health
        self.mp = mp
        self.atk = atk
        self.df = df
        self.mgk_atk = mgk_atk
        self.mgk_def = mgk_def
        self.items = items
        self.spells = spells
        self.descri = descri

    def attacks(self, target):
        if target.health <= 0:
            print("Enemy is already dead. Choose another adversary.")
        else:
            dmg = self.atk - target.df
            if dmg < 0:
                dmg = 0
            target.health -= dmg
            print(f"{self.name} attacks {target.name} for {dmg} points of damage")

    def cast_magic(self, target, magic):
        if magic.mp < self.mp:
            print("You don't have enough mana points!")
        else:
            self.mp = self.mp - magic.mp
            dmg = self.mgk_atk - target.mgk_def
            if dmg < 0:
                dmg = 0
            target.health -= dmg
            print(f"{self.name} casts [spell name] on {target.name} dealing {dmg} points of damage")

    def cast_heal(self, target, magic):
        if magic.mp < self.mp:
            print("You don't have enough mana points!")
        else:
            self.mp = self.mp - magic.mp
            target.health += magic.heal
            print(f"{self.name} healed {target.name} for {magic.heal} health points")

    def choose_magic(self):
        pass

    def choose_item(self):
        pass

    def choose_target(self):
        pass

    def __str__(self):
        return (f"Name: {self.name}"
                f"\nHealth: {self.health}"
                f"\tAtk: {self.atk}"
                f"\tDef: {self.df}"
                f"\nMP: {self.mp}"
                f"\tMagic Attack: {self.mgk_atk}"
                f"\tMagic Defence: {self.mgk_def}"
                f"\nItems: {self.items}"
                f"\nSpells: {self.spells}")