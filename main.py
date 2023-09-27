import pygame
from player import Player  # Import the Player class

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("2D Platformer")

# Create a player instance
player = Player()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the player
    player.update()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    pygame.draw.rect(screen, (255, 0, 0), player.rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
