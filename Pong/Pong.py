import sys, pygame
import pygame.font
pygame.init()

# Colours
BLACK = (0,  0,  0)
WHITE = (255,255,255)
red = (255, 0, 0)
# Screen setup
size = (800,500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
FPS = 20
screen.fill(BLACK)
pygame.display.set_caption("Pong")


# Game loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
    
    pygame.draw.rect(screen, WHITE, (30,200,20,125))
    pygame.display.update()

    pygame.draw.rect(screen, WHITE, (750,200,20,125))
    pygame.display.update()




#Shutdown
pygame.quit()