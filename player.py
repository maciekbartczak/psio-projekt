import pygame
import colors

class Player:
    def __init__(self, pos, size, display, speed):
        self.x, self.y = pos
        self.size = size
        self.display = display
        self.speed = speed

    def draw(self):
        return pygame.draw.rect(self.display, colors.BLUE, [self.x, self.y, self.size, self.size])

    def move(self):
        offset = self.speed
        w, _ = self.display.get_size()
        remaining_x_left = self.x
        remaining_x_right = w - (self.x + self.size)
        if offset < 0:
            if offset > remaining_x_left:
                offset = -remaining_x_left
        else:
            if offset > remaining_x_right:
                offset = remaining_x_right
        self.x += offset