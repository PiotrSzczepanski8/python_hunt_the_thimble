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

while player_x == key_x and player_y == key_y:
    key_x = randint(1, GAME_WIDTH)
    key_y = randint(1, GAME_HEIGHT)

def generate_unique_coordinates(game_width, game_height, player_x, player_y, key_x, key_y):
    extra = []
    while len(extra) < 10:
        new_tuple = (randint(1, game_width), randint(1, game_height))

        if (new_tuple not in extra and 
            new_tuple != (player_x, player_y) and 
            new_tuple != (key_x, key_y)):
            extra.append(new_tuple)

    return extra

player_x_test = player_x
player_y_test = player_y
key_x_test = key_x
key_y_test = key_y

extra = generate_unique_coordinates(GAME_WIDTH, GAME_HEIGHT, player_x, player_y, key_x, key_y)
#print(extra)

def swap_coordinates(coord_list):
    return [(y, x) for x, y in coord_list]

player_found_key = False
background_color = '#FAF9F6'
steps = 0
distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
game_ended = False
icon = pygame.image.load('media/key_icon.svg')
on_extra = False
a_button = pygame.Rect(476, 310, 120, 120)
p_button = pygame.Rect(682, 310, 120, 120)
cursor = pygame.SYSTEM_CURSOR_ARROW
button_color = '#888888'
img_con_button = pygame.Rect(30, 30, 350, 50)
print(extra)
image = pygame.image.load('media/image.png').convert()
image = pygame.transform.scale(image, (47, 47))
display_image = False
image_effect_on = False
image_colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'oryginał']
red_button = pygame.Rect(1120, 65, 110, 37)
green_button = pygame.Rect(1120, 105, 110, 37)
blue_button = pygame.Rect(1120, 145, 110, 37)
cyan_button = pygame.Rect(1120, 185, 110, 37)
magenta_button = pygame.Rect(1120, 225, 110, 37)
yellow_button = pygame.Rect(1120, 265, 110, 37)
original_button = pygame.Rect(1120, 305, 110, 37)
color_buttons = [red_button, green_button, blue_button, cyan_button, magenta_button, yellow_button, original_button]