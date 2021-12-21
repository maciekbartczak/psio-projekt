import pygame
from player import Player
from obstacle import Obstacle


class Game:
    PLAYER_SPEED = 10
    OBSTACLE_SPEED = 10
    PLAYER_SIZE = 50
    OBSTACLE_SIZE = 50
    WINDOW_SIZE = (1000, 800)

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.player = Player((475, self.WINDOW_SIZE[1] - self.PLAYER_SIZE), self.PLAYER_SIZE, self.display, 0)
        self.obstacle = Obstacle(self.OBSTACLE_SIZE, self.display, self.OBSTACLE_SPEED)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.player.speed = -self.PLAYER_SPEED
                    if event.key == pygame.K_d:
                        self.player.speed = self.PLAYER_SPEED
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a or event.key == pygame.K_d:
                        self.player.speed = 0

            self.display.fill((255, 255, 255))
            player = self.player.draw()
            self.obstacle.draw()

            self.obstacle.move()
            self.player.move()

            if self.obstacle.y > self.WINDOW_SIZE[1]:
                self.obstacle = Obstacle(self.OBSTACLE_SIZE, self.display, self.OBSTACLE_SPEED)
            
            if self.obstacle.check_collision(player):
                pygame.quit()

            pygame.display.flip()
            self.clock.tick(60)

game = Game()
game.run()


