import sys, pygame
import pygame.font
pygame.init()

# Colours
BLACK = (0,  0,  0)
WHITE = (255,255,255)
# Display
size = (800,500)
screen = pygame.display.set_mode(size)
screen.fill(BLACK)
pygame.display.set_caption("Pong")
# Player 1
player_1_y = 150
player_1_x = 20
player_1_up = pygame.K_w
player_1_down = pygame.K_s
# Player 2
player_2_y = 150
player_2_x = 760
player_2_up = pygame.K_UP
player_2_down = pygame.K_DOWN
# Misc
running = True
FPS = 20
player_move_units = 50
lower_bound = 350
upper_bound = 0

# Game loop
while running:

    for event in pygame.event.get():
        # Quit key (esc)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Moving player 1
            if event.key == player_1_up:
                if player_1_y < upper_bound:
                    player_1_y == player_1_y
                elif player_1_y > upper_bound:
                    player_1_y = player_1_y - player_move_units
            if event.key == player_1_down:
                if player_1_y > lower_bound:
                    player_1_y = player_1_y
                elif player_1_y < lower_bound:
                    player_1_y = player_1_y + player_move_units
            # Moving player 2
            if event.key == player_2_up:
                if player_2_y < upper_bound:
                    player_2_y == player_2_y
                elif player_2_y > upper_bound:
                    player_2_y = player_2_y - player_move_units
            if event.key == player_2_down:
                if player_2_y > lower_bound:
                    player_2_y = player_2_y
                elif player_2_y < lower_bound:
                    player_2_y = player_2_y + player_move_units

        # Quits when the user presses the close button (x)
        elif event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Drawing the players
    clock = pygame.time.Clock()
    pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
    pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
    # Drawing the ball
    pygame.draw.rect(screen, WHITE, (385, 235 , 30, 30))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()