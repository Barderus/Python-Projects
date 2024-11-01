import random
from Colors import bcolors

class Magic:
    def __init__(self, name, school, mp, dmg=0, heal=0, effect_type="damage", description=""):
        self.name = name
        self.school = school
        self.mp = mp
        self.dmg = dmg
        self.heal = heal
        self.effect_type = effect_type
        self.descri = description

    def check_mp(self, caster):
        if caster.mp < self.mp:
            print(f"{caster.name} doesn't have enough MP to cast {self.name}. {caster.name} is stunned.")
            return False
        caster.mp -= self.mp
        return True

    def apply(self, caster, target):
        if not self.check_mp(caster):
            return

        if self.effect_type == "damage":
            # Define critical hit parameters
            critical_chance = 0.25  # 25% chance for a critical hit
            critical_multiplier = 2  # Critical hits deal double damage

            magic_dmg = (caster.mgk_atk + self.dmg) - target.mgk_def
            # Determine if a critical hit occurs
            is_critical = random.random() < critical_chance
            if is_critical:
                magic_dmg *= critical_multiplier  # Apply critical damage multiplier
                print("Critical hit! ")

            if self.name == "Drain":
                target.hp = max(0, target.hp - magic_dmg)
                recovery = magic_dmg * 0.25
                caster.hp += recovery
                print(f"{caster.name} casts {self.name} on {target.name}, dealing {int(magic_dmg)} damage.{caster.name} recovers {int(recovery)} HP.")
                return

            # Update target's HP and ensure it doesn't go below zero
            target.hp = max(0, target.hp - magic_dmg)
            print(f"{caster.name} casts {self.name} on {target.name}, dealing {int(magic_dmg)} damage.")

        elif self.effect_type == "healing":
            heal = self.heal + (caster.mgk_atk / 2)
            target.hp = min(target.maxhp, target.hp + heal)
            print(f"{caster.name} heals {target.name} for {int(heal)} HP.")

        elif self.effect_type == "buff":
            if self.name == "Protect":
                target.df += 10
            elif self.name == "Shell":
                target.mgk_def += 10
            elif self.name == "Speed":
                target.speed += 5
            print(f"{caster.name} casts {self.name}, buffing {target.name}.")

        elif self.effect_type == "revive" and target.hp == 0:
            target.hp = target.maxhp * 0.5
            print(f"{caster.name} revives {target.name}.")

def __str__(self):
    return (f"Name: {self.name}"
            f"\nDamage: {self.dmg}\tMP: {self.mp}"
            f"Description: {self.descri}")
