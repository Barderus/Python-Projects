from person import Person
from magic import Magic
from items import Items

# Black Spells
fire = Magic("Fire", "black", 25, 45, 0, "damage",
             "The mage emits a jolt of fire from their hands towards the enemy")
thunder = Magic("Thunder", "black", 25, 45, 25, "damage",
                "Lightning jolts from the mage's hand towards the enemy")
blizzard = Magic("Blizzard", "black", 25, 45, 0, "damage",
                 "A cold wind forms icicles that shoot towards the enemy")
meteor = Magic("Meteor", "black", 100, 150, 0, "damage",
               "A small meteor shower crashes down upon the enemy")
quake = Magic("Quake", "black", 80, 60, 0, "damage",
              "The ground trembles as fissures open beneath the enemy's feet")
tornado = Magic("Tornado", "black", 75, 65, 0, "damage",
                "A fierce whirlwind surrounds the enemy, slashing at them with violent winds")
ultima = Magic("Ultima", "black", 120, 200, 0, "damage",
               "The ultimate destructive spell, causing catastrophic damage to all enemies")
dark = Magic("Dark", "black", 30, 60, 0, "damage",
             "A shadowy force strikes the enemy, dealing damage and shrouding them in darkness.")
bio = Magic("Bio", "black", 30, 50, 0, "damage",
            "A poisonous wind that deals damage over time to the target.")
drain = Magic("Drain", "black", 25, 40, 0, "drain",
              "A sinister spell that drains the target's life force, restoring a portion of health to the caster.")

# White Spells
cure = Magic("Cure", "white", 25, 0, 50, "healing",
             "A gentle green light envelops the target, healing their wounds")
cura = Magic("Cura", "white", 35, 0, 75, "healing",
             "A stronger healing light mends the target's deeper wounds")
curaga = Magic("Curaga", "white", 50, 0, 100, "healing",
               "A powerful healing force restores the target to full HP")
revive = Magic("Revive", "white", 75, 0, 65, "revival",
               "A soft light envelops the fallen ally, reviving them with 10% of their maximum HP")

# Green Spells
protect = Magic("Protect", "green", 25, 0, 0, "buff",
                "A magical barrier surrounds the target, reducing physical damage taken")
shell = Magic("Shell", "green", 25, 0, 0, "buff",
              "A shimmering shield surrounds the target, reducing magical damage taken")
speed = Magic("Speed", "green", 25, 0, 0, "buff",
              "A spell that enhances the speed of all allies, allowing them to act more quickly in battle.")

# Blue Spell
holy = Magic("Holy", "blue", 100, 90, 0, "damage",
             "A blinding light descends from above, purging the enemy with divine power")
flare = Magic("Flare", "blue", 110, 100, 0, "damage",
              "A concentrated burst of flames descends from the sky, engulfing the enemy.")

# Healing items
healing_pot = Items("Healing Potion", "heal", 1,"Restore 100 HP")
hi_pot = Items("HI-Potion", "heal", 1,"Restore 250 HP")
ether = Items("Ether", "heal", 1,"Restore 50MP")
hi_ether = Items("HI-Ether", "heal", 1,"Restore 100MP")
elixir = Items("Elixir", "heal", 1,"Restore 200 HP and 50 MP")
hi_elixir = Items("HI-Elixir", "heal", 1,"Restore to full Health and MP")
phoenix_down = Items("Phoenix Down", "heal", 1,"Revive target with 10% of HP")

# Status inc items
hermes_shoes = Items("Hermes Shoes", "buff", 1,"Increases target speed in 10")
red_fang = Items("Red Fang", "buff", 1,"Increases Attack in 10")
protect_coat = Items("Protect Coat", "buff", 1, "Increase Defense in 10")
faerie_bless = Items("Faerie Bless", "buff", 1,"Increase Magik Attack in 10")
witch_hat = Items("Witch's Hat", "buff", 1,"Increase Magik Defence in 10")

# Status dec items
slug_bomb = Items("Slug Bomb", "debuff", 1,"Lowers target Attack in 10")
acid = Items("Acid", "debuff", 1,"Lowers target Defense in 10")
spider_silk = Items("Spider Silk", "debuff", 1,"Lowers target Speed in 10")
moonstone = Items("Moonstone", "debuff", 1,"Lowers target Magik Attack in 10")
dragon_spit = Items("Dragon Spit", "debuff", 1, "Lowers target Magik Defense in 10")

