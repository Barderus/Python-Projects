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

    def damage(self, target):
        dmg = self.atk - target.df
        if dmg < 0:
            dmg = 0
        target.health -= dmg
        print(f"{self.name} attacks {target.name} for {dmg} points of damage")

    def cast_magic(self, target, magic):
        mp_cost = self.mp - magic.mp
        dmg = self.mgk_atk - target.mgk_def
        if dmg < 0:
            dmg = 0
        target.health -= dmg
        print(f"{self.name} casts [spell name] on {target.name} dealing {dmg} points of damage")

    def cast_heal(self, target, magic):
        mp_cost = self.mp - magic.mp
        target.health += magic.heal
        print(f"{self.name} healed {target.name} for {magic.heal} health points")

    def choose_magic(self):
        pass

    def choose_item(self):
        pass

    def choose_target(self):
        pass

    def get_stats(self):
        pass