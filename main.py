import pygame
from player import Player
from camera import Camera
from platform_1 import Platform

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)

# Screen and clock setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("2D Platformer")
clock = pygame.time.Clock()

# Create player and camera
player = Player()
camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
platforms = pygame.sprite.Group()
ground = Platform(0,SCREEN_HEIGHT -50, SCREEN_WIDTH,50)
platforms.add(ground)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.stop()

    # Update
    player.update(platforms)
    camera.update(player)

    # Draw
    screen.fill(WHITE)
    player.draw(screen, camera)

    for platform in platforms:
        screen.blit(platform.image, camera.apply(platform))
    # Draw other game objects here...

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
