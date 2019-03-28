import pygame
from GameObject import GameObject

class Ball(GameObject):
    def __init__(self, x, y, radius, color, speed):
        GameObject.__init__(self, x - radius, y - radius, radius * 2, radius * 2, speed)
        self.radius = radius
        self.diameter = radius * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius)

    def update(self):
        super().update()
