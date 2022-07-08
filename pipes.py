import pygame
import random


class Pipe(object):
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()


        # random position of pipes
        self.y = random.randint(-100, 60)
        # self.size_u1 = self.size_l1 - 160 - 200
        # self.size_l2 = random.choice([330, 390, 450, 510, 570, 600])
        # self.size_u2 = self.size_l2 - 160 - 200

        # lower pipes
        self.lower_pipe_image1 = pygame.image.load('assets/pipe-green.png').convert()
        self.lower_pipe_rect1 = self.lower_pipe_image1.get_rect()
        self.lower_pipe_rect1.center = (450, 480)

        self.lower_pipe_image2 = pygame.image.load('assets/pipe-green.png').convert()
        self.lower_pipe_rect2 = self.lower_pipe_image2.get_rect()
        self.lower_pipe_rect2.center = (670, 370)


        # upper pipes
        self.upper_pipe_image1 = pygame.image.load('assets/pipe-green.png').convert()
        self.upper_pipe_image1 = pygame.transform.flip(self.upper_pipe_image1, False, True)
        self.upper_pipe_rect1 = self.upper_pipe_image1.get_rect()
        self.upper_pipe_rect1.center = (450, -160)

        self.upper_pipe_image2 = pygame.image.load('assets/pipe-green.png').convert()
        self.upper_pipe_image2 = pygame.transform.flip(self.upper_pipe_image2, False, True)
        self.upper_pipe_rect2 = self.upper_pipe_image1.get_rect()
        self.upper_pipe_rect2.center = (670, -170)

        self.pipe_list = [self.lower_pipe_rect1, self.lower_pipe_rect2, self.upper_pipe_rect1, self.upper_pipe_rect2]

    def draw_pipe(self):
        self.screen.blit(self.lower_pipe_image1, self.lower_pipe_rect1)
        self.screen.blit(self.lower_pipe_image2, self.lower_pipe_rect2)
        # self.screen.blit(self.upper_pipe_image, self.upper_pipe_rect)
        self.screen.blit(self.upper_pipe_image1, self.upper_pipe_rect1)
        self.screen.blit(self.upper_pipe_image2, self.upper_pipe_rect2)

    def move_pipes(self):
        self.lower_pipe_rect1.x -= 2
        self.upper_pipe_rect1.x -= 2
        self.lower_pipe_rect2.x -= 2
        self.upper_pipe_rect2.x -= 2
        # self.upper_pipe_rect.x -= 1
        # x = (self.lower_pipe_rect.topright)

        # random position of pipes
        # self.size_l1 = random.choice([330, 390, 450, 510, 570, 600])
        # self.size_u1 = self.size_l1 - 160 - 200
        # self.size_l2 = random.choice([330, 390, 450, 510, 570, 600])
        # self.size_u2 = self.size_l2 - 160 - 200
        y = random.choice([-140, -100, -60, 0, 60, 100])
        x = y + 480
        if (self.upper_pipe_rect1.centerx + 53) < 0:
            self.upper_pipe_rect1.center = (450, y)
        if (self.lower_pipe_rect1.centerx + 53) < 0:
            self.lower_pipe_rect1.center = (450, x)

        y1 = random.choice([-140, -100, -60, 0, 60, 100])
        x1 = y1 + 480
        if (self.upper_pipe_rect2.centerx + 53) < 0:
            self.upper_pipe_rect2.center = (450, y1)
        if (self.lower_pipe_rect2.centerx + 53) < 0:
            self.lower_pipe_rect2.center = (450, x1)
