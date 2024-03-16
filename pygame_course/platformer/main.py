import pygame

from constants import *
from world import World
from levels.level_creator import world_data
from player import Player
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

world = World(world_data)

my_player = Player(100, 500)

bg_img = pygame.image.load("assets/sky.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg_img, (0,0))
    world.draw(screen)
    my_player.draw(screen)
    my_player.update(world.tile_list)
    pygame.display.update()
    clock.tick(FPS)

