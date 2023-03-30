import pygame
from random import randint

pygame.init()

game_sc = pygame.display.set_mode([800, 600])
icon = pygame.image.load('ufo.png')
FPS = 60

pygame.display.set_caption('Космические захватчики')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

background = pygame.image.load('background.png')

player = pygame.image.load('player.png')
player_rect = player.get_rect()
player_rect.x = 365
player_rect.y = 500
player_speed = 5

enemies = []
enemies_coords = []
enemies_speed = []

enemies_num = 5

bullet = pygame.image.load('bullet.png')
bullet_rect = bullet.get_rect()
bullet_status = 'ready'
bullet_speed = 10

for i in range(enemies_num):
    enemy = pygame.image.load('enemy.png')
    enemies.append(enemy)
    enemies_coords.append(pygame.Rect(
        randint(0, 800 - enemy.get_rect().width), 
        randint(50, 150),
        enemy.get_rect().width,
        enemy.get_rect().height
    ))
    enemies_speed.append(5)

while True:
    game_sc.fill(pygame.Color('black'))
    game_sc.blit(background, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
        if player_rect.x < 0:
            player_rect.x = 0
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
        if player_rect.x > 800 - player_rect.width:
            player_rect.x = 800 - player_rect.width
    if keys[pygame.K_UP]:
        if bullet_status == 'ready':
            bullet_status = 'fire'
            bullet_rect.x = player_rect.x
            bullet_rect.y = player_rect.y
            game_sc.blit(bullet, bullet_rect)

    for i in range(enemies_num):
        enemy = enemies_coords[i]
        enemy.x += enemies_speed[i]
        if enemy.x > 800 - enemy.width:
            enemy.y += 40
            enemies_speed[i] = -enemies_speed[i]
        elif enemy.x <= 0:
            enemy.y += 40
            enemies_speed[i] = -enemies_speed[i]

        index = bullet_rect.collidelist(enemies_coords)
        if index != -1:
            bullet_status = 'ready'
            bullet_rect.y = player_rect.y
            enemies_coords[index].x = randint(0, 736)
            enemies_coords[index].y = randint(50, 150)

        game_sc.blit(enemies[i], enemies_coords[i])

    if bullet_rect.y <= 0:
        bullet_status = 'ready'

    if bullet_status == 'fire':
        bullet_rect.y -= bullet_speed
        game_sc.blit(bullet, bullet_rect)

    game_sc.blit(player, player_rect)

    pygame.display.flip()
    clock.tick(FPS)

