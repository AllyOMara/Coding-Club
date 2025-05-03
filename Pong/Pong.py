import sys, pygame
import pygame.font
pygame.init()

# Colours
BLACK = (0,  0,  0)
WHITE = (255,255,255)

# Screen setup
size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 20
screen.fill(BLACK)
pygame.display.set_caption("Pong")

def draw_player_1(width, height, x, y):
    pygame.draw.rect(screen, WHITE, (width, height, x, y))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = y + 100
                pygame.display.update()
            if event.key == pygame.K_DOWN:
                y = y - 100
                pygame.display.update()

# Game loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        draw_player_1(30,200,20,125)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()

    pygame.draw.rect(screen, WHITE, (750,200,20,125))
    pygame.display.update()
