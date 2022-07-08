import pygame

class Bird:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.bird_image1 = pygame.image.load('assets/redbird-upflap.png').convert()
        self.bird_image2 = pygame.image.load('assets/yellowbird-downflap.png').convert()
        self.bird_image3 = pygame.image.load('assets/bluebird-midflap.png').convert()

        self.bird_rect = self.bird_image3.get_rect()
        self.bird_rect.center = (90, 300)

        self.bird_list = [self.bird_image1, self.bird_image2, self.bird_image3]
        # gravity
        self.gravity = True

        self.y = float(self.bird_rect.y)


    def draw_bird(self, n = 2):
        self.screen.blit(self.bird_list[n], self.bird_rect)
        # self.bird_gravity()

    def bird_gravity(self):
        self.y += 1.97
        self.bird_rect.y = self.y
    #     else:
    #         self.y -= 2.2
    #         self.bird_rect.y = self.y

    def bird_flap(self):
        self.y -= 5.1
        self.bird_rect.y = self.y

    def bird_movement(self):
        if not self.gravity:
            self.bird_flap()
        else:
            self.bird_gravity()

        # Bird is always falling when gravity is applied.
        # So, bird movement is just bird flapping up or falling down.
