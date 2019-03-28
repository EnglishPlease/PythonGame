import pygame
import config
from GameObject import GameObject

class Paddle(GameObject):
    def __init__(self, x, y, width, height, color, offset):
        GameObject.__init__(self, x, y, width, height)
        self.color = color
        self.offset = offset
        self.moving_left = False
        self.moving_right = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def handle(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = not self.moving_left
        else:
            self.moving_right = not self.moving_right

    def update(self):
        if self.moving_left:
            dx = -(min(self.offset, self.left))
        elif self.moving_right:
            dx = min(self.offset, config.screen_width - self.right)
        else:
            return

        self.move(dx, 0)
