import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Cannon settings
cannon_width = 200
cannon_height = 30
cannon_x, cannon_y = 100, 330
angle = 0

# Projectile list
projectiles = []

# Game loop
gameOn = True
while gameOn:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
        
        # Fire a projectile with space bar
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                projectiles.append([cannon_x + cannon_width // 2, cannon_y])  # Center of rectangle

    # Get key presses for movement
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        cannon_x -= 0.5  # Move left
    if keys[K_RIGHT]:
        cannon_x += 0.5  # Move right
    if keys[K_UP]:
        cannon_y -= 0.5  # Move up
    if keys[K_DOWN]:
        cannon_y += 0.5  # Move down

    # Clear screen
    screen.fill((0,0,0))

    # Draw the cannon
    pygame.draw.rect(screen, BLUE, (cannon_x, cannon_y, cannon_width, cannon_height))  # Cannon base
    pygame.draw.circle(screen, GREEN, (cannon_x + cannon_width // 2, cannon_y), 30)  # Cannon head


    # Move and draw projectiles
    for projectile in projectiles:
        projectile[1] -= 0.5  # Move upward
        pygame.draw.rect(screen, GREEN, (*projectile, 10, 10))  # Draw projectile
    
    # Remove off-screen projectiles
    projectiles = [p for p in projectiles if p[1] > 0]

    # Update display
    pygame.display.flip()

pygame.quit()
