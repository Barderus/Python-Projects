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
            print(f"\t\t{bcolors.YELLOW}{bcolors.BOLD}{caster.name} doesn't have enough MP to cast {self.name}. {caster.name} is stunned.{bcolors.ENDC}")
            return False
        caster.mp -= self.mp
        return True

    def apply(self, caster, target):
        if not self.check_mp(caster):
            return

        if self.effect_type == "damage":

            # Define critical hit parameters
            critical_chance = 0.2  # 20% chance for a critical hit
            critical_multiplier = 2  # Critical hits deal double damage

            magic_dmg = (caster.mgk_atk + self.dmg) - target.mgk_def
            # Determine if a critical hit occurs
            is_critical = random.random() < critical_chance
            if is_critical:
                magic_dmg *= critical_multiplier  # Apply critical damage multiplier
                print(bcolors.BOLD + bcolors.BLUE + "Arcane Surge! " + bcolors.ENDC)

            dodge_messages = [
                f"{target.name} swiftly dodges the attack!",
                f"{target.name} anticipates and avoids the magic!",
                f"{target.name} parries, nullifying the spell's effect!",
                f"{target.name} deflects the spell in a burst of light!"
            ]
            kill_messages = [
                f"{caster.name}'s magic {bcolors.RED}{bcolors.BOLD}obliterates{bcolors.ENDC} {target.name}!",
                f"{target.name} is {bcolors.RED}{bcolors.BOLD}consumed{bcolors.ENDC} by {caster.name}'s powerful spell!",
                f"{caster.name}'s magic overwhelms {target.name}, leaving {bcolors.RED}{bcolors.BOLD}no chance{bcolors.ENDC} for survival!",
                f"{caster.name} casts a {bcolors.RED}{bcolors.BOLD}fatal blow{bcolors.ENDC}, ending {target.name}!"
            ]

            # If magic is dodged or blocked
            if magic_dmg <= 0:
                print(random.choice(dodge_messages))
                return

            # Check for Drain spell
            if self.name == "Drain":
                target.hp = max(0, target.hp - magic_dmg)
                recovery = magic_dmg * 0.25
                caster.hp += recovery
                print(
                    f"{caster.name} casts {self.name} on {target.name}, dealing {int(magic_dmg)} damage. {caster.name} recovers {int(recovery)} HP.")
                return

            # Update target's HP and ensure it doesn't go below zero
            target.hp = max(0, target.hp - magic_dmg)

            # Check if target was defeated
            if target.hp == 0:
                print(f"{caster.name} casts {self.name} on {target.name} dealing {bcolors.RED}{bcolors.BOLD}{magic_dmg}{bcolors.ENDC} points of damage")
                print(random.choice(kill_messages))
            else:
                print(f"{caster.name} casts {self.name} on {target.name}, dealing {bcolors.RED}{bcolors.BOLD}{int(magic_dmg)}{bcolors.ENDC} damage.")

        elif self.effect_type == "healing":
            heal = self.heal + (caster.mgk_atk / 2)
            target.hp = min(target.maxhp, target.hp + heal)
            print(f"{caster.name} heals {target.name} for {bcolors.GREEN}{bcolors.BOLD}{int(heal)}{bcolors.ENDC} HP.")

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
