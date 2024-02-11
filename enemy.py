import pygame

class Ailen():
    def __init__(self, SW):
        self.screen = SW.screen
        self.image = pygame.image.load('images/house.png')
        self.rect = self.image.get_rect()
        self.screen_rect = SW.screen.get_rect()
        self.ailen_speed = 0.5

        self.y = float(self.rect.y)
    def update_ailen(self):
        if self.rect.bottom < self.screen_rect.bottom:
            self.y += self.ailen_speed
        self.rect.y = self.y
    def blit_ailen(self):
        self.screen.blit(self.image, self.rect)
