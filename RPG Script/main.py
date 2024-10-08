from characters import *
import random
import time

def battle_screen(allies, enemies):
    """ Display each character health points and their names """
    print(f"{allies[0].name:^10}\t\t{allies[1].name:^10}\t\t{allies[2].name:^10}\t\t{allies[3].name:^10}")
    print(f"HP: {allies[0].get_hp()} /{allies[0].maxhp:^10}\t\t"
          f"HP: {allies[1].get_hp()} /{allies[1].maxhp:^10}\t\t"
          f"HP: {allies[2].get_hp()} /{allies[2].maxhp:^10}\t\t"
          f"HP: {allies[3].get_hp()} /{allies[3].maxhp:^10}")
    print()
    print(f"{enemies[0].name:^15}\t\t{enemies[1].name:^15}\t\t{enemies[2].name:^15}\t\t{enemies[3].name:^15}")
    print(f"HP: {enemies[0].get_hp()} /{enemies[0].maxhp:^10} \t\t"
          f"HP: {enemies[1].get_hp()} /{enemies[1].maxhp:^10}\t\t"
          f"HP: {enemies[2].get_hp()} /{enemies[2].maxhp:^10}\t\t"
          f"HP: {enemies[3].get_hp()} /{enemies[3].maxhp:^10}")

def attack(ally, enemies):
    while True:
        choose_target = int(input("Choose a target: "
                                  f"1. {enemies[0].name:^10}\n "
                                  f"2. {enemies[1].name:^10}\n"
                                  f"3. {enemies[2].name:^10}\n "
                                  f"4. {enemies[3].name:^10}\n "))
        if enemies[choose_target].hp <= 0:
            print(f"{enemies[choose_target].name} is already dead. Choose another target")
        else:
            ally.attacks(enemies[choose_target])
            break

def cast_magic(ally, enemy):
    pass

def items(ally, enemy):
    pass

def actions(allies, enemies):
    action = input("ACTIONS:"
                   "1. Attack"
                   "2. Magic"
                   "3. Items"
                   "Choose Action: ")
    if action == "1":
        attack(allies, enemies)
    elif action == "2":
        cast_magic(allies, enemies)
    elif action == "3":
        items(allies, enemies)

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
    time.sleep(5)
    print("\n" * 100)

def battle(ally_team, enemies_team):

    for x in range(10):
        battle_screen(ally_team, enemies_team)
        for k in range(2):
            random_ally = random.choice(ally_team)
            random_enemy = random.choice(enemies_team)
            random_ally.attacks(random_enemy)
            random_enemy.attacks(random_ally)

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

main()