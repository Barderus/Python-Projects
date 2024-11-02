import random
from Colors import bcolors

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
        critical_chance = 0.2  # 20% chance for a critical hit
        critical_multiplier = 2  # Critical hits deal double damage

        # Define attack damage range
        min_attack = self.atk // 2  # Minimum attack damage
        max_attack = self.atk  # Maximum attack damage

        # Generate random damage within the specified range
        dmg = random.randint(min_attack, max_attack) - target.df

        # Determine if a critical hit occurs
        is_critical = random.random() < critical_chance
        if is_critical:
            dmg *= critical_multiplier
            print(bcolors.BOLD + bcolors.RED+ "\nCritical hit! " + bcolors.ENDC)

        miss_messages = [
            "{target} swiftly evades {attacker}'s attack!",
            "{attacker} strikes, but {target} nimbly dodges!",
            "{target} deflects the blow with a perfect parry!",
            "{attacker}'s attack is met with a quick parry from {target}!",
            "{target} braces, absorbing {attacker}'s strike!",
            "{attacker}'s attack lands, but {target} blocks it with a solid defense!"
        ]
        if dmg < 0:
            message = random.choice(miss_messages).format(attacker=self.name, target=target.name)
            print(message)
        elif target.hp - dmg <= 0:
            target.hp = 0

            kill_messages = [
                "{attacker} lands a devastating strike, finishing off {target}!",
                "{target} falls as {attacker} delivers the final blow!",
                "{attacker} defeats {target} with a powerful attack!",
                "With a fierce attack, {attacker} vanquishes {target}!",
                "{attacker}'s strike overwhelms {target}, leaving them defeated!"
            ]

            message = random.choice(kill_messages).format(attacker=self.name, target=target.name)
            print(f"{bcolors.BOLD}{message}{bcolors.ENDC}")

        else:
            target.hp -= dmg
            print(f"{self.name} attacks {target.name} for {dmg} points of damage\n")


    def cast_magic(self, target, magic):
        magic.apply(caster=self, target=target)

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
