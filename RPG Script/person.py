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
            print(f"{self.name} attacks, but {target.name} dodged the attack before it lands.")
        elif target.hp - dmg < 0:
            target.hp = 0
            print(f"{self.name} kills {target.name}")
        else:
            target.hp -= dmg
            print(f"{self.name} attacks {target.name} for {dmg} points of damage\n")

    def cast_magic(self, target, magic):
        """
            This function selects which method to call to cast the spell
        """
        if magic.school == "black":
            self.black_spell(target, magic)
        elif magic.school == "white":
            self.white_spell(target, magic)
        elif magic.school == "blue":
            self.blue_spell(target, magic)
        elif magic.school == "green":
            self.green_spell(target, magic)


    def black_spell(self, target, magic):
        if magic.name == "Fire":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Thunder":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Blizzard":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Meteor":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Quake":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Tornado":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Ultima":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Dark":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Bio":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Drain":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

    def white_spell(self, target, magic):
        if magic.name == "Cure":
            self.check_mp(magic)
            self.magic_heal(target, magic)

        elif magic.name == "Cura":
            self.check_mp(magic)
            self.magic_heal(target, magic)

        elif magic.name == "Curaga":
            self.check_mp(magic)
            self.magic_heal(target, magic)

        elif magic.name == "Revive":
            self.check_mp(magic)
            self.magic_revive(target)

    def green_spell(self, target, magic):
        if magic.name == "Protect":
            self.check_mp(magic)

            target.df += 10  # Raise defense
            print(f"{self.name} casts {magic.name} on {target.name}, increasing defense by 10!\n")

        elif magic.name == "Shell":
            self.check_mp(magic)

            target.mgk_def += 10  # Raise magical defense
            print(f"{self.name} casts {magic.name} on {target.name}, increasing magic defense by 10!\n")

        elif magic.name == "Speed":
            self.check_mp(magic)

            target.speed += 5  # Raise speed
            print(f"{self.name} casts {magic.name} on {target.name}, increasing speed by 10!\n")

    def blue_spell(self, target, magic):

        if magic.name == "Holy":
            self.check_mp(magic)
            self.magic_dmg(target, magic)

        elif magic.name == "Flare":
            self.check_mp(magic)
            self.magic_dmg(target, magic)
        else:
            print("Something wrong has happened")

    def check_mp(self, magic):
        if self.mp <= 0:
            print("You have no mana points left!\n")
            return False
        elif self.mp < magic.mp:
            print(f"{self.name} tries to access the source of magic, but it has been depleted. {self.name} is stunned.\n")
            return False

        self.mp -= magic.mp
        return True

    def magic_heal(self, target, magic):
        # Calculate healing amount
        heal = magic.heal + (self.mgk_atk / 2)

        # Check if the target is already at full health
        if target.hp >= target.maxhp:
            print(f"{self.name} attempted to heal {target.name}, but {target.name} is already at full HP!")
            return

        # Heal the target
        target.hp += heal

        # Ensure the target's HP does not exceed maximum HP
        if target.hp > target.maxhp:
            target.hp = target.maxhp
        print(f"{self.name} healed {target.name} for {int(heal)} hit points. {target.name}'s current HP: {int(target.hp)}/{target.maxhp}")

    def magic_revive(self, target):
        if target.hp == 0:
            target.hp = (self.maxhp * 0.5)
        print(f"{self.name} revived {target.name}.")

    def magic_dmg(self, target, magic):
        dmg =  (magic.dmg + (self.mgk_atk / 2)) - target.mgk_def
        if dmg == 0:
            print(f"{target.name} dodges your spell, taking no damage.")
        elif target.hp - dmg < 0:
            target.hp = 0
            print(f"{self.name} pulverizes {target.name} after casting {magic.name}")
        else:
            target.hp -= dmg
            print(f"{self.name} casts {magic.name} on {target.name}, dealing {int(dmg)} points of {magic.dmg_type} damage\n")


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
