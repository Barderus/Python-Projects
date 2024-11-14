import pygame
from spritesheet import SpriteSheet

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

# Ghoul animation
ghoul_atk_img = pygame.image.load("../Images/Characters/2 - Row/Ghoul/Attack/Attack1.png").convert_alpha()
ghoul_sprite_sheet = SpriteSheet(ghoul_atk_img)

# Wraith animation
wraith_atk_img = pygame.image.load("../Images/Characters/2 - Row/Wraith/Attack/Attack3.png").convert_alpha()
wraith_sprite_sheet = SpriteSheet(wraith_atk_img)

# Dark Wizard
dark_wizard_atk_img = pygame.image.load("../Images/Characters/2 - Row/Dark Wizard/Attack1.png")
dark_wizard_sprite_sheet = SpriteSheet(dark_wizard_atk_img)

# Fire worm
fire_worm_atk_img = pygame.image.load("../Images/Characters/2 - Row/Fire Worm/Attack/Attack.png")
fire_worm_sprite_sheet = SpriteSheet(fire_worm_atk_img)

last_update = pygame.time.get_ticks()
animation_cooldown = 75# 75ms
ghoul_frame = 0
wraith_frame = 0
d_wizard_frame = 0
fire_worm_frame = 0


# Animation list for ghoul
ghoul_animation_list = []
ghoul_animation_steps = 11
for x in range(ghoul_animation_steps):
    ghoul_animation_list.append(ghoul_sprite_sheet.get_image( x, 144, 110, 2, BLACK))

# Animation list for wraith
wraith_animation_list = []
wraith_animation_steps = 14
for x in range(wraith_animation_steps):
     wraith_animation_list.append(wraith_sprite_sheet.get_image( x, 200, 190, 2, BLACK, True))

# Animation list for dark wizard
dark_wizard_animation_list = []
dark_wizard_animation_steps = 8
for x in range(dark_wizard_animation_steps):
     dark_wizard_animation_list.append(dark_wizard_sprite_sheet.get_image( x, 250, 190, 2, BLACK, True))


# Animation list for fire worm
fire_worm_animation_list = []
fire_worm_animation_steps = 16
for x in range(fire_worm_animation_steps):
     fire_worm_animation_list.append(fire_worm_sprite_sheet.get_image( x, 90, 190, 2, BLACK, True))




def draw_bg():
    screen.blit(background_img, (0, 0))

# function for drawing panel
def draw_panel():
    #draw panel rectangle
    screen.blit(panel_img, (0, SCREEN_HEIGHT - BOTTOM_PANEL))


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
        ghoul_frame += 1
        wraith_frame += 1
        d_wizard_frame += 1
        fire_worm_frame += 1

        last_update = current_time
        if ghoul_frame >= len(ghoul_animation_list):
            ghoul_frame = 0
        if wraith_frame >= len(wraith_animation_list):
            wraith_frame = 0
        if d_wizard_frame >= len(dark_wizard_animation_list):
            d_wizard_frame = 0
        if fire_worm_frame >= len(fire_worm_animation_list):
            fire_worm_frame = 0

    screen.blit(wraith_animation_list[wraith_frame], (550, 120))
    screen.blit(ghoul_animation_list[ghoul_frame], (550, 330))
    screen.blit(dark_wizard_animation_list[d_wizard_frame], (750, 150))
    screen.blit(fire_worm_animation_list[fire_worm_frame], (800, 150))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()

