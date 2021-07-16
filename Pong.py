import pygame
import sys
import random

# Initializing pygame
pygame.mixer.pre_init(44100,-16,1, 1024)
pygame.init()
clock = pygame.time.Clock()

# Sound
home_sound = pygame.mixer.Sound('Fluffing-a-Duck.mp3')

# Setting up the game window
screen_width = 900
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong Game')

# Coloring the background
light_grey = (128, 0, 128)
bg_color = pygame.Color('grey12')

# Game components
ball = pygame.Rect(screen_width/2 - 15, screen_height/2, 30, 30)
player = pygame.Rect(screen_width/2, screen_height - 40, 140, 10)
play = pygame.Rect(screen_width/2 - 80, 3*screen_height/4 - 25, 140, 50)

# Initializing speeds of game components
difficulty = 60
cnt = 1
ball_speed_y = -7
ball_speed_x = 7 * random.choice((-1, 1))
player_speed = 0

# Scores
player_score = 0

# Fonts
basic_font = pygame.font.Font('freesansbold.ttf', 32)
title_font = pygame.font.Font('freesansbold.ttf', 60)
White = (255, 255, 255)

# Variable to start the game
start = False

# Difficulty level
sensitivity = 6

# Variable for page
page = "home"

def draw_score():
    ''' Utility function to draw score on screen '''
    global player_score, White, screen_width, screen_height

    player_Score = basic_font.render(str(player_score), True, White)
    player_score_rect = player_Score.get_rect(midleft=(screen_width / 2, 20))
    screen.blit(player_Score, player_score_rect)

def ball_movement():
    ''' Function to move the ball '''
    global ball_speed_x, ball_speed_y, player_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.colliderect(player):
        ball_speed_y *= -1

    if ball.bottom >= screen_height:
        game_reset()

    if ball.right >= screen_width or ball.left <= 0:
        ball_speed_x *= -1

    if ball.colliderect(player):
        player_score += 1

def game_reset():
    ''' Function that resets the game '''
    global ball_speed_x, ball_speed_y, start, player_score

    ball.center = (screen_width/2, screen_height/2)
    player.center = (screen_width/2, screen_height - 40)
    ball_speed_x *= -1
    ball_speed_y *= random.choice((-1, 1))
    player_score = 0
    start = False

def player_movement():
    ''' Function that moves the player Rectangle '''
    player.x += player_speed

    if player.left <= 0:
        player.left = 0

    if player.right >= screen_height:
        player.right = screen_height

def Start_Game():
    ''' Function to start the game '''
    global screen, light_grey,player, bg_color,screen_height,screen_width

    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (0,screen_height/2), (screen_width, screen_height/2))
    draw_score()

def home_page():
    ''' Function for home page '''
    global White, bg_color, light_grey, play, title_font, page, home_sound

    pygame.mixer.Sound.play(home_sound)
    page = "home"
    settings = pygame.image.load('settings.png')
    screen.fill(bg_color)

    _home = title_font.render("PONG GAME", True, White)
    _play = basic_font.render("PLAY", True, White)

    home_rect = _home.get_rect(midleft=(screen_width/2 - 200, screen_height/2 - 50))
    play_rect = _play.get_rect(midleft=(screen_width/2-50, 3*screen_height/4))

    pygame.draw.rect(screen, light_grey, play)

    screen.blit(settings, (screen_width/2 - 60, screen_height/2 + 10))
    screen.blit(_play, play_rect)
    screen.blit(_home, home_rect)

def draw_back_button(pos):
    ''' Function to draw the 'BACK' Button '''
    global screen, light_grey

    back_button = basic_font.render("BACK", True, White)
    _back_button = back_button.get_rect(midleft=(60,80))
    back_button_box = pygame.Rect(pos[0],pos[1],110,60)

    pygame.draw.rect(screen,light_grey,back_button_box)

    screen.blit(back_button,_back_button)
    pygame.display.flip()

