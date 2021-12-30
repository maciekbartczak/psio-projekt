import pygame
import colors

class Player:
    def __init__(self, pos, size, display, speed):
        self.x, self.y = pos
        self.size = size
        self.display = display
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load('./assets/rocket.png'), self.size)

    def draw(self):
        rect = self.image.get_rect()
        rect.topleft = self.x, self.y
        self.display.blit(self.image, rect)
        return rect

    def move(self, dt):
        offset = self.speed * dt
        w, _ = self.display.get_size()
        remaining_x_left = self.x
        remaining_x_right = w - (self.x + self.size[0])
        if offset < 0:
            if offset > remaining_x_left:
                offset = -remaining_x_left
        else:
            if offset > remaining_x_right:
                offset = remaining_x_right
        self.x += offset