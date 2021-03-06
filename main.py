import pygame
from player import Player
from obstacle import Obstacle
import cv2
import config
from cvzone.HandTrackingModule import HandDetector


class Game:

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode(config.WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.bg = pygame.image.load('./assets/bg.jpg')
        self.font = pygame.font.SysFont("monospace", 30, bold=True)
        self.font_lower = pygame.font.SysFont("monospace", 20, bold=True)

        self.player = Player((config.WINDOW_SIZE[0] / 2, config.WINDOW_SIZE[1] - config.PLAYER_SIZE[1]), config.PLAYER_SIZE,
                             self.display, 0)
        self.obstacle_speed = config.OBSTACLE_SPEED_INIT
        self.obstacles = []

        self.score = 0
        self.running = False
        self.quit = False

    def run(self):
        dt = 0
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)
        detector = HandDetector(detectionCon=0.8, maxHands=1)

        while True:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                success, img = cap.read()
                hands, img = detector.findHands(img)
                if len(hands):
                    self.running = True
                    break
                cv2.imshow("Camera", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                self.display.blit(self.bg, (0, 0))
                welcome_text = self.font_lower.render("Welcome!", True, config.WHITE)
                steer_text = self.font_lower.render("Steer the rocket and avoid asteroids as long as you can!", True, config.WHITE)
                show_text = self.font_lower.render("Show hand to start playing the game!", True, config.WHITE)
                self.display.blit(welcome_text, (config.WINDOW_SIZE[0]/2 - welcome_text.get_size()[0]/2, 220))
                self.display.blit(steer_text, (config.WINDOW_SIZE[0]/2 - steer_text.get_size()[0]/2, 250))
                self.display.blit(show_text, (config.WINDOW_SIZE[0]/2 - show_text.get_size()[0]/2, 280))

                pygame.display.flip()

            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                success, img = cap.read()
                hands, img = detector.findHands(img)

                if len(hands) == 1:
                    current_x = config.WINDOW_SIZE[0] - hands[0]['lmList'][9][0] * 1.5
                    if 0 <= current_x <= config.WINDOW_SIZE[0] - config.PLAYER_SIZE[0]:
                        self.player.x = current_x

                cv2.imshow("Camera", img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

                self.display.blit(self.bg, (0, 0))

                player = self.player.draw()

                score_text = self.font.render("Score = " + str(self.score), True, config.WHITE)
                self.display.blit(score_text, (5, 10))

                for obstacle in self.obstacles:
                    obstacle.draw()
                    obstacle.move(dt)

                    if obstacle.check_collision(player):
                        self.running = False
                        break

                    if (obstacle.y > config.WINDOW_SIZE[1] or obstacle.x < 0
                            or obstacle.x > config.WINDOW_SIZE[0]):
                        self.obstacles.remove(obstacle)
                        self.score += 10
                        if self.score % 100 == 0 and self.score != 0:
                            self.obstacle_speed += config.OBSTACLE_ACCEL

                if len(self.obstacles) < config.MAX_OBSTACLES:
                    for _ in range(len(self.obstacles), config.MAX_OBSTACLES):
                        self.obstacles.append(self.spawn_obstacle())

                pygame.display.flip()
                dt = self.clock.tick(60) / 1000

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                success, img = cap.read()
                hands, img = detector.findHands(img)
                cv2.imshow("Camera", img)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    self.quit = True
                    break
                elif key == ord('r'):
                    self.score = 0
                    self.obstacle_speed = config.OBSTACLE_SPEED_INIT
                    self.obstacles.clear()
                    break

                self.display.blit(self.bg, (0, 0))
                lost_text = self.font_lower.render("You lost! Your points: " + str(self.score), True, config.WHITE)
                commands_text = self.font_lower.render("Click r button to restart or q to quit!", True, config.WHITE)
                self.display.blit(lost_text, (config.WINDOW_SIZE[0]/2 - lost_text.get_size()[0]/2, 220))
                self.display.blit(commands_text, (config.WINDOW_SIZE[0]/2 - commands_text.get_size()[0]/2, 250))

                pygame.display.flip()

            if self.quit:
                pygame.quit()
                break

    def spawn_obstacle(self):
        return Obstacle(config.OBSTACLE_SIZE, self.display, self.obstacle_speed)


game = Game()
game.run()
