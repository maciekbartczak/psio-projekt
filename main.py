import pygame

pygame.init()

width, height = 800, 600

display = pygame.display.set_mode((width, height))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    display.fill((255, 255, 255))
    
    pygame.display.update()