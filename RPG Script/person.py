
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

    def damage(self, atk):
        pass

    def cast_magic(self):
        pass

    def cast_heal(self):
        pass

    def take_damage(self, damage):
        pass

    def reduce_mp(self):
        pass

    def choose_magic(self):
        pass

    def choose_item(self):
        pass

    def choose_target(self):
        pass

    def get_stats(self):
        pass
