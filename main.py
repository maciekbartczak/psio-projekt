import pygame
from player import Player
from obstacle import Obstacle
import random
import cv2
from cvzone.HandTrackingModule import HandDetector

class Game:
    PLAYER_SPEED = 300
    PLAYER_SIZE = (50, 100)
    OBSTACLE_SIZE = 40
    WINDOW_SIZE = (1000, 800)
    MAX_OBSTACLES = 3
    OBSTACLE_SPEED_RANGE = (100, 300)

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load('./assets/bg.jpg')

        self.player = Player((475, self.WINDOW_SIZE[1] - self.PLAYER_SIZE[1]), self.PLAYER_SIZE, self.display, 0)
        self.obstacles = [self.spawn_obstacle()]

        self.running = True

    def run(self):
        dt = 1

        cap = cv2.VideoCapture(0)
        detector = HandDetector(detectionCon=0.8, maxHands=2)

        while self.running:

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


            success, img = cap.read()
            hands, img = detector.findHands(img)

            if len(hands) == 1:
                if hands[0]["type"] == "Left":
                    self.player.speed = -self.PLAYER_SPEED
                elif hands[0]["type"] == "Right":
                    self.player.speed = self.PLAYER_SPEED
            else:
                self.player.speed = 0

            cv2.imshow("Camera", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            self.display.blit(self.bg, (0, 0))

            player = self.player.draw()
            
            for obstacle in self.obstacles:
                obstacle.draw()
                obstacle.move(dt)

                if obstacle.check_collision(player):
                    self.running = False

                if (obstacle.y > self.WINDOW_SIZE[1] 
                    or obstacle.x < 0 
                    or obstacle.x > self.WINDOW_SIZE[0]):
                        self.obstacles.remove(obstacle)

            if len(self.obstacles) < self.MAX_OBSTACLES:
                for _ in range(len(self.obstacles), self.MAX_OBSTACLES):
                    self.obstacles.append(self.spawn_obstacle())

            self.player.move(dt)

            pygame.display.flip()
            print(dt)
            dt = self.clock.tick(60) / 1000
            
        pygame.quit()
    
    def spawn_obstacle(self):
        return Obstacle(self.OBSTACLE_SIZE, self.display, random.randrange(self.OBSTACLE_SPEED_RANGE[0],self.OBSTACLE_SPEED_RANGE[1]))


game = Game()
game.run()


