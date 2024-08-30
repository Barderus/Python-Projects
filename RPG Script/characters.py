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
               "A powerful healing force restores the target to full health")
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
        name="Aragorn",
        health=1500,
        mp=200,
        atk=200,
        df=150,
        mgk_atk=50,
        mgk_def=100,
        items=[],
        spells=[]
    ),
    "dwarf": Person(
        name="Gimli",
        health=1800,
        mp=100,
        atk=220,
        df=200,
        mgk_atk=30,
        mgk_def=150,
        items=[],
        spells=[]
    ),
    "barbarian": Person(
        name="Conan",
        health=1700,
        mp=150,
        atk=210,
        df=180,
        mgk_atk=40,
        mgk_def=120,
        items=[],
        spells=[]
    ),
    "healer": Person(
        name="Aerith",
        health=1200,
        mp=500,
        atk=30,
        df=80,
        mgk_atk=150,
        mgk_def=120,
        items=[],
        spells=[cura, curaga, revive, flare]
    ),
    "gandalf": Person(
        name="Gandalf",
        health=1400,
        mp=400,
        atk=120,
        df=150,
        mgk_atk=100,
        mgk_def=140,
        items=[],
        spells=[cure, protect, shell, holy]
    ),
    "snape": Person(
        name="Severus Snape",
        health=1100,
        mp=600,
        atk=40,
        df=70,
        mgk_atk=200,
        mgk_def=100,
        items=[],
        spells=[thunder, ultima, quake, tornado]
    ),
    "vivi": Person(
        name="Vivi",
        health=1100,
        mp=600,
        atk=40,
        df=70,
        mgk_atk=200,
        mgk_def=100,
        items=[],
        spells=[fire, blizzard, ultima, meteor]
    )
}

# Creating enemies
enemies = {
    # Enemies
    "goblin": Person(
        name="Goblin",
        health=400,
        mp=50,
        atk=70,
        df=30,
        mgk_atk=10,
        mgk_def=20,
        items=[],
        spells=[]
    ),
    "orc": Person(
        name="Orc",
        health=600,
        mp=40,
        atk=100,
        df=50,
        mgk_atk=20,
        mgk_def=30,
        items=[],
        spells=[]
    ),
    "kobold": Person(
        name="Kobold",
        health=350,
        mp=30,
        atk=60,
        df=20,
        mgk_atk=15,
        mgk_def=25,
        items=[],
        spells=[]
    ),
    "skeleton": Person(
        name="Skeleton Warrior",
        health=500,
        mp=60,
        atk=80,
        df=40,
        mgk_atk=10,
        mgk_def=35,
        items=[],
        spells=[]
    ),
    "knight": Person(
        name="Dark Knight",
        health=700,
        mp=70,
        atk=120,
        df=60,
        mgk_atk=25,
        mgk_def=40,
        items=[],
        spells=[]
    ),
    "ghoul": Person(
        name="Ghoul",
        health=550,
        mp=80,
        atk=90,
        df=50,
        mgk_atk=30,
        mgk_def=45,
        items=[],
        spells=[]
    ),
    "slime": Person(
        name="Slime",
        health=650,
        mp=50,
        atk=110,
        df=45,
        mgk_atk=20,
        mgk_def = 30,
        items=[],
        spells=[]
    ),
    "necro": Person(
        name="Necromancer",
        health=600,
        mp=150,
        atk=70,
        df=30,
        mgk_atk=150,
        mgk_def=70,
        items=[],
        spells=[]
    ),
    "ghost": Person(
        name="Wraith",
        health=500,
        mp=120,
        atk=80,
        df=35,
        mgk_atk=130,
        mgk_def=60,
        items=[],
        spells=[]
    ),
    "troll": Person(
        name="Troll",
        health=800,
        mp=40,
        atk=150,
        df=80,
        mgk_atk=15,
        mgk_def=50,
        items=[],
        spells=[]
    ),
}
# Bosses
bosses = {
    "dragon": Person(
        name="Ur - Dragon",
        health=2000,
        mp=300,
        atk=250,
        df=100,
        mgk_atk=250,
        mgk_def=100,
        items=[],
        spells=[]
    ),
    "lich": Person(
        name="Lich",
        health=1800,
        mp=400,
        atk=100,
        df=80,
        mgk_atk=300,
        mgk_def=90,
        items=[],
        spells=[]
    ),
    "demon": Person(
        name="Orcus",
        health=1600,
        mp=500,
        atk=90,
        df=70,
        mgk_atk=350,
        mgk_def=80,
        items=[],
        spells=[]
    )
}