from constants import *
class World:
    def __init__(self):
        self.image= pygame.image.load("assets/background.png")
        self.rect = self.image.get_rect(topleft = (0,0))
        
    def draw(self):
        screen.blit(self.image, self.rect)