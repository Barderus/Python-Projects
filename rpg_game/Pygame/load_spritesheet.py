import pygame
from spritesheet import SpriteSheet

pygame.init()

BOTTOM_PANEL = 200
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500 + BOTTOM_PANEL
BLACK = (0, 0, 0)
GRAYISH = (50, 50, 50)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheet')

ghoul_atk_img = pygame.image.load("../Images/Characters/2 - Row/Ghoul/Attack/Attack1.png").convert_alpha()
sprite_sheet = SpriteSheet(ghoul_atk_img)

# Animation list
animation_list = []
animation_steps = 11
last_update = pygame.time.get_ticks()
animation_cooldown = 75 # 75ms
frame = 0

for x in range(animation_steps):
    animation_list.append(sprite_sheet.get_image( x, 144, 110, 2, GRAYISH))



run = True
while run:
    screen.fill(BLACK)
    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0


    screen.blit(animation_list[frame], (600, 0))
    pygame.display.update()


    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()