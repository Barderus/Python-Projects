from magic import Magic
from person import Person
from characters import *
import os
import random

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
    print("\n\t\t\t\t\t\tChoose your hero: ")

    # List of all the character names to be chosen from
    avatar_names = [avatars["fighter"].name, avatars["bruiser"].name, avatars["barbarian"].name,
                    avatars["healer"].name, avatars["green mage"].name, avatars["wizard"].name,
                    avatars["sorcerer"].name, avatars["you"].name]

    # Display the names in a list format. Also including the hero's description.
    for index, name in enumerate(avatar_names):
        print(f"\t\t\t\t\t\t{index+1}. {name}")
        avatar_obj = next(avatar for avatar in avatars.values() if avatar.name == name)
        print(f"\t\t\t\t\t {avatar_obj.descri}\n")

    # Control loop to check if the name entered by the user is valid
    while True:
        hero_choice = input("Enter the hero's name: ").capitalize()
        if hero_choice in avatar_names:
            name_to_avatar = {avatar.name: avatar for avatar in avatars.values()}
            selected_hero = name_to_avatar[hero_choice]
            print(f"You have selected: {selected_hero.name}")
            break
        else:
            print(f"{hero_choice} is not a playable characters!")

    # Returns the name of the hero
    return hero_choice

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


def gen_allies():
    """
        This function generates a random list of allies to join the player to fight
    """
    allies_list = []

    for i in range(1, 3):
        allies_list.append(random.choice(allies_options))

    return allies_list


def clear():
    """
        This function clears the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    # Prompt ally for their hero
    hero = prompt()

    # Checking the hero name
    print(hero)
    clear()

main()