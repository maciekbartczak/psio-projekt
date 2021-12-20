import pygame
import random

pygame.init()

width, height = 1000, 800

obstacle_size = 50;
obstacle_speed = 10;

obstacle_x = random.randrange(0, width)
obstacle_y = -50

display = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

def draw_obstacle(display, x, y, size):
    pygame.draw.rect(display, (0, 0, 0), [x, y, size, size])

while True:
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill((255, 255, 255))
    draw_obstacle(display, obstacle_x, obstacle_y, obstacle_size)

    obstacle_y += obstacle_speed

    if obstacle_y > height:
        obstacle_y = -50
        obstacle_x = random.randrange(0, width)
    
    pygame.display.flip()
    clock.tick(60)