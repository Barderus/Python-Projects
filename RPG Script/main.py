from magic import Magic
from person import Person
from characters import *
import os
import random
import time

def battle_screen():
    pass

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
    enemy_list = list(enemies.values())
    boss_list = list(bosses.values())

    enemy_fight_set= set()
    boss_fight_set= set()

    #  Select the enemies
    while len(enemy_fight_set) < random.randint(1, 6):
        enemy_fight_set.add(random.choice(enemy_list))

    # Select the enemies for the boss fight
    for x in range(1, 3):
        boss_fight_set.add(random.choice(enemy_list))
    boss_fight_set.add(random.choice(boss_list))


    return list(enemy_fight_set), list(boss_fight_set)

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
    time.sleep(5)
    print("\n" * 100)

def battle(ally_team, enemies_team):
    ally_team[0].attacks(enemies_team[0])

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

    battle(allies_team, enemies_fight)

main()