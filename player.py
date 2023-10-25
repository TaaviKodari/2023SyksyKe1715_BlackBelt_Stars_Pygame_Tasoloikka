import pygame

class Player(pygame.sprite.Sprite):
    GRAVITY = 0  # Adjust this value to change the strength of gravity

    def __init__(self, pos, frames):
        super().__init__()
        self.frames = frames
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect(center=pos)
        self.change_x = 0  # Velocity in the x direction
        self.change_y = 0  # Velocity in the y direction
        self.on_ground = False  # To check if the player is on a platform
        #self.platforms = platforms  # Platforms for collision checking
        self.animation_time = 0.1  # Time (in seconds) for each frame
        self.current_time = 0

    def move_left(self):
        """Set the player's velocity to move left."""
        self.change_x = -5

    def move_right(self):
        """Set the player's velocity to move right."""
        self.change_x = 5

    def stop(self):
        """Stop the player's horizontal movement."""
        self.change_x = 0

    def update(self, dt):
        """Update the player's position based on velocity and check for collisions."""
        # Apply gravity
        self.change_y += self.GRAVITY
        self.rect.y += self.change_y

        # Check for collisions with platforms
        self.on_ground = False
        #hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        #for platform in hit_list:
         #   if self.change_y > 0:
          #      self.rect.bottom = platform.rect.top
           #     self.on_ground = True
            #    self.change_y = 0

        self.rect.x += self.change_x
        #hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        #for platform in hit_list:
         #   if self.change_x > 0:
          #      self.rect.right = platform.rect.left
           # elif self.change_x < 0:
            #    self.rect.left = platform.rect.right

        # Animation logic
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]
