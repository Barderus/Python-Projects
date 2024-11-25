import pygame
from Fighter import *
pygame.init()

clock = pygame.time.Clock()
fps = 60

BOTTOM_PANEL = 200
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500 + BOTTOM_PANEL
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeons and the Ur-Dragon")

# Load background
background_img = pygame.image.load("../Images/Background/Eerie Cave Background1.png").convert_alpha()
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT - BOTTOM_PANEL))

# Load Panel image
panel_img = pygame.image.load("../Images/Background/panel.png").convert_alpha()
panel_img = pygame.transform.scale(panel_img, (SCREEN_WIDTH, BOTTOM_PANEL))

# define game variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
potion_effect = 15
clicked = False
game_over = 0

# define fonts
game_font = pygame.font.SysFont('Times New Roman', 26)

# define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)


hero = Fighter("Aerith", 100, 100, 100, 100, 100, 100, 100, None, 64, 64)


def draw_bg():
    screen.blit(background_img, (0, 0))


def draw_panel():
    # draw panel rectangle
    screen.blit(panel_img, (0, SCREEN_HEIGHT - BOTTOM_PANEL))


def draw_menu_action():
    border_rect = pygame.Rect(130, 585, 585, 130)
    border_rect.center = (SCREEN_WIDTH - 900, SCREEN_HEIGHT - BOTTOM_PANEL / 2)
    pygame.draw.rect(screen, (184, 10, 203), border_rect)

    rect = pygame.Rect(120, 575, 575, 120)
    rect.center = (SCREEN_WIDTH - 900, SCREEN_HEIGHT - BOTTOM_PANEL / 2)
    pygame.draw.rect(screen, (83, 143, 229), rect)


run = True
while run:

    clock.tick(fps)

    # draw background
    draw_bg()

    # draw panel
    draw_panel()

    # Update and draw the fighter
    hero.update()
    hero.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