# Creating player avatar
avatars= {
    "fighter": Person(
        name="Aragorn", hp=900, mp=60, atk=200, df=70, speed = 70, mgk_atk=50, mgk_def=50,
        items=[red_fang, hermes_shoes, acid, healing_pot],
        spells=[],
        descri = "A fearless and stalwart protector, the Warrior excels in close combat and defense."
    ),
    "bruiser": Person(
        name="Gimli", hp=1800, mp=30, atk=180, df=100, speed = 30, mgk_atk=30, mgk_def=60,
        items=[hi_pot, healing_pot, protect_coat, spider_silk],
        spells=[],
        descri = "A stout and resilient fighter, known for his unwavering strength and indomitable spirit"
    ),
    "barbarian": Person(
        name="Conan", hp=950, mp=30, atk=220, df=50, speed = 60, mgk_atk=40, mgk_def=50,
        items=[],
        spells=[healing_pot, hermes_shoes],
        descri = "A fierce and untamed warrior, the Barbarian relies on raw power and savage attacks to overwhelm foes."
    ),
    "healer": Person(
        name="Aerith", hp=700, mp=180, atk=30, df=80, speed = 45, mgk_atk=150, mgk_def=100,
        items=[hi_pot, ether, witch_hat, dragon_spit],
        spells=[cura, curaga, revive, flare],
        descri = "A compassionate and wise protector, the Healer specializes in restoring hp and safeguarding allies."
    ),
    "green mage": Person(
        name="Gandalf", hp=750, mp=200, atk=80, df=75, speed = 40, mgk_atk=200, mgk_def=90,
        items=[elixir, faerie_bless, dragon_spit, healing_pot],
        spells=[cure, protect, shell, holy],
        descri = "A versatile caster, the Green Mage blends healing magic with elemental attacks, balancing support and offense."
    ),
    "wizard": Person(
        name="Snape", hp=680, mp=220, atk=40, df=70, speed = 50, mgk_atk=220, mgk_def=70,
        items=[elixir, faerie_bless, dragon_spit, healing_pot],
        spells=[thunder, ultima, quake, tornado],
        descri = "A master of destructive magic, the Black Mage wields powerful spells to annihilate enemies from afar."
    ),
    "sorcerer": Person(
        name="Vivi", hp=650, mp=190, atk=40, df=70, speed = 60, mgk_atk=200, mgk_def=100,
        items=[elixir, faerie_bless, dragon_spit, healing_pot],
        spells=[fire, blizzard, ultima, meteor],
        descri = "A dark and enigmatic sorcerer, this Black Mage conjures arcane forces to devastate foes with precision."
    ),
    "you": Person(
        name= "You", hp=125, mp=100, atk=100, df=65, speed = 80, mgk_atk=125, mgk_def=80,
        items=[hi_pot, hi_elixir, phoenix_down],
        spells=[],
        descri = "The destined champion, the Hero embodies the player's choices, leading the charge against evil with courage and valor."
    )
}

