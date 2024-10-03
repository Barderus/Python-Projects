from magic import Magic
from person import Person
from characters import *
import os
import random
import time

def prompt():
    """
        This function displays a welcoming message and prompts the user for their characters.
    """
    # Display a welcome message and prompt user for their character
    print("\t\t\t\tWelcome to Dungeons and the Ur-Dragon!\n\n\
     \tAre you ready to embark on an epic adventure, defeat the forces of evil,\n\
     \tand become a legendary hero?\n\n")
    input("\t\t\t\tEnter any button to begin...\n >")
    print("\t\t\t\t\t\tLet the quest begin!")
    print("\n\t\tChoose your hero: ")

    # List of all the character names to be chosen from
    avatar_names = [avatar.name for avatar in avatars.values()]

    # Display the names in a list format. Also including the hero's description.
    for index, name in enumerate(avatar_names):
        print(f"\t\t{index+1}. {name}")
        avatar_obj = next(avatar for avatar in avatars.values() if avatar.name == name)
        print(f"\t\t {avatar_obj.descri}\n")

    # Control loop to check if the name entered by the user is valid
    while True:
        hero_choice = input("Enter the hero's name: ").capitalize()
        if hero_choice in avatar_names:
            name_to_avatar = {avatar.name: avatar for avatar in avatars.values()}
            selected_hero = name_to_avatar[hero_choice]  # Now this is the object
            break
        else:
            print(f"{hero_choice} is not a playable character!")

    # Returns the name of the hero
    return selected_hero

def gen_enemies():
    """
        This function generates a random list of enemies for the player to fight
    """
    enemy_names = [enemies["goblin"].name, enemies["orc"].name, enemies["kobold"].name,
                   enemies["skeleton"].name, enemies["ghoul"].name, enemies["slime"].name,
                   enemies["necro"].name, enemies["troll"].name]

    boss_names = [bosses["dragon"].name, bosses["lich"].name, bosses["demon"].name]

    enemies_fight = []
    boss_fight = []

    # Get the enemies for a fight
    for i in range(1, 4):
        enemies_fight.append(random.choice(enemy_names))

    # Get the enemies for boss fight
    for i in range(1, 3):
        boss_fight.append(random.choice(enemy_names))
    boss_fight.append(random.choice(boss_names))

    return enemies_fight, boss_fight

def gen_allies():
    """
        This function generates a random list of allies to join the player to fight
    """
    allies_list = list(allies.values())

    allies_team = set()
    while len(allies_team) < 3:
        allies_team.add(random.choice(allies_list))
    return list(allies_team)

def clear():
    """
        This function clears the screen
            os.system('cls' if os.name == 'nt' else 'clear') << Not working
    """
    time.sleep(10)
    print("\n" * 100)

def battle():
    pass
def main():

    # Generate allies and enemies
    allies_team = gen_allies()
    enemies_fight, boss_fight = gen_enemies()

    # Prompt the user for their hero
    selected_hero = prompt()

    # Create the main team
    main_team = [selected_hero] + allies_team

    # Display the team roster with access to object attributes
    print("Your team roster: ")
    for ally in main_team:
        print(f"\t{ally.name}\n\t\t{ally.descri}")
    clear()

    battle()

main()