from pygame.sprite import Sprite
import pygame

class Enemy(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/blob.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        group.add(self)
        
    def update(self):
        pass