import pygame

pygame.init()
clock = pygame.time.Clock()
fps = 60

BOTTOM_PANEL = 200
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500 + BOTTOM_PANEL

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dungeons and the Ur-Dragon")
running = True

# Load background and characters
background_img = pygame.image.load("../Images/Background/Eerie Cave Background1.png").convert_alpha()
background_img = pygame.transform.scale(background_img, (SCREEN_WIDTH, SCREEN_HEIGHT - BOTTOM_PANEL))


def draw_bg():
    screen.blit(background_img, (0, 0))

def draw_menu_action():

    border_rect = pygame.Rect(130, 585, 585, 130)
    border_rect.center = (SCREEN_WIDTH -900, SCREEN_HEIGHT - BOTTOM_PANEL / 2)
    pygame.draw.rect(screen, (184,10,203), border_rect)

    rect = pygame.Rect(120, 575, 575, 120)
    rect.center = (SCREEN_WIDTH - 900, SCREEN_HEIGHT - BOTTOM_PANEL / 2)
    pygame.draw.rect(screen, (83,143,229), rect)


def draw_menu_options():

    border_rect = pygame.Rect(130, 585, 585, 130)
    border_rect.center = (SCREEN_WIDTH - 305, SCREEN_HEIGHT - BOTTOM_PANEL / 2)
    pygame.draw.rect(screen, (184,10,203), border_rect)

    rect = pygame.Rect(120, 575, 575, 120)
    rect.center = (SCREEN_WIDTH - 305, SCREEN_HEIGHT - BOTTOM_PANEL / 2)
    pygame.draw.rect(screen, (83,143,229), rect)


while running:
    clock.tick(fps)

    # Draw background
    draw_bg()
    #  Draw allies menu box
    draw_menu_action()
    # Draw enemies menu box
    draw_menu_options()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()

