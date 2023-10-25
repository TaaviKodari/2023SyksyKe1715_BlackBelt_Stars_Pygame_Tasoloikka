import pygame
from platform import Platform

class Level:
    def __init__(self):
        """Constructor for the level."""
        self.platforms = pygame.sprite.Group()

    def update(self):
        """Update everything in this level."""
        self.platforms.update()

    def draw(self, screen, camera):
        """Draw everything on this level."""
        for platform in self.platforms:
            screen.blit(platform.image, camera.apply(platform))

    # You can add more methods to add enemies, items, etc.

class Level_01(Level):
    def __init__(self):
        super().__init__()

        # Define level layout
        # You can add more platforms or other elements specific to this level
        ground = Platform(0, 550, 800, 50)
        platform1 = Platform(200, 400, 150, 30)
        platform2 = Platform(400, 300, 150, 30)

        self.platforms.add(ground, platform1, platform2)
