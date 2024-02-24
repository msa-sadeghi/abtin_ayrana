from constants import *
from player import Player
from enemy import Enemy
def spawn_enemies():
    for i in range(4):
        for j in range(8):
            e = Enemy(j * 96, i * 96, enemy_bullet_group)
            enemy_group.add(e)
player_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
spawn_enemies()


def check_bullet_collisions():
    if pygame.sprite.groupcollide(player_bullet_group, enemy_group, True, True):
        pass
    if pygame.sprite.spritecollide(my_player, enemy_bullet_group, True):
        pass
    if pygame.sprite.groupcollide(player_bullet_group, enemy_bullet_group, True, True):
        pass
    
    
    
level =1
def check_edge_collisions():
    on_edge = False
    for enemy in enemy_group:
        if enemy.rect.left < 0 or enemy.rect.right > SCREEN_WIDTH:
            on_edge = True
            break
    if on_edge:
        for enemy in enemy_group:
            enemy.direction *= -1
            enemy.rect.y += level * 10
my_player = Player(player_bullet_group)
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                my_player.fire()
    check_edge_collisions()
    check_bullet_collisions()
    screen.fill((0,0,0)) 
    my_player.move()           
    my_player.draw()
    enemy_group.update()
    enemy_group.draw(screen)
    player_bullet_group.update()
    player_bullet_group.draw(screen)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(screen)
    
    pygame.display.update()