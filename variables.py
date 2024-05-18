from random import randint
from math import sqrt
import pygame
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True
game_name = "Hunt the thimble"
GAME_WIDTH = 10
GAME_HEIGHT = 10
margin_left = 600
margin_top = 100
player_color = "#8f00ff"
key_x = randint(1, GAME_WIDTH)
key_y = randint(1, GAME_HEIGHT)
player_x = randint(1, GAME_WIDTH)
player_y= randint(1, GAME_HEIGHT)
min_steps = 0
if player_x == key_x and player_y == key_y:
    key_x = randint(1, GAME_WIDTH)
    key_y = randint(1, GAME_HEIGHT)
    player_x = randint(1, GAME_WIDTH)
    player_y= randint(1, GAME_HEIGHT)

player_x_test = player_x
player_y_test = player_y
key_x_test = key_x
key_y_test = key_y

player_found_key = False
background_color = '#FAF9F6'
steps = 0
distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
game_ended = False
icon = pygame.image.load('media/key_icon.svg')