import pygame
from spritesheet import SpriteSheet
from fighter import *

pygame.init()
clock = pygame.time.Clock()
fps = 60

BOTTOM_PANEL = 200
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500 + BOTTOM_PANEL
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeons and the Ur-Dragon")
running = True

# Load background
background_img = pygame.image.load("../Images/Background/Eerie Cave Background1.png").convert_alpha()
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT - BOTTOM_PANEL))

# Load Panel image
panel_img = pygame.image.load("../Images/Background/panel.png").convert_alpha()
panel_img = pygame.transform.scale(panel_img, (SCREEN_WIDTH, BOTTOM_PANEL))

ghoul_atk_img = pygame.image.load("../Images/Characters/2 - Row/Ghoul/Attack/Attack1.png").convert_alpha()
sprite_sheet = SpriteSheet(ghoul_atk_img)

# Animation list
animation_list = []
animation_steps = 11
last_update = pygame.time.get_ticks()
animation_cooldown = 75 # 75ms
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image( x, 144, 110, 2, BLACK))


def draw_bg():
    screen.blit(background_img, (0, 0))

# function for drawing panel
def draw_panel():
    #draw panel rectangle
    screen.blit(panel_img, (0, SCREEN_HEIGHT - BOTTOM_PANEL))
    #show knight stats


def draw_menu_action():

    border_rect = pygame.Rect(130, 585, 585, 130)
    border_rect.center = (SCREEN_WIDTH -900, SCREEN_HEIGHT - BOTTOM_PANEL / 2)
    pygame.draw.rect(screen, (184,10,203), border_rect)

    rect = pygame.Rect(120, 575, 575, 120)
    rect.center = (SCREEN_WIDTH - 900, SCREEN_HEIGHT - BOTTOM_PANEL / 2)
    pygame.draw.rect(screen, (83,143,229), rect)


while running:
    clock.tick(fps)

    # Draw background
    draw_bg()
    draw_panel()

    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0


    screen.blit(animation_list[frame], (550, 330))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()

