import pygame
from GameObject import GameObject

class Brick(GameObject):
    def __init__(self, x, y, width, height, color):
        GameObject.__init__(self, x, y, width, height)
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)
