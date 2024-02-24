from constants import *
from world import World

game_world = World()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw()       
    pygame.display.update()
    clock.tick(fps)