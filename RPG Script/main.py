"""
    Queuing characters
        1. Queue each character to a queue if char.hp > 0 sorted by their speed
        2. Check if char.hp > 0, if not, dequeue it
        3. Dequeue each char after they act
        4. If queue is empty, finish the round
            Add all chars again if their hp > 0
"""
from characters import *
import random
import time
from collections import deque


def battle_screen(ally_team, enemy_team):
    """ Display each character's health points and their names """
    # Define the width for formatting
    name_width = 20  # Width for names
    hp_width = 15  # Width for HP and max HP display
    mp_width = 15  # Width for MP and max MP display

    # Display ally team
    print(f"{ally_team[0].name:<{name_width}}\t{ally_team[1].name:<{name_width}}\t"
          f"{ally_team[2].name:<{name_width}}\t{ally_team[3].name:<{name_width}}")
    print(f"HP: {int(ally_team[0].get_hp()):<3}/{int(ally_team[0].maxhp):<{hp_width}}\t"
          f"HP: {int(ally_team[1].get_hp()):<3}/{int(ally_team[1].maxhp):<{hp_width}}\t"
          f"HP: {int(ally_team[2].get_hp()):<3}/{int(ally_team[2].maxhp):<{hp_width}}\t"
          f"HP: {int(ally_team[3].get_hp()):<3}/{int(ally_team[3].maxhp):<{hp_width}}")

    print(f"MP: {int(ally_team[0].get_mp()):<3}/{int(ally_team[0].maxmp):<{mp_width}}\t"
          f"MP: {int(ally_team[1].get_mp()):<3}/{int(ally_team[1].maxmp):<{mp_width}}\t"
          f"MP: {int(ally_team[2].get_mp()):<3}/{int(ally_team[2].maxmp):<{mp_width}}\t"
          f"MP: {int(ally_team[3].get_mp()):<3}/{int(ally_team[3].maxmp):<{mp_width}}")

    print()

    # Display enemy team
    print(f"{enemy_team[0].name:<{name_width}}\t{enemy_team[1].name:<{name_width}}\t"
          f"{enemy_team[2].name:<{name_width}}\t{enemy_team[3].name:<{name_width}}")
    print(f"HP: {int(enemy_team[0].get_hp()):<3}/{int(enemy_team[0].maxhp):<{hp_width}}\t"
          f"HP: {int(enemy_team[1].get_hp()):<3}/{int(enemy_team[1].maxhp):<{hp_width}}\t"
          f"HP: {int(enemy_team[2].get_hp()):<3}/{int(enemy_team[2].maxhp):<{hp_width}}\t"
          f"HP: {int(enemy_team[3].get_hp()):<3}/{int(enemy_team[3].maxhp):<{hp_width}}")
    print()



def attack(ally, enemy_team):
    while True:
        char_name = input("\n\tChoose a target: "
                                  f"\n\t {enemy_team[0].name:^10}\n "
                                  f"\n\t {enemy_team[1].name:^10}\n"
                                  f"\n\t {enemy_team[2].name:^10}\n "
                                  f"\n\t {enemy_team[3].name:^10}\n "
                                  "\n\t Target: ")

        # Find the target in the enemy team
        target = None
        for enemy in enemy_team:
            if enemy.name.lower() == char_name.lower():  # Case-insensitive comparison
                target = enemy
                break

        if target is None:
            print("Invalid target name. Please try again.")
            continue

        if target.hp <= 0:
            print(f"{target.name} is already dead. Choose another target.")
        else:
            ally.attacks(target)  # Attack the selected target
            if target.hp == 0:
                print(f"{target.name} is dead.")
            break

def cast_spell(ally, enemy_team, ally_team):
    # Check if the ally has any spells
    if not ally.spells:
        print("No spells to display")
        return "c"

    # Display available spells
    for spell in ally.spells:
        print(f"\nSpell Name: {spell.name} | MP cost: {spell.mp} | Damage: {spell.dmg} \nDescription: {spell.descri}")

    # Get user input for choosing a spell
    choose_spell = input("\n\tChoose a spell (c to cancel): ").strip().lower()
    if choose_spell == "c":
        return "c"


    # Find the chosen spell
    chosen_spell = next((spell for spell in ally.spells if spell.name.lower() == choose_spell), None)
    if not chosen_spell:
        print("Spell not found.")
        return "c"


    # Create a list of valid targets (enemies and allies)
    all_targets = [obj for obj in enemy_team if obj.hp > 0] + [obj for obj in ally_team if obj.hp > 0]

    # Target selection loop
    while True:
        char_name = input("\n\tEnter the name of your target: ").strip().lower()

        # Find target by name
        target = next((person for person in all_targets if person.name.lower() == char_name), None)

        if target:
            break
        else:
            print("Invalid target. Please try again.")

    #if not chosen_spell.check_mp(ally):
        #return f"{ally.name} is out of mp and can't cast magic right now."

    ally.cast_magic(target, chosen_spell)


def items(ally, enemy, ally_team):
    pass


def actions(ally, enemy_team, ally_team):
    while True:
        action = input(f"\n{ally.name}'s action:"
                       "\nACTIONS:"
                       "\n1. Attack"
                       "\n2. Magic"
                       "\n3. Items"
                       "\nChoose Action: ").strip()
        if action == "1":
            attack(ally, enemy_team)
            break
        elif action == "2":
            result = cast_spell(ally, enemy_team, ally_team)
            if result == "c":
                continue
            break
        elif action == "3":
            items(ally, enemy_team, ally_team)
            break
        else:
            print("Invalid action. Please choose 1, 2, or 3.")


def enemy_attack(ally_team, enemy):
    random_ally = random.choice(ally_team)
    if random_ally.hp <= 0:
        print(f"{enemy.name} slips and isn't able to attack.")
    else:
        enemy.attacks(random_ally)
        if random_ally.hp == 0:
            print(f"{random_ally.name} is dead.")


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
        print(f"\t\t{index + 1}. {name}")
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

    enemy_fight_set = set()
    boss_fight_set = set()

    #  Select the enemies
    while len(enemy_fight_set) < 4:
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
    time.sleep(2)
    print("\n" * 100)


def battle(ally_team, enemies_team):
    running = True
    char_q = deque()
    char_list = ally_team + enemies_team
    char_list = sorted(char_list, key=lambda chars: chars.speed if chars.hp > 0 else 0, reverse=True)
    for char in char_list:
        char_q.append(char)

    print()
    while running and char_q:
        battle_screen(ally_team, enemies_team)
        current_char = char_q.popleft()

        if current_char.hp > 0:
            if current_char in ally_team:
                actions(current_char, enemies_team, ally_team)
            elif current_char in enemies_team:
                enemy_attack(ally_team, current_char)

        if all(enemy.hp <= 0 for enemy in enemies_team):
            print("All enemies are defeated! You win!")
            running = False
            break
        if all(allies.hp <= 0 for allies in ally_team):
            print("You failed. You and your allies perished in the hands of enemy.")
            running = False
            break

        if not char_q:
            char_list = [char for char in ally_team + enemies_team if char.hp > 0]
            if char_list:  # Refill the queue if there are still characters alive
                char_list = sorted(char_list, key=lambda chars: char.speed, reverse=True)
                for char in char_list:
                    char_q.append(char)
            else:
                print("Battle is over!")
                running = False


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

    battle(main_team, enemies_fight)


if "__main__" == __name__:
    main()
