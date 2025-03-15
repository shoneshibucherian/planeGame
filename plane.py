import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 700, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Cannon settings
cannon_width = 200
cannon_height = 30
cannon_x, cannon_y = 300, 430
projectiles = []

# Meteor settings
meteors = []
meteor_spawn_delay = 30  # Frames between new meteor spawns
meteor_speed = 5

# Game loop variables
clock = pygame.time.Clock()
gameOn = True
frame_count = 0

while gameOn:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOn = False
        
        # Fire a projectile
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                projectiles.append([cannon_x + cannon_width // 2, cannon_y])  # From cannon center

    # Move cannon with arrow keys
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and cannon_x > 0:
        cannon_x -= 5
    if keys[K_RIGHT] and cannon_x + cannon_width < WIDTH:
        cannon_x += 5

    # Clear screen
    screen.fill((0,0,0))

    # Draw cannon
    pygame.draw.rect(screen, BLUE, (cannon_x, cannon_y, cannon_width, cannon_height))
    pygame.draw.circle(screen, GREEN, (cannon_x + cannon_width // 2, cannon_y), 30)

    # Move and draw projectiles
    for projectile in projectiles:
        projectile[1] -= 10  # Move upward
        pygame.draw.rect(screen, GREEN, (*projectile, 10, 10))

    # Remove off-screen projectiles
    projectiles = [p for p in projectiles if p[1] > 0]

    # Spawn meteors at random
    if frame_count % meteor_spawn_delay == 0:
        meteor_x = random.randint(0, WIDTH - 40)  # Random x position
        meteors.append([meteor_x, 0])  # Start at the top

    # Move and draw meteors
    for meteor in meteors:
        meteor[1] += meteor_speed  # Move downward
        pygame.draw.circle(screen, RED, (meteor[0], meteor[1]), 20)

    # Remove off-screen meteors
    meteors = [m for m in meteors if m[1] < HEIGHT]

    # Check for collisions (meteors and projectiles)
    for meteor in meteors[:]:
        for projectile in projectiles[:]:
            # Collision detection
            if abs(meteor[0] - projectile[0]) < 20 and abs(meteor[1] - projectile[1]) < 20:
                meteors.remove(meteor)
                projectiles.remove(projectile)
                break

    # Check if any meteor hits the cannon
    for meteor in meteors:
        if cannon_y < meteor[1] + 20 and abs(meteor[0] - (cannon_x + cannon_width // 2)) < 100:
            gameOn = False  # End the game

    # Update display and frame count
    pygame.display.flip()
    clock.tick(30)
    frame_count += 1

# Game Over Screen
screen.fill(WHITE)
font = pygame.font.SysFont(None, 55)
game_over_text = font.render("Game Over!", True, RED)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 30))
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
