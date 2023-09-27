import pygame
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(self.width / 2)
        y = -target.rect.centery + int(self.height / 2)

        # Keep the camera within the bounds of the level (if you have level boundaries)
        # x = min(0, x)
        # y = min(0, y)
        # x = max(-(self.level_width - self.width), x)
        # y = max(-(self.level_height - self.height), y)

        self.camera = pygame.Rect(x, y, self.width, self.height)
