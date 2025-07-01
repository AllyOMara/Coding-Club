import pygame
import random
# Setup
pygame.init()
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
screen_size = (800, 500)
screen = pygame.display.set_mode(screen_size)
screen.fill(BLACK)
pygame.display.set_caption("Pong")
lower_bound = 350
upper_bound = 0
player_1_y = 150
player_1_x = 20
player_1_up = pygame.K_w
player_1_down = pygame.K_s
player_1_score = 0
player_2_y = 150
player_2_x = 760
player_2_up = pygame.K_UP
player_2_down = pygame.K_DOWN
player_2_score = 0
ball_x = 375
ball_y = 235
ball_speed = 9
running = True
FPS = 50
fpsClock = pygame.time.Clock()
player_move_units = 50
start = False
font = pygame.font.Font(None, 60)
score_font = pygame.font.Font(None, 160)
starting_text = font.render("Press any button to start", True, (255, 255, 255))
fullscreen_reminder = font.render("Press ctrl to toggle fullscreen", True, (255, 255, 255))
text_rect_starter = starting_text.get_rect(center=(400, 400))
text_rect_reminder = fullscreen_reminder.get_rect(center=(400, 450))
player_1_score_text = score_font.render(f"{player_1_score}", True, (128, 128, 128))
player_2_score_text = score_font.render(f"{player_2_score}", True, (128, 128, 128))
text_player_2_score_text = player_2_score_text.get_rect(center=(900, 50))
text_player_1_score_text = player_1_score_text.get_rect(center=(400, 50))

ball_start_side = random.randint(1, 2)
if ball_start_side == 1:
    player_turn = "left"
elif ball_start_side == 2:
    player_turn = "right"
ball_start_angle = random.randint(1, 2)
if ball_start_angle == 1:
    ball_y_direction = "down"
elif ball_start_angle == 2:
    ball_y_direction = "up"
title_screen = True
pong_title_screen_text = font.render("PONG", True, (255, 255, 255))
text_rect_title_screen = pong_title_screen_text.get_rect(center = (400,100))
start = font.render("start", True, (255, 255, 255))
rect_start = pong_title_screen_text.get_rect(center = (400,200))
how_to = font.render("PONG", True, (255, 255, 255))
how_to_rect = pong_title_screen_text.get_rect(center = (400,100))

title_option = 1
# Title screen
while title_screen == True:
    # Display
    screen.blit(pong_title_screen_text, text_rect_title_screen)
    
    # Choosing menu options

    # Change to main menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            # Toggle fullscreen
            elif event.key == pygame.K_LCTRL:
                pygame.display.toggle_fullscreen()
                screen.blit(pong_title_screen_text, text_rect_title_screen)
            else:
                title_screen = False
    pygame.display.flip()

# Main menu
screen.fill(BLACK)
pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
clock = pygame.time.Clock()
pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
player_1_score_text = score_font.render(f"{player_1_score}", True, (128, 128, 128))
player_2_score_text = score_font.render(f"{player_2_score}", True, (128, 128, 128))
text_player_2_score_text = player_2_score_text.get_rect(center=(900, 50))
text_player_1_score_text = player_1_score_text.get_rect(center=(400, 50))
screen.blit(starting_text, text_rect_starter)
screen.blit(fullscreen_reminder, text_rect_reminder)
pygame.display.flip()
pygame.display.flip()
fpsClock.tick(FPS)
while start == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            # Toggle fullscreen
            elif event.key == pygame.K_LCTRL:
                pygame.display.toggle_fullscreen()
                screen.fill(BLACK)
                pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
                clock = pygame.time.Clock()
                pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
                pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
                pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
                screen.blit(starting_text, text_rect_starter)
                screen.blit(fullscreen_reminder, text_rect_reminder)
                pygame.display.flip()
            else:
                start = True

# Game loop
while running:
    while start == True:
        for event in pygame.event.get():
            # Quits
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                # Player movement
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
            # Quits
            elif event.type == pygame.QUIT:
                running = False
        # Ball Movement
        if ball_y_direction == "up":
            if ball_y > 0:
                ball_y = ball_y - ball_speed
            elif ball_y <= 0:
                ball_y = ball_y + ball_speed
                ball_y_direction = "down"
        elif ball_y_direction == "down":
            if ball_y < 470:
                ball_y = ball_y + ball_speed
            elif ball_y >= 470:
                ball_y = ball_y - ball_speed
                ball_y_direction = "up"
        # Collision with players
        if player_turn == "left":
            if ball_x > 0:
                if player_1_x <= ball_x <= player_1_x + 20 and player_1_y <= ball_y <= player_1_y + 150:
                    ball_x = ball_x + ball_speed
                    player_turn = "right"
                else:
                    ball_x = ball_x - ball_speed
            elif ball_x <= 0:
                player_2_score = player_2_score + 1
                player_1_y = 150
                player_1_x = 20
                player_2_y = 150
                player_2_x = 760
                ball_x = 375
                ball_y = 235
                start = False
            else:
                start = True
        elif player_turn == "right":
            if 730 <= ball_x <= 750 and player_2_y <= ball_y <= player_2_y + 150:
                player_turn = "left"
                ball_x = ball_x - ball_speed
            if ball_x < 770:
                if 730 <= ball_x <= 750 and player_2_y - 15 <= ball_y <= player_2_y + 150:
                    player_turn = "left"
                    ball_x = ball_x - ball_speed
                else:
                    ball_x = ball_x + ball_speed
            else:
                player_1_score = player_1_score + 1
                player_1_y = 150
                player_1_x = 20
                player_2_y = 150
                player_2_x = 760
                ball_x = 375
                ball_y = 235
                start = False
        # New frame
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
        clock = pygame.time.Clock()
        player_1_score_text = score_font.render(f"{player_1_score}", True, (128, 128, 128))
        player_2_score_text = score_font.render(f"{player_2_score}", True, (128, 128, 128))
        text_player_2_score_text = starting_text.get_rect(center=(900, 50))
        text_player_1_score_text = fullscreen_reminder.get_rect(center=(400, 50))
        screen.blit(player_1_score_text, text_player_1_score_text)
        screen.blit(player_2_score_text, text_player_2_score_text)
        pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
        pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
        pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
        pygame.display.flip()

        fpsClock.tick(FPS)

    # Between rounds
    while start == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    elif event.key == pygame.K_LCTRL:
                        pygame.display.toggle_fullscreen()
                        screen.fill(BLACK)
                        pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
                        clock = pygame.time.Clock()
                        pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
                        pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
                        pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
                        screen.blit(starting_text, text_rect_starter)
                        screen.blit(fullscreen_reminder, text_rect_reminder)
                        screen.blit(player_1_score_text, text_player_1_score_text)
                        screen.blit(player_2_score_text, text_player_2_score_text)
                        pygame.display.flip()
                    else:
                        start = True

pygame.quit()