import pygame
from SpriteSheet import *
pygame.init()

# fighter class
"""
    Initializes a character with specific attributes and properties.

    Parameters:
    ----------
    name : str
        The name of the character.
    hp : int
        The maximum health points (HP) of the character.
    mp : int
        The initial mana points (MP) of the character.
    atk : int
        The attack power of the character for physical attacks.
    df : int
        The defense stat of the character to reduce incoming damage.
    speed : int
        The speed of the character, determining action order in battles.
    mgk_atk : int
        The magic attack stat of the character for spell potency.
    mgk_def : int
        The magic defense stat of the character to reduce magic damage.
    spells : list
        A list of available spells the character can cast.
    xcoord : int
        The initial x-coordinate of the character in the game space.
    ycoord : int
        The initial y-coordinate of the character in the game space.
    boss : bool, optional
        A flag indicating if the character is a boss (default is False).
"""
class Fighter:
    def __init__(self, name, hp, mp, atk, df, speed, mgk_atk, mgk_def, spells, xcoord, ycoord, boss=False):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.strength = atk
        self.mp = mp
        self.df = df
        self.speed = speed
        self.mgk_atk = mgk_atk
        self.mgk_def = mgk_def
        self.spells = spells
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.boss = boss
        self.alive = True
        self.animation_list = []
        self.action = 0  # 0:idle, 1:attack, 2:hurt, 3:dead
        self.frame_index = 0
        self.animation_speed = 0.2  # Adjust for slower/faster animations

        # Common animation settings
        width = 64  # Example width (adjust as needed)
        height = 64  # Example height (adjust as needed)
        scale = 2
        color = (0, 0, 0)  # Black background to be transparent

        # Load and store each character sprites
        #                                       Images\Characters\{}\Idle
        idle_sheet = SpriteSheet(images_folder=f'../Images/Characters/{self.name}/Idle')
        attack_sheet = SpriteSheet(images_folder=f'../Images/Characters/{self.name}/Attack')
        hurt_sheet = SpriteSheet(images_folder=f'../Images/Characters/{self.name}/Hurt')
        death_sheet = SpriteSheet(images_folder=f'../Images/Characters/{self.name}/Death')

        self.animation_list.append(idle_sheet.get_frames(None, width, height, scale, color))
        self.animation_list.append(attack_sheet.get_frames(None, width, height, scale, color))
        self.animation_list.append(hurt_sheet.get_frames(None, width, height, scale, color))
        self.animation_list.append(death_sheet.get_frames(None, width, height, scale, color))

        self.current_frame = self.animation_list[self.action][self.frame_index]

    def update(self):
        # Update animation frame
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
        self.current_frame = self.animation_list[self.action][int(self.frame_index)]

    def draw(self, surface):
        # Draw current animation frame
        surface.blit(self.current_frame, (self.xcoord, self.ycoord))


