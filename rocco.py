import pygame


class Rocco(object):
    sprite = pygame.image.load("assets/rocco/rocco_still.png")

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]  # This will define where our enemy starts and finishes their path.
        self.walkCount = 0
        self.vel = 3
