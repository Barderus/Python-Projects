class Magic:
    def __init__(self, name, school, dmg, heal, mp, dmg_type, descri):
        self.name = name
        self.mp = mp
        self.school = school
        self.dmg = dmg
        self.heal = heal
        self.dmg_type = dmg_type
        self.descri = descri

    def __str__(self):
        return (f"Name: {self.name}"
                f"\nDamage: {self.dmg}\tMP: {self.mp}"
                f"Description: {self.descri}")
