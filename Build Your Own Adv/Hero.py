import random


class Hero:
    def __init__(self, hp, atk, df):
        self.hp = hp
        self.atk = atk
        self.df = df

    def generate_dmg(self):
        low = self.atk - 15
        high = self.atk + 15
        return random.randrange(low, high)

    def block_dmg(self, damage):
        blocked = damage - self.df
        return blocked
