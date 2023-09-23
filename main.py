import pygame
import time
import random
import schedule
from Fruit import Fruit
from Player import Player


# Window size
window_x = 720
window_y = 480

initial_fruit_x = random.randrange(1, (window_x // 10)) * 10
initial_fruit_y = random.randrange(1, (window_y // 10)) * 10

fruits = [Fruit(initial_fruit_x, initial_fruit_y)]

def add_fruit():
    x = random.randrange(1, (window_x // 10)) * 10
    y = random.randrange(1, (window_y // 10)) * 10
    fruit = Fruit(x, y)
    fruits.append(fruit)


schedule.every(6).seconds.do(add_fruit)

snake_speed = 15

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialising pygame
pygame.init()

player1 =  Player('player1', blue, 'RIGHT', 100, 50)
player2 =  Player('player2', green, 'LEFT', 500, 200)
players = [player1, player2]
# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

def is_screen_colliding(player):
    return player.position[0] < 0 or player.position[0] > window_x - 10 or player.position[1] < 0 or player.position[1] > window_y - 10

def is_self_colliding(player):
    for block in player.snake_body[1:]:
        if player.position[0] == block[0] and player.position[1] == block[1]:
            return True
    return False

def is_player_colliding(player):
    for otherPlayer in players:
        for block in otherPlayer.snake_body[1:]:
            if player.position[0] == block[0] and player.position[1] == block[1]:
                return True

# displaying Score function
def show_score(color, font, size, player, top ):
    # creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    # create the display surface object
    # score_surface
    score_surface = score_font.render(player.name+ ' score : ' + str(player.score), True, color)

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()
    score_rect.topleft = (0, top)

    # displaying text
    game_window.blit(score_surface, score_rect)


# game over function
def game_over(player):
    # creating font object my_font
    my_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = my_font.render(
        str(player.name) + 'lost\n' + 'Score : ' + str(player.score), True, player.color)

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while True:
    schedule.run_pending()
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player1.setDirection('UP')
            if event.key == pygame.K_DOWN:
                player1.setDirection('DOWN')
            if event.key == pygame.K_LEFT:
                player1.setDirection('LEFT')
            if event.key == pygame.K_RIGHT:
                player1.setDirection('RIGHT')
            if event.key == pygame.K_w:
                player2.setDirection('UP')
            if event.key == pygame.K_s:
                player2.setDirection('DOWN')
            if event.key == pygame.K_a:
                player2.setDirection('LEFT')
            if event.key == pygame.K_d:
                player2.setDirection('RIGHT')

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    game_window.fill(black)

    for index, player in enumerate(players):
        player.draw(game_window)
        show_score(white, 'times new roman', 20, player, index * 20)
        fruitEaten = False
        for fruit in fruits:
            fruitEaten = player.position[0] == fruit.x and player.position[1] == fruit.y
            if fruitEaten:
                fruits.remove(fruit)
        if fruitEaten:
            player.move(True)
            fruit_spawn = False
            player.score += 10
            continue
        player.move(False)
        if is_screen_colliding(player) or is_self_colliding(player) or is_player_colliding(player):
            game_over(player)


    for fruit in fruits:
        pygame.draw.rect(game_window, white, pygame.Rect(fruit.x, fruit.y, 10, 10))

    pygame.display.update()

    fps.tick(snake_speed)

