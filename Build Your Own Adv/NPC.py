import random


class NPC:
    def __init__(self, hp, atk, mgk, df):
        self.hp = hp
        self.atk = atk
        self.df = df
        self.mgk = mgk

    def generate_pdmg(self):
        low = self.atk - 15
        high = self.atk + 15
        return random.randrange(low, high)

    def generate_mdmg(self):
        low = self.mgk - 15
        high = self.mgk + 15
        return random.randrange(low, high)

    def block_dmg(self, damage):
        blocked = damage - self.df
        return blocked


