import pygame

WHITE = (255, 255, 255)
pygame.init()
clock=pygame.tick.Clock()
time=pygame.time.get_ticks()


class SpriteSheet:
    sprites = []

    def __init__(self, image):
        self.time = 0
        self.delay = 500
        self.count = 0
        self.sheet = pygame.image.load(image).convert_alpha()

    def get_image(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height))
        image.fill(color)
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        return image

    def load(self, start, end):
        for i in range(0, 6):
            self.sprites.append(self.get_image(self.count, 100, 100, 0.5, (255,255,255)))
        print(len(self.sprites))

    def animate(self):
        currentTime = pygame.time.get_ticks()
        # debounce logic
        if currentTime - self.time > self.delay:
            self.time = currentTime
            self.count += 1
            if self.count >= len(self.sprites):
                self.count = 0

    def draw(self, image):
        self.animate()





