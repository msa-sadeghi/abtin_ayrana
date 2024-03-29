from pygame.sprite import Sprite
import pygame
from constants import *
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        
        self.right_images = []
        self.left_images = []
        for i in range(1, 5):
            img = pygame.image.load(f"assets/guy{i}.png")
            img = pygame.transform.scale(img, (64, 64))
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
       
        self.frame_index = 0
        self.counter = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.idle = True
        self.inair = False
        self.dead_image = pygame.image.load("assets/ghost.png")

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self, tiles):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.idle = False
            dx -= 5
        if keys[pygame.K_RIGHT]:
            self.idle = False
            dx += 5
        if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.idle = True
        if keys[pygame.K_SPACE]   :
            self.vel_y = -15
        dy += self.vel_y
        self.vel_y += 1
           
        for t in tiles:
            if t[1].colliderect(self.rect.x + dx , self.rect.y, self.image.get_width(), self.image.get_height()):
                dx = 0
            if t[1].colliderect(self.rect.x , self.rect.y + dy, self.image.get_width(), self.image.get_height()):
                self.vel_y = 0
                dy = 0
     
        self.rect.x += dx
        self.rect.y += dy
        self.animation()

    def animation(self):
        self.counter += 1
        if self.counter >= 10:
            self.frame_index += 1
            self.counter = 0
        if self.frame_index >= len(self.right_images) or self.idle:
            self.frame_index = 0
        self.image = self.right_images[self.frame_index]
        
        