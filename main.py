import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5

# Colors
WHITE = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('2D Platformer')

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((SCREEN_WIDTH, 50))  # Width of screen and height of 50 pixels
        self.image.fill((50, 168, 82))  # A green color for the ground
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT  # Position the ground at the bottom of the screen


class Player(pygame.sprite.Sprite):
    def __init__(self, spritesheet_path):
        super().__init__()
        self.spritesheet = pygame.image.load(spritesheet_path).convert_alpha()
        self.frame_index = 0
        self.frame_delay = 5  # Adjust this for faster/slower animation
        self.frame_timer = 0  # Initialize frame_timer here
        self.image = self.get_image(0)  # Start with the idle frame
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.moving = False
        # Apply gravity
        self.vel_y = 0  # Vertical velocity
        self.gravity = 1  # Gravity strength, adjust as needed


    def get_image(self, frame_index):
        """Extracts a single sprite from the spritesheet."""
        width = 48
        height = 48
        image = pygame.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (frame_index * width, 0, width, height))
        image.set_colorkey((0,0,0))
        return image.convert_alpha()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= PLAYER_SPEED
            self.moving = True
        elif keys[K_RIGHT]:
            self.rect.x += PLAYER_SPEED
            self.moving = True
        else:
            self.moving = False

      # Update the sprite based on movement
        if self.moving:
            self.frame_timer += 1
            if self.frame_timer > self.frame_delay:
                self.frame_timer = 0
                self.frame_index = (self.frame_index + 1) % 8  # Loop through 8 frames
            self.image = self.get_image(self.frame_index)
        else:
            self.image = self.get_image(0)  # Idle frame
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        if self.rect.bottom > SCREEN_HEIGHT - 50:  # 50 is the height of the ground
            self.rect.bottom = SCREEN_HEIGHT - 50
            self.vel_y = 0  # Reset vertical velocity when on the ground


def main():
    clock = pygame.time.Clock()
    player = Player('Sprites\Asset Packs 1-3 (final)\Asset Pack-V3\PlayerWalk\PlayerWalk 48x48.png')
    ground = Ground()
    all_sprites = pygame.sprite.Group(player, ground)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        all_sprites.update()

        screen.fill(WHITE)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
