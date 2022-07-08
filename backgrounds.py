import pygame
from pygame import mixer
from pipes import Pipe
class BackGround:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Background image - day
        self.bg_image = pygame.image.load('assets/background-day.png').convert()
        self.background = pygame.transform.scale(self.bg_image, (400, 600))
        self.background_rect = self.background.get_rect()


        # floor image
        self.floor_image1 = pygame.image.load('assets/base.png').convert()
        self.floor_image2 = pygame.image.load('assets/base.png').convert()

        self.floor_bg1 = pygame.transform.scale(self.floor_image1, (400, 112))
        self.floor_bg2 = pygame.transform.scale(self.floor_image2, (400, 112))

        self.floor_rect1 = self.floor_bg1.get_rect()
        self.floor_rect2 = self.floor_bg2.get_rect()

        self.floor_rect1.bottom = self.screen_rect.bottom
        self.floor_rect2.bottomleft = self.floor_rect1.bottomright

        # floor
        self.floor_list = [self.floor_rect1, self.floor_rect2]
        # pipes
        self.pipe = Pipe(self)


        self.game_beat = mixer.music.load('sound/sfx_swooshing.wav')

        self.start_screen = pygame.transform.scale(pygame.image.load('assets/gameover.png').convert(), (400, 600))
        self.start_screen_rect = self.start_screen.get_rect()

        self.end_image = pygame.image.load('assets/gameover.png').convert()
        self.end_screen = pygame.transform.scale(self.end_image, (200, 50))
        self.end_screen_rect = self.end_screen.get_rect()

    def draw_background(self):
        self.screen.blit(self.background, self.background_rect)

    def draw_floor(self):
        self.screen.blit(self.floor_bg1, self.floor_rect1)
        self.screen.blit(self.floor_bg2, self.floor_rect2)

    def floor_movement(self):
        self.floor_rect1.x -= 1
        self.floor_rect2.x -= 1
        x = int(self.floor_rect1.x) + 395
        y = int(self.floor_rect2.x) + 395
        if x < 0:
            self.floor_rect1.x = 400
            print("deleted 1")
        if y < 0:
            self.floor_rect2.x = 400
            print("deleted 2")

    def background_mechanics(self):
        self.draw_background()
        self.pipe.draw_pipe()
        self.pipe.move_pipes()
        self.draw_floor()
        self.floor_movement()


