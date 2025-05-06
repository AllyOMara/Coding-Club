import sys, pygame
import pygame.font
pygame.init()

# Colours
BLACK = (0,  0,  0)
WHITE = (255,255,255)

# Setup
size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 20
screen.fill(BLACK)
pygame.display.set_caption("Pong")
running = True

# Player positions
player_1_y = 150
player_move_units = 50
player_1_up = pygame.K_UP
player_1_down = pygame.K_DOWN

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == player_1_up:
                if player_1_y < 0:
                    player_1_y == player_1_y
                elif player_1_y > 0:
                    player_1_y = player_1_y - player_move_units
            if event.key == player_1_down:
                if player_1_y > 300:
                    player_1_y = player_1_y
                elif player_1_y < 300:
                    player_1_y = player_1_y + player_move_units
        elif event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (20, player_1_y, 20, 200))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()