import pygame
from player import Player
from obstacle import Obstacle
import random
import cv2
import colors
from cvzone.HandTrackingModule import HandDetector


class Game:
    PLAYER_SPEED = 300
    PLAYER_SIZE = (50, 100)
    OBSTACLE_SIZE = 40
    WINDOW_SIZE = (960, 720)
    MAX_OBSTACLES = 3
    OBSTACLE_SPEED_RANGE = (100, 300)

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(self.WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load('./assets/bg.jpg')
        self.font = pygame.font.SysFont("monospace", 30, bold=True)

        self.player = Player((self.WINDOW_SIZE[0] / 2, self.WINDOW_SIZE[1] - self.PLAYER_SIZE[1]), self.PLAYER_SIZE,
                             self.display, 0)
        self.obstacles = [self.spawn_obstacle()]
        self.score = 0

        self.running = True

    def run(self):
        dt = 1
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        detector = HandDetector(detectionCon=0.8, maxHands=1)

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            success, img = cap.read()
            hands, img = detector.findHands(img)

            if len(hands) == 1:
                current_x = self.WINDOW_SIZE[0] - hands[0]['lmList'][9][0] * 1.5
                if 0 <= current_x <= self.WINDOW_SIZE[0] - self.PLAYER_SIZE[0]:
                    self.player.x = current_x

            cv2.imshow("Camera", img)

            self.display.blit(self.bg, (0, 0))

            player = self.player.draw()

            score_text = self.font.render("Score = " + str(self.score), True, colors.WHITE)
            self.display.blit(score_text, (5, 10))

            for obstacle in self.obstacles:
                obstacle.draw()
                obstacle.move(dt)

                if obstacle.check_collision(player):
                    self.running = False

                if (obstacle.y > self.WINDOW_SIZE[1] or obstacle.x < 0
                        or obstacle.x > self.WINDOW_SIZE[0]):
                    self.obstacles.remove(obstacle)
                    self.score += 10

            if len(self.obstacles) < self.MAX_OBSTACLES:
                for _ in range(len(self.obstacles), self.MAX_OBSTACLES):
                    self.obstacles.append(self.spawn_obstacle())

            pygame.display.flip()
            dt = self.clock.tick(60) / 1000

        pygame.quit()

    def spawn_obstacle(self):
        return Obstacle(self.OBSTACLE_SIZE, self.display,
                        random.randrange(self.OBSTACLE_SPEED_RANGE[0], self.OBSTACLE_SPEED_RANGE[1]))


game = Game()
game.run()
