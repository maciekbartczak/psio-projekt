import pygame
import random

pygame.init()

width, height = 1000, 800

obstacle_size = 50;
obstacle_speed = 5;
player_speed = 0;

obstacle_x = random.randrange(0, width)
obstacle_y = -50

player_x = 475

display = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

def draw_rect(display, x, y, size, color):
    pygame.draw.rect(display, color, [x, y, size, size])

while True:
    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player_speed = -5
            if event.key == pygame.K_d:
                player_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player_speed = 0

    display.fill((255, 255, 255))
    draw_rect(display, obstacle_x, obstacle_y, obstacle_size, (255, 0, 0))
    draw_rect(display, player_x, height - obstacle_size, obstacle_size, (0, 0, 255))

    obstacle_y += obstacle_speed
    
    if player_x + player_speed >= 0 and player_x + player_speed + obstacle_size <= width:
        player_x += player_speed

    if obstacle_y > height:
        obstacle_y = -50
        obstacle_x = random.randrange(0, width)
    
    pygame.display.flip()
    clock.tick(60)