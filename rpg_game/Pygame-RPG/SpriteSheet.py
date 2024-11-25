import os

import pygame
pygame.init()

"""
    Parameter:
    image: A single sprite sheet image (optional). This would typically be a pygame.Surface object.
    images_folder: A folder containing separate images (optional), in case the animations aren't in a single sprite sheet.

    Attributes:
        self.sheet: Stores the provided sprite sheet image (or None if not given).
        self.images_folder: Stores the path to a folder containing individual images (if applicable).
        self.is_sprite_sheet: A boolean indicating if a sprite sheet is provided (True if image is not None).
        self.frames: An empty list intended to store individual frames extracted from the sprite sheet.
"""
class SpriteSheet:
    def __init__(self, image = None, images_folder=None):
        self.sheet = image
        self.images_folder = images_folder
        self.is_sprite_sheet = image is not None
        self.frames = []

    """
    Parameters:
        frame: The index of the frame to extract (starting from 0).
        width: The width of each frame in the sprite sheet.
        height: The height of each frame in the sprite sheet.
        scale: A scaling factor to resize the frame.
        color: A color that should be treated as transparent in the frame (set as the "colorkey").
        flip: A boolean indicating whether the frame should be flipped horizontally.
    """
    # Get frames out of a single spreadsheet
    def get_image(self, frame, width, height, scale, color, flip=False):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))

        image = pygame.transform.scale(image, (width * scale, height * scale))

        if flip:
            image = pygame.transform.flip(image, True, False)
        image.set_colorkey(color)

        return image

    def get_frames(self, file_path, width, height, scale, color, flip=False):
        frames = []
        images = sorted(os.listdir(self.images_folder))  # Removed file_path; using self.images_folder directly

        if not images:
            print(f"No images found in {self.images_folder}")
            return frames

        for image_file in images:
            img = pygame.image.load(os.path.join(self.images_folder, image_file)).convert_alpha()
            img = pygame.transform.scale(img, (width * scale, height * scale))
            img.set_colorkey(color)
            if flip:
                img = pygame.transform.flip(img, True, False)
            frames.append(img)

        return frames
