from person import Person
from magic import Magic

fire = Magic("Fire", "black", 600, 0, 25,
             "The mage emits a jolt of fire from their hands towards the enemy")
thunder = Magic("Thunder", "black", 600, 0, 25,
                "Lightning jolts from the mage's hand towards the enemy")
blizzard = Magic("Blizzard", "black", 600, 0, 25,
                 "A cold wind forms icicles that shoot towards the enemy")
meteor = Magic("Meteor", "black", 1200, 0, 50,
               "A small meteor shower crashes down upon the enemy")
quake = Magic("Quake", "black", 140, 0, 15,
              "The ground trembles as fissures open beneath the enemy's feet")
tornado = Magic("Tornado", "black", 1600, 0, 45,
                "A fierce whirlwind surrounds the enemy, slashing at them with violent winds")
ultima = Magic("Ultima", "black", 3000, 0, 100,
               "The ultimate destructive spell, causing catastrophic damage to all enemies")

# Creating White spells
cure = Magic("Cure", "white", 0, 400, 20,
             "A gentle green light envelops the target, healing their wounds")
cura = Magic("Cura", "white", 0, 800, 40,
             "A stronger healing light mends the target's deeper wounds")
curaga = Magic("Curaga", "white", 0, 1200, 60,
               "A powerful healing force restores the target to full hp")
protect = Magic("Protect", "white", 0, 0, 35,
                "A magical barrier surrounds the target, reducing physical damage taken")
shell = Magic("Shell", "white", 0, 0, 35,
              "A shimmering shield surrounds the target, reducing magical damage taken")
flare = Magic("Flare", "black", 1800, 0, 75,
              "A concentrated burst of descends from the sky, engulfing the enemy in holy flames")
holy = Magic("Holy", "white", 2000, 0, 80,
             "A blinding light descends from above, purging the enemy with divine power")
revive = Magic("Revive", "white", 0, 0, 50,
               "A soft light envelops the fallen ally, reviving them with 10% of their maximum HP")

# Creating player avatar
avatars= {
    "fighter": Person(
        name="Aragorn", hp=1500, mp=200, atk=200, df=150, mgk_atk=50, mgk_def=100,
        items=[],
        spells=[],
        descri = "A fearless and stalwart protector, the Warrior excels in close combat and defense."
    ),
    "bruiser": Person(
        name="Gimli", hp=1800, mp=100, atk=220, df=200, mgk_atk=30, mgk_def=150,
        items=[],
        spells=[],
        descri = "A stout and resilient fighter, known for his unwavering strength and indomitable spirit"
    ),
    "barbarian": Person(
        name="Conan",
        hp=1700, mp=150, atk=210, df=180, mgk_atk=40, mgk_def=120,
        items=[],
        spells=[],
        descri = "A fierce and untamed warrior, the Barbarian relies on raw power and savage attacks to overwhelm foes."
    ),
    "healer": Person(
        name="Aerith",
        hp=1200, mp=500, atk=30, df=80, mgk_atk=150, mgk_def=120,
        items=[],
        spells=[cura, curaga, revive, flare],
        descri = "A compassionate and wise protector, the Healer specializes in restoring hp and safeguarding allies."
    ),
    "green mage": Person(
        name="Gandalf", hp=1400, mp=400, atk=120, df=150, mgk_atk=100, mgk_def=140,
        items=[],
        spells=[cure, protect, shell, holy],
        descri = "A versatile caster, the Green Mage blends healing magic with elemental attacks, balancing support and offense."
    ),
    "wizard": Person(
        name="Snape",
        hp=1100, mp=600, atk=40, df=70, mgk_atk=200, mgk_def=100,
        items=[],
        spells=[thunder, ultima, quake, tornado],
        descri = "A master of destructive magic, the Black Mage wields powerful spells to annihilate enemies from afar."
    ),
    "sorcerer": Person(
        name="Vivi",
        hp=1100, mp=600, atk=40, df=70, mgk_atk=200, mgk_def=100,
        items=[],
        spells=[fire, blizzard, ultima, meteor],
        descri = "A dark and enigmatic sorcerer, this Black Mage conjures arcane forces to devastate foes with precision."
    ),
    "you": Person(
        name= "You", hp=1500, mp=500, atk=50, df=50, mgk_atk=50, mgk_def=50,
        items=[],
        spells=[],
        descri = "The destined champion, the Hero embodies the player's choices, leading the charge against evil with courage and valor."
    )
}

