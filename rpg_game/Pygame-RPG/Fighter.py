import pygame
from SpriteSheet import *
pygame.init()

# fighter class
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
        scale = 2
        color = (0, 0, 0)  # Black background for transparency

        # Load animations
        self.animation_list.append(
            SpriteSheet(f'../Images/Characters/{self.name}/Idle').get_frames(scale, color)
        )
        self.animation_list.append(
            SpriteSheet(f'../Images/Characters/{self.name}/Attack').get_frames(scale, color)
        )
        self.animation_list.append(
            SpriteSheet(f'../Images/Characters/{self.name}/Hurt').get_frames(scale, color)
        )
        self.animation_list.append(
            SpriteSheet(f'../Images/Characters/{self.name}/Death').get_frames(scale, color)
        )

        # Set the first frame as the default
        self.current_frame = self.animation_list[self.action][self.frame_index]

    def update(self):
        """
        Update the current animation frame.
        """
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0  # Loop back to the first frame
        self.current_frame = self.animation_list[self.action][int(self.frame_index)]

    def draw(self, surface):
        """
        Draw the current animation frame onto the given surface.
        """
        surface.blit(self.current_frame, (self.xcoord, self.ycoord))