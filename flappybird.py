import pygame
import sys
import pygame.time
from pygame import mixer


from bird import Bird
from backgrounds import BackGround
from pipes import Pipe
# pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
pygame.init()
clock = pygame.time.Clock()

class FlappyBird(object):
    def __init__(self):
        self.screen = pygame.display.set_mode((400, 600))
        self.screen_rect = self.screen.get_rect()
        self.birb = Bird(self)
        self.bg = BackGround(self)
        # self.p = Pipe(self)
        self.i = 2
        self.collision = False
        self.flap_beat = mixer.Sound('sound/sfx_wing.wav')
        self.hit_sound = mixer.Sound('sound/sfx_hit.wav')

        
        self.game_stat = True

    def run_game(self):
        while True:
            if self.game_stat == True:
                self.bg.background_mechanics()
                # self.p.draw_pipe()

                self.birb.draw_bird(self.i)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.flap_beat.play()
                            self.birb.gravity = False
                            self.i = 0
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            self.birb.gravity = True
                            self.i = 1
                    # if event.type == pygame.KEYUP:
                    #     if event.key == pygame.K_SPACE:
                    #         self.birb.gravity = True

                self.birb.bird_movement()
                if self.check_collision():
                    self.hit_sound.play()
                    self.game_stat = False

                clock.tick(120)
                pygame.display.flip()

            if self.game_stat == False:
                self.draw_gameover_screen()
                self.birb.bird_rect.center = (90, 300)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            self.game_stat = True

                pygame.display.flip()

    def game_score(self):
        pass

    def draw_welcome_screen(self):
        self.screen.blit(self.bg.start_screen, self.bg.start_screen_rect)

    def draw_gameover_screen(self):
        self.screen.blit(self.bg.end_screen, self.bg.end_screen_rect)

    def check_collision_bird_pipe(self):
        for pipe in self.bg.pipe.pipe_list:
            if self.birb.bird_rect.colliderect(pipe):
                return True

    def check_col_bird_floor(self):
        for floor in self.bg.floor_list:
            if self.birb.bird_rect.colliderect(floor):
                  return True

    def check_collision(self):
        if self.check_collision_bird_pipe():
            return True
        if self.check_col_bird_floor():
            return True
        if self.birb.bird_rect.y < 0:
            return True

    def reset_game(self):
        self.bg.background_mechanics()
        self.draw_welcome_screen()
        pygame.display.flip()
        self.game_stat = True

if __name__ == '__main__':
    fl = FlappyBird()
    fl.run_game()
