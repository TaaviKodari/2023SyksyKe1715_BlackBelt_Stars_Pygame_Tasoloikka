import pygame

class Player(pygame.sprite.Sprite):
    GRAVITY = 0.5  # Adjust this value to change the strength of gravity

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.change_x = 0  # Velocity in the x direction
        self.change_y = 0  # Velocity in the y direction
        self.on_ground = False  # To check if the player is on a platform

    def move_left(self):
        """Set the player's velocity to move left."""
        self.change_x = -5

    def move_right(self):
        """Set the player's velocity to move right."""
        self.change_x = 5

    def stop(self):
        """Stop the player's horizontal movement."""
        self.change_x = 0

    def update(self, platforms):
        """Update the player's position based on velocity and check for collisions."""
        # Apply gravity
        self.change_y += self.GRAVITY
        self.rect.y += self.change_y

        # Check for collisions with platforms
        self.on_ground = False
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for platform in hit_list:
            if self.change_y > 0:
                self.rect.bottom = platform.rect.top
                self.on_ground = True
                self.change_y = 0

        self.rect.x += self.change_x
        hit_list = pygame.sprite.spritecollide(self, platforms, False)
        for platform in hit_list:
            if self.change_x > 0:
                self.rect.right = platform.rect.left
            elif self.change_x < 0:
                self.rect.left = platform.rect.right

    def draw(self, screen, camera):
        """Draw the player on the screen, adjusted for the camera's position."""
        screen.blit(self.image, camera.apply(self))
