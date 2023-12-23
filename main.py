# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

#game window
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
icon = pygame.image.load("assets/rocco/rocco_still.png")
icon = pygame.transform.scale(icon, (32, 16.84))

# Set the window title and icon
pygame.display.set_caption("Rocco")
pygame.display.set_icon(icon)

# Set up Rocco NPC
rocco = pygame.image.load("assets/rocco/rocco_still.png")
rocco = pygame.transform.scale(rocco, (57,30))

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw rocco in the center
    screen.blit(rocco, (220, 250))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()