import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()  # Blank surface
        # Blit( image, coord on the surface, area from the spreadsheet
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))

        # Scale the image
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image

