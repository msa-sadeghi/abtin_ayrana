import random
import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
FPS = 60

# pygame.mixer.music.load("assets/-----.mp3")
# pygame.mixer.music.set_volume(0.5)
# pygame.mixer.music.play(-1)

pick_sound = pygame.mixer.Sound("assets/pick.wav")
loss_sound = pygame.mixer.Sound("assets/loss.wav")

my_clock = pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bear_image = pygame.image.load("assets/bear.png")
bear_rect =bear_image.get_rect()
bear_rect.bottomright = (SCREEN_WIDTH, SCREEN_HEIGHT)

honey_image = pygame.image.load("assets/h.png")
honey_rect = honey_image.get_rect()
honey_rect.bottomleft = (0, random.randint(100+honey_image.get_height(), SCREEN_HEIGHT))

f = pygame.font.Font("assets/f.otf", 32)
score = 0
score_text = f.render(f"Score:{score}", True, (85, 82, 188))
score_rect = score_text.get_rect(topleft=(0,0))

lives = 1
lives_text = f.render(f"Lives:{lives}", True, (85, 82, 188))
lives_rect = lives_text.get_rect(topright=(SCREEN_WIDTH - 20,0))


def game_over():
    pygame.mixer.music.stop()
    global running, score, lives
    game_over_text = f.render("Game Over, Press Enter to play again...", True, (145,20,190))
    game_over_rect = game_over_text.get_rect()
    game_over_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    score_text = f.render(f"Score:{score}", True, (85, 82, 188))
    lives_text = f.render(f"Lives:{lives}", True, (85, 82, 188))
    SCREEN.fill((0,0,0))
    SCREEN.blit(score_text, score_rect)
    SCREEN.blit(lives_text, lives_rect)
    SCREEN.blit(game_over_text, game_over_rect)
    pygame.display.update()
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pause = False
                    score = 0
                    lives = 3
                    pygame.mixer.music.play()

            if event.type == pygame.QUIT:
                pause = False
                running = False







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and bear_rect.top > 0:
        bear_rect.y -= 5
    if keys[pygame.K_DOWN] and bear_rect.bottom < SCREEN_HEIGHT:
        bear_rect.y += 5
    if keys[pygame.K_LEFT] and bear_rect.left > 0:
        bear_rect.x -= 5
    if keys[pygame.K_RIGHT] and bear_rect.right < SCREEN_WIDTH:
        bear_rect.x += 5

    honey_rect.x += 5
    if honey_rect.left >= SCREEN_WIDTH:
        loss_sound.play()
        lives -= 1
        if lives <= 0:
            game_over()
        honey_rect.bottomleft = (0, random.randint(100+honey_image.get_height(), SCREEN_HEIGHT))

    if honey_rect.colliderect(bear_rect):
        pick_sound.play()
        score += 1
        honey_rect.bottomleft = (0, random.randint(100+honey_image.get_height(), SCREEN_HEIGHT))


    score_text = f.render(f"Score:{score}", True, (85, 82, 188))
    lives_text = f.render(f"Lives:{lives}", True, (85, 82, 188))
    SCREEN.fill((0,0,0))
    SCREEN.blit(bear_image, bear_rect)
    SCREEN.blit(honey_image, honey_rect)
    SCREEN.blit(score_text, score_rect)
    SCREEN.blit(lives_text, lives_rect)
    pygame.display.update()
    my_clock.tick(FPS)