# Create the NPC dictionary
allies = {
    "liora": Person(
        name="Liora the Healer", hp=450, mp=300, atk=50, df=40, mgk_atk=70, mgk_def=90,
        items=[],
        spells=["Cure", "Raise", "Regen"],
        descri="A compassionate healer from the White Lotus Order. Liora is known for her ability to mend even the most grievous wounds."
    ),
    "zarek": Person(
        name="Zarek the Black Mage", hp=320, mp=450, atk=30, df=35, mgk_atk=95, mgk_def=75,
        items=[],
        spells=["Fire", "Thunder", "Blizzard"],
        descri="A powerful black mage with mastery over the elements. Zarek's spells bring destruction to his foes."
    ),
    "eldric": Person(
        name="Eldric the Warrior", hp=700, mp=100, atk=85, df=70, mgk_atk=20, mgk_def=30,
        items=[],
        spells=[],
        descri="A seasoned warrior known for his unshakable resolve and strength in battle. Eldric excels in close combat."
    ),
    "sylphra": Person(
        name="Sylphra the White Mage", hp=400, mp=350, atk=40, df=45, mgk_atk=65, mgk_def=80,
        items=[],
        spells=["Cura", "Protect", "Esuna"],
        descri="A gentle white mage with a deep connection to the divine. Sylphra uses her magic to protect and heal her allies."
    ),
    "thorn": Person(
        name="Thorne the Dark Blade", hp=620, mp=150, atk=90, df=65, mgk_atk=45, mgk_def=55,
        items=[],
        spells=["Dark", "Drain"],
        descri="A warrior with a mastery of dark magic, Thorne strikes fear into the hearts of his enemies with his cursed blade."
    ),
    "faye": Person(
        name="Faye the Mystic", hp=380, mp=420, atk=25, df=30, mgk_atk=85, mgk_def=70,
        items=[],
        spells=["Bio", "Comet", "Silence"],
        descri="A mysterious mage who wields unconventional magic. Faye uses forbidden spells to outsmart and debilitate her foes."
    ),
    "garrick": Person(
        name="Garrick the Guardian", hp=800, mp=80, atk=75, df=85, mgk_atk=35, mgk_def=40,
        items=[],
        spells=[],
        descri="A stalwart warrior who prioritizes defense. Garrick’s immense strength and resilience make him a formidable protector."
    ),
    "talia": Person(
        name="Talia the Battle Cleric", hp=520, mp=250, atk=60, df=55, mgk_atk=55, mgk_def=65,
        items=[],
        spells=["Holy", "Cura", "Shell"],
        descri="A battle-hardened cleric who wields both a mace and holy magic. Talia can fight on the frontlines while supporting her allies."
    )
}

# Creating enemies
enemies = {
    # Enemies
    "goblin": Person(
        name="Goblin", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "orc": Person(
        name="Orc", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "kobold": Person(
        name="Kobold", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "skeleton": Person(
        name="Skeleton Warrior", hp=400, mp=70, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "knight": Person(
        name="Dark Knight", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "ghoul": Person(
        name="Ghoul", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "slime": Person(
        name="Slime", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "necro": Person(
        name="Necromancer", hp=400, mp=50, atk=40, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "ghost": Person(
        name="Wraith", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "troll": Person(
        name="Troll", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
}
# Bosses
bosses = {
    "dragon": Person(
        name="Ur-Dragon", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "lich": Person(
        name="Lich", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "demon": Person(
        name="Orcus", hp=400, mp=50, atk=70, df=30, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    )
}