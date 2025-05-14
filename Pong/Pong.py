import pygame
import random
pygame.init()

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128,128,128)
# Display setup
screen_size = (800,500)
screen = pygame.display.set_mode(screen_size)
screen.fill(BLACK)
pygame.display.set_caption("Pong")
lower_bound = 350
upper_bound = 0
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
# Ball variables
ball_x = 375
ball_y = 235
ball_speed = 9
# Starting direction
ball_start_side = random.randint(1,2)
if ball_start_side == 1:
    player_turn = "left"
if ball_start_side == 2:
    player_turn = "right"
# Misc
running = True
FPS = 50
fpsClock = pygame.time.Clock()
player_move_units = 50
ball_y_direction = "down"
start = False
font = pygame.font.Font(None, 60)
starting_text = font.render("Press any button to start", True, (255, 255, 255))
text_rect = starting_text.get_rect(center=(400, 400))

# Game loop
while running:

    # When the game has not started
    while start == False:
        screen.fill(BLACK)
        # Drawing the midpoint line
        pygame.draw.rect(screen, GREY, (385, 0, 10, 500))
        # Drawing the players
        clock = pygame.time.Clock()
        pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
        pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
        # Drawing the ball
        pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))
        pygame.display.flip()
        # Displaying the text
        screen.blit(starting_text, text_rect)
        pygame.display.flip()


        fpsClock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    start = True

    # When the game has started
    for event in pygame.event.get():
        # Quits if user presses esc
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
    
    # Moving the ball
    # Vertical movement
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
    # Horizontal movement
    if player_turn == "left":
        if ball_x > 0:
            ball_x = ball_x - ball_speed
        elif ball_x <= 0:
            player_turn = "right"
    elif player_turn == "right":
        if ball_x < 770:
            ball_x = ball_x + ball_speed
        elif ball_x >= 0:
            player_turn = "left"
    
    screen.fill(BLACK)
    
    # Drawing the midpoint line
    pygame.draw.rect(screen, GREY, (385, 0, 10, 500))

    # Drawing the players
    clock = pygame.time.Clock()
    pygame.draw.rect(screen, WHITE, (player_1_x, player_1_y, 20, 150))
    pygame.draw.rect(screen, WHITE, (player_2_x, player_2_y, 20, 150))
    # Drawing the ball
    pygame.draw.rect(screen, WHITE, (ball_x, ball_y , 30, 30))

    pygame.display.flip()
    fpsClock.tick(FPS) 

# Quit
pygame.quit()