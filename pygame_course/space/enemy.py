from constants import *
from pygame.sprite import Sprite
class Enemy(Sprite):
    def __init__(self,x,y, bullet_group):
        super().__init__()
        self.image = pygame.image.load("assets/enemy.png")
        self.rect = self.image.get_rect(topleft=(x,y)) 
        self.bullet_group = bullet_group  
        self.direction = 1
        self.speed = 5  
    
    def update(self):
        self.rect.x += self.direction * self.speed  
            
    def fire(self):
        pass