def settings():
    ''' Function for the settings page '''
    global sensitivity, page, difficulty

    show_difficulty()
    show_sensitivity()

    page = "settings"
    screen.fill(bg_color)

    settings = title_font.render("SETTINGS", True, White)
    plus = title_font.render("+", True, White)
    minus = title_font.render("-", True, White)
    sens = basic_font.render("Sensitivity", True, White)
    diff = basic_font.render("Difficulty", True, White)

    _sens = sens.get_rect(midleft=(360, 310))
    _diff = sens.get_rect(midleft=(370, 478))
    _settings = settings.get_rect(midleft=(screen_width/2 - 160, 200))
    _plus = plus.get_rect(midleft=(518, 372))
    _minus = minus.get_rect(midleft=(344, 375))

    screen.blit(settings,_settings)
    screen.blit(sens,_sens)
    screen.blit(diff,_diff)
    screen.blit(plus,_plus)
    screen.blit(minus,_minus)

    _plus = plus.get_rect(midleft=(518, 568))
    _minus = minus.get_rect(midleft=(344, 569))

    screen.blit(plus,_plus)
    screen.blit(minus,_minus)

    draw_back_button((50,50))
    pygame.display.flip()

def __clear(pos):
    ''' Function to clear screen at particular position '''
    global screen, bg_color

    empty = pygame.Rect(pos[0],pos[1], 60, 50)
    pygame.draw.rect(screen,bg_color,empty)
    pygame.display.flip()

def show_difficulty():
    ''' Function to show the difficulty level '''
    global cnt

    __clear((430, 550))
    show_diff = basic_font.render(str(cnt), True, White)
    _show_diff = show_diff.get_rect(midleft=(434, 569))

    screen.blit(show_diff,_show_diff)
    pygame.display.flip()

def show_sensitivity():
    ''' Function to show the sensitivity level '''
    global sensitivity

    __clear((430, 350))

    show_sens = basic_font.render(str(sensitivity), True, White)
    _show_sens = show_sens.get_rect(midleft=(445, 377))

    screen.blit(show_sens,_show_sens)
    pygame.display.flip()

def check(pos):
    ''' Function to identify position of click and do necessary actions '''
    global start, page, sensitivity, difficulty, cnt

    x, y = pos
    
    # Take user to the appropriate page based on click
    if x >= 370 and x <= 510 and y >= 575 and y <= 625:
        start = True
    elif x >= 400 and x <= 470 and y >= 430 and y <= 490 and page == "home":
        settings()
        show_difficulty()
        show_sensitivity()
    elif x >= 338 and x <= 368 and y >= 555 and y <= 586 and page == "settings":
        if cnt > 1:
            cnt -= 1
            difficulty -= 50
        show_difficulty()
    elif x >= 522 and x <= 552 and y >= 544 and y <= 590 and page == "settings":
        if cnt < 4:
            difficulty += 50
            cnt += 1
        show_difficulty()
    elif x >= 338 and x <= 368 and y >= 360 and y <= 390 and page == "settings":
        if sensitivity > 4:
            sensitivity -= 1
        show_sensitivity()
    elif x >= 522 and x <= 552 and y >= 355 and y <= 395 and page == "settings":
        if sensitivity < 15:
            sensitivity += 1
        show_sensitivity()
    elif x >= 50 and x <= 160 and y >= 50 and y <= 110 and page == "settings":
        home_page()

# Infinite loop to run the game
while True:

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            check(pos)

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_speed -= sensitivity
            if event.key == pygame.K_RIGHT:
                player_speed += sensitivity

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_speed += sensitivity
            if event.key == pygame.K_RIGHT:
                player_speed -= sensitivity

    # If game has not started yet, Display the home page
    if start == False:
        if page == "home":
            home_page()
            pygame.display.flip()
        continue

    # Start the game
    Start_Game()
    pygame.display.flip()

    ball_movement()
    player_movement()

    clock.tick(difficulty)
