import pygame
from GameObject import GameObject
from TextObject import TextObject
import config

class Button(GameObject):
    def __init__(self, x, y, w, h, text, on_click = lambda x: None, padding = 0):
        super().__init__(x, y, w, h)
        self.state = 'normal'
        self.on_click = on_click
        self.text = TextObject(x + padding, y + padding, lambda: text, config.button_text_color, config.font_name, config.font_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.back_color, self.bounds)
        self.text.draw(surface)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.bounds.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.bounds.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'

    @property
    def back_color(self):
        return dict(normal = config.button_normal_back_color, hover = config.button_hover_back_color, pressed = config.button_pressed_back_color)[self.state]
