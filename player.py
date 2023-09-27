import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((32, 32))  # Replace with player sprite
        self.image.fill((255, 0, 0))  # Replace with player sprite
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)  # Initial spawn point

        # Player attributes
        self.speed = 5  # Movement speed
        self.jump_power = -10  # Jump strength
        self.gravity = 0.5  # Gravity value
        self.is_jumping = False
        self.is_running = False
        self.y_velocity = 0  # Vertical velocity

    def update(self):
        # Handle player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Handle jumping
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True
            self.y_velocity = self.jump_power
        else:
            self.y_velocity += self.gravity

        # Update player's vertical position
        self.rect.y += self.y_velocity

        # Ground collision (adjust based on your ground level)
        if self.rect.y > 400:  # Replace with your ground level
            self.rect.y = 400
            self.is_jumping = False
            self.y_velocity = 0

        # Handle running
        if keys[pygame.K_LSHIFT]:
            self.is_running = True
            self.speed = 10  # Adjust the running speed
        else:
            self.is_running = False
            self.speed = 5  # Reset to normal speed