# Create the NPC dictionary
allies = {
    "liora": Person(
        name="Liora the Healer", hp=600, mp=180, atk=55, df=50, speed = 35, mgk_atk=180, mgk_def=100,
        items=[healing_pot, hi_pot, elixir, phoenix_down, protect_coat],
        spells=[cure, cura, curaga, revive],
        descri="A compassionate healer from the White Lotus Order. Liora is known for her ability to mend even the most grievous wounds."
    ),
    "zarek": Person(
        name="Zarek the Black Mage", hp=500, mp=200, atk=50, df=65, speed = 65, mgk_atk=220, mgk_def=75,
        items=[ether, healing_pot, faerie_bless, moonstone],
        spells=[fire, thunder, blizzard],
        descri="A powerful black mage with mastery over the elements. Zarek's spells bring destruction to his foes."
    ),
    "eldric": Person(
        name="Eldric the Warrior", hp=650, mp=50, atk=120, df=70, speed = 90, mgk_atk=80, mgk_def=60,
        items=[healing_pot, hermes_shoes, acid, slug_bomb, red_fang],
        spells=[],
        descri="A seasoned warrior known for his unshakable resolve and strength in battle. Eldric excels in close combat."
    ),
    "sylphra": Person(
        name="Sylphra the White Mage", hp=450, mp=180, atk=40, df=50, speed = 50, mgk_atk=150, mgk_def=110,
        items=[hi_pot, ether, protect_coat, witch_hat, elixir],
        spells=[cura, protect, shell],
        descri="A gentle white mage with a deep connection to the divine. Sylphra uses her magic to protect and heal her allies."
    ),
    "thorn": Person(
        name="Thorne the Dark Blade", hp=620, mp=150, atk=90, df=65, speed = 55, mgk_atk=100, mgk_def=55,
        items=[ether, moonstone, witch_hat, spider_silk, dragon_spit, healing_pot],
        spells=[dark, drain],
        descri="A warrior with a mastery of dark magic, Thorne strikes fear into the hearts of his enemies with his cursed blade."
    ),
    "faye": Person(
        name="Faye the Mystic", hp=430, mp=170, atk=50, df=50, speed = 75, mgk_atk=220, mgk_def=75,
        items=[ether, faerie_bless, acid, spider_silk],
        spells=[bio, meteor, speed],
        descri="A mysterious mage who wields unconventional magic. Faye uses forbidden spells to outsmart and debilitate her foes."
    ),
    "garrick": Person(
        name="Garrick the Guardian", hp=800, mp=40, atk=120, df=100, speed = 40, mgk_atk=35, mgk_def=50,
        items=[healing_pot, hi_pot, protect_coat, red_fang],
        spells=[],
        descri="A stalwart warrior who prioritizes defense. Garrick’s immense strength and resilience make him a formidable protector."
    ),
    "talia": Person(
        name="Talia the Battle Cleric", hp=520, mp=120, atk=85, df=65, speed = 45, mgk_atk=90, mgk_def=85,
        items=[healing_pot, ether, phoenix_down, acid, moonstone],
        spells=[holy, flare, cure, protect],
        descri="A battle-hardened cleric who wields both a mace and holy magic. Talia can fight on the frontlines while supporting her allies."
    )
}

# Creating enemies
enemies = {
    # Enemies
    "goblin": Person(
        name="Goblin", hp=200, mp=50, atk=95, df=30, speed = 100, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "orc": Person(
        name="Orc", hp=600, mp=50, atk=145, df=50, speed = 75, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "kobold": Person(
        name="Kobold", hp=400, mp=50, atk=95, df=30, speed = 90, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "skeleton": Person(
        name="Skeleton Warrior", hp=380, mp=50, atk=105, df=30, speed = 60, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "knight": Person(
        name="Dark Knight", hp=650, mp=50, atk=170, df=70, speed = 70, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "ghoul": Person(
        name="Ghoul", hp=320, mp=50, atk=120, df=10, speed = 0, mgk_atk=10, mgk_def=20,
        items=[],
        spells=[],
        descri = ""
    ),
    "slime": Person(
        name="Slime", hp=500, mp=50, atk=105, df=120, speed = 10, mgk_atk=10, mgk_def=50,
        items=[],
        spells=[],
        descri = ""
    ),
    "necro": Person(
        name="Necromancer", hp=400, mp=400, atk=75, df=30, speed = 60, mgk_atk=160, mgk_def=80,
        items=[],
        spells=[dark, drain, fire, quake, revive],
        descri = ""
    ),
    "ghost": Person(
        name="Wraith", hp=720, mp=50, atk=190, df=100, speed = 70, mgk_atk=10, mgk_def=70,
        items=[],
        spells=[],
        descri = ""
    ),
    "troll": Person(
        name="Troll", hp=950, mp=50, atk=200, df=110, speed = 30, mgk_atk=10, mgk_def=50,
        items=[],
        spells=[],
        descri = ""
    ),
}
# Bosses
bosses = {
    "dragon": Person(
        name="Ur-Dragon", hp=4000, mp=50, atk=250, df=100, speed = 100, mgk_atk=50, mgk_def=100,
        items=[],
        spells=[],
        descri = ""
    ),
    "lich": Person(
        name="Lich", hp=2000, mp=1000, atk=100, df=80, mgk_atk=250, speed = 60, mgk_def=100,
        items=[],
        spells=[meteor, dark, drain, quake, cura, revive],
        descri = ""
    ),
    "demon": Person(
        name="Orcus", hp=6666, mp=666, atk=166, df=99, mgk_atk=99, speed = 120, mgk_def=99,
        items=[],
        spells=[],
        descri = ""
    )
}