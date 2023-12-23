# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

# game window
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
rocco = pygame.transform.scale(rocco, (200, 100))

# Set up Player NPC
hand = pygame.image.load("assets/player/cursor_hover.png")
hand = pygame.transform.scale(hand, (57, 57))
hand = pygame.cursors.Cursor((20, 20), hand)
pygame.mouse.set_cursor(hand)
pygame.mouse.set_visible(True)

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
    screen.blit(rocco, ((250 - rocco.get_width()/2), 250))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
