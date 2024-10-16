class Person:
    def __init__(self, name, hp, mp, atk, df, speed, mgk_atk, mgk_def, items, spells, descri,):
        self.name = name
        self.hp = hp
        self.maxhp = hp
        self.mp = mp
        self.maxmp = mp
        self.atk = atk
        self.df = df
        self.speed = speed
        self.mgk_atk = mgk_atk
        self.mgk_def = mgk_def
        self.items = items
        self.spells = spells
        self.descri = descri


    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def attacks(self, target):
        dmg = self.atk - target.df
        if dmg < 0:
            dmg = 0
            print(f"{self.name} attacks, but {target.name} dodged the attack before it lands.")
        elif target.hp - dmg < 0:
            target.hp = 0
            print(f"{self.name} kills {target.name}")
        else:
            target.hp -= dmg
            print(f"{self.name} attacks {target.name} for {dmg} points of damage\n")

    def cast_magic(self, target, magic):
        if self.mp < magic.mp:
            print("You don't have enough mana points!")
            return

        self.mp -= magic.mp
        dmg = self.mgk_atk - target.mgk_def + magic.dmg
        if dmg < 0:
            dmg = 0
        target.hp -= dmg
        print(f"{self.name} casts [spell name] on {target.name} dealing {dmg} points of {magic.dmg_type} damage\n")

    def white_spell(self, target, magic):
        heal = 0
        if self.mp < magic.mp:
            print("You don't have enough mana points!\n")
            return

        self.mp = self.mp - magic.mp
        if target.hp == target.maxhp:
            target.hp = self.maxhp
        else:
            heal += (magic.heal + (self.mgk_atk/2))
            target.hp += heal
            print(f"{self.name} healed {target.name} for {magic.heal} hit points\n")

    def green_spell(self, target, magic):
        if self.mp < magic.mp:
            print("You don't have enough mana points!\n")
            return

        self.mp = self.mp - magic.mp
        if magic.name == "Protect":
            target.df += 10  # Raise defense
            print(f"{self.name} casts {magic.name} on {target.name}, increasing defense by 10!\n")

        elif magic.name == "Shell":
            target.mgk_def += 10  # Raise magical defense
            print(f"{self.name} casts {magic.name} on {target.name}, increasing magic defense by 10!\n")

        elif magic.name == "Speed":
            target.speed += 5  # Raise speed
            print(f"{self.name} casts {magic.name} on {target.name}, increasing speed by 10!\n")

    def blue_spell(self, target, magic):
        if self.mp < magic.mp:
            print("You don't have enough mana points!\n")

        self.mp = self.mp - magic.mp

        if magic.name == "Holy":
            target.hp -= (magic.dmg + (self.mgk_atk/2))
            print(f"{self.name} casts {magic.name} on {target.name}, dealing  by 10!\n")


    def __str__(self):
        return (f"Name: {self.name}"
                f"\nHealth: {self.hp}"
                f"\tAtk: {self.atk}"
                f"\tDef: {self.df}"
                f"\nMP: {self.mp}"
                f"\tMagic Attack: {self.mgk_atk}"
                f"\tMagic Defence: {self.mgk_def}"
                f"\nItems: {self.items}"
                f"\nSpells: {self.spells}")