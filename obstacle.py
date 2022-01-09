import pygame
import random


class Obstacle:
    offset = [1, -1]

    def __init__(self, size, display, speed):
        self.x = random.randrange(0, display.get_size()[0] - size)
        self.y = 0 - size
        self.size = size
        self.display = display
        self.speed = speed
        self.rect = None
        self.image = pygame.transform.scale(pygame.image.load('./assets/asteroid.png'), (self.size, self.size))
        self.rect = None
        self.direction = random.choice(self.offset)

    def draw(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.display.blit(self.image, self.rect)

    def move(self, dt):
        self.y += self.speed * dt
        self.x += self.direction * (self.speed // 6) * dt

    def check_collision(self, player_rect):
        return self.rect.colliderect(player_rect) if self.rect else False
