import pygame


class Rocco(object):

    sprite = pygame.image.load("assets/rocco/rocco_still.png")
    state = "still"
    pos_x = 0
    pos_y = 0

    def __init__(self, screen_width, screen_height):
        # save the screen size for use
        self.screen_width = screen_width
        self.screen_height = screen_height

        # save the size of the sprite
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()

    def draw(self, screen):
        if self.state == "still":
            # since we are at still, set the sprite to the middle of the screen
            # by taking half of the screen size and then subtracting half of the
            # length of the current sprite.
            self.pos_x = self.screen_width / 2 - self.width / 2
            self.pos_y = self.screen_height / 2
            screen.blit(self.sprite, (self.pos_x, self.pos_y))

    def touching(self, x, y):
        # check to see if the given position is within the bounds of where the sprite begins and where it ends
        if self.pos_x <= x < (self.pos_x + self.sprite.get_width()):
            if self.pos_y <= y < (self.pos_y + self.sprite.get_height()):
                return True

        return False

    def set_state(self, state):
        self.state = state
