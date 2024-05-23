from variables import *
from image import *

import pygame

pygame.init()

font = pygame.font.SysFont("Arial", 30)
img12 = font.render('konwerter obrazow', True, '#222222')
img9 = font.render('wybierz opcję:', True, '#212121')
font = pygame.font.SysFont("Arial", 60)
img10 = font.render('A', True, '#222222')
img11 = font.render('P', True, '#222222')

pygame.display.set_caption(game_name)
pygame.display.set_icon(icon)

# algorytm zachłanny
while player_x_test != key_x_test or player_y_test != key_y_test:
    
    if player_x_test < key_x_test:
        player_x_test += 1
    elif player_x_test > key_x_test:
        player_x_test -= 1
    else:
        if player_y_test < key_y_test:
            player_y_test += 1
        elif player_y_test > key_y_test:
            player_y_test -= 1
    min_steps += 1

while running:
    x, y = pygame.mouse.get_pos()
    pygame.mouse.set_cursor(cursor)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_ended == False and event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d] and on_extra == False:
            if text_change == True:
                text_change = False
            if event.key == pygame.K_w:
                player_y -= 1
                if player_y < 1:
                    text2 = "Auć! uderzasz w ścianę!"
                    text_change = True
                    player_y = 1
            if event.key == pygame.K_s:
                player_y += 1
                if player_y > GAME_HEIGHT:
                    text2 = "Auć! uderzasz w ścianę!"
                    text_change = True
                    player_y = GAME_HEIGHT
            if event.key == pygame.K_a:
                player_x -= 1
                if player_x < 1:
                    text2 = "Auć! uderzasz w ścianę!"
                    text_change = True
                    player_x = 1
            if event.key == pygame.K_d:
                player_x += 1
                if player_x > GAME_WIDTH:
                    text2 = "Auć! uderzasz w ścianę!"
                    text_change = True
                    player_x = GAME_WIDTH

            distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
            steps += 1
            steps_text = f'Wykonane kroki: {steps}'

            if distance_after_move == 0:
                text = 'Zwycięstwo'
                game_ended = True
            elif distance_before_move > distance_after_move:
                text = 'Ciepło'
            elif distance_before_move < distance_after_move:
                text = 'Zimno'

            if (player_x, player_y) in extra:
                extra.remove((player_x, player_y))
                on_extra = True

            font = pygame.font.SysFont("Arial", 50)
            if 'text' in globals():
                img = font.render(text.upper(), True, '#212121')
            if 'steps_text' in globals():
                img3 = font.render(steps_text, True, '#212121')

            font = pygame.font.SysFont("Arial", 40)
            if 'min_steps' in globals():
                img8 = font.render(f'najkrótsza trasa: {min_steps} kroków', True, '#212121')

            font = pygame.font.SysFont("Arial", 30)
            if 'distance_before_move' in globals():
                img4 = font.render('distance before move:', True, '#666666')
                img5 = font.render(f'{distance_before_move}', True, '#666666')
            if 'distance_after_move' in globals():
                img6 = font.render('distance after move:', True, '#666666')
                img7 = font.render(f'{distance_after_move}', True, '#666666')
        
            distance_before_move = distance_after_move
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if a_button.collidepoint(event.pos) and on_extra == True:
                text2 = 'wszystkie pola zostały zamienione'
                text_change = True
                number = len(extra)
                player_x = randint(1, GAME_WIDTH)
                player_y= randint(1, GAME_HEIGHT)
                while player_x == key_x and player_y == key_y:
                    key_x = randint(1, GAME_WIDTH)
                    key_y = randint(1, GAME_HEIGHT)
                extra = generate_unique_coordinates(GAME_WIDTH, GAME_HEIGHT, player_x, player_y, key_x, key_y, number)
                on_extra = False
            
            if p_button.collidepoint(event.pos) and on_extra == True:
                text2 = 'plansza obróciła się'
                text_change = True
                key_x, key_y = key_y, key_x
                player_x, player_y = player_y, player_x
                extra = swap_coordinates(extra)
                on_extra = False
            
            if img_con_button.collidepoint(event.pos):
                if display_image == True:
                    display_image = False
                else:
                    display_image = True
            
            for rect, color in zip(color_buttons, image_colors):
                if rect.collidepoint(event.pos):
                    effect = color
                    image_effect_on = True


    screen.fill(background_color)
    pygame.draw.rect(screen, '#212121', pygame.Rect(margin_left, margin_top, GAME_WIDTH*50, GAME_HEIGHT*50))
    
    for i in range(GAME_WIDTH):
        pygame.draw.line(screen, background_color, ((margin_left + i*50), margin_top), (margin_left + i*50, margin_top+GAME_HEIGHT*50), 3)
    
    for i in range(GAME_WIDTH):
        pygame.draw.line(screen, background_color, ((margin_left), margin_top + i*50), (margin_left+GAME_WIDTH*50, margin_top + i*50), 3)
    image_x, image_y = margin_left, margin_top
    if display_image == True:
        if image_effect_on == True:
            image = pygame.image.load('media/image_effect.png').convert()
            image = pygame.transform.scale(image, (47, 47))
        for i in range(GAME_HEIGHT*GAME_WIDTH):
            screen.blit(image, (image_x, image_y))
            if i!= 0 and (str(i))[-1] == '9':
                image_y += 50
                image_x -= 500
            image_x += 50
    
    pygame.draw.rect(screen, player_color, pygame.Rect(margin_left + player_x*50+2-50, margin_top+player_y*50+2-50, 47, 47))

    pygame.draw.rect(screen, button_color, img_con_button)

    if 'img' in globals():
        screen.blit(img, (480, 10))

    font = pygame.font.SysFont('Arial', 50)
    if 'text2' in globals():
        img2 = font.render(text2, True, '#212121')

    if 'img2' in globals():
        if img2 != None:
           if text_change == True:
                screen.blit(img2, (360, 630))

    if 'img3' in globals():
        screen.blit(img3, (30, 210))

    if 'img4' in globals() and 'img5' in globals():
        screen.blit(img4, (30, 430))
        screen.blit(img5, (30, 465))
    if 'img6' in globals() and 'img7' in globals():
        screen.blit(img6, (30, 515))
        screen.blit(img7, (30, 550))
    
    if 'img8' in globals():
        screen.blit(img8, (30, 270))
    
    screen.blit(img12, (80, 37))

    if display_image == True:
        for color, rect in zip(image_colors, color_buttons):
            font = pygame.font.SysFont("Arial", 20)
            text_surface = font.render(color, True, '#212121')
            if color == 'oryginał':
                color = '#666666'
            pygame.draw.rect(screen, color, rect)
            screen.blit(text_surface, (1130, rect.y+5))


    if x > img_con_button.x and x < (img_con_button.x + img_con_button.width) and y > img_con_button.y and y < (img_con_button.y + img_con_button.height) or (x > 1120 and x < 1250 and y > 65 and y < 342):
        cursor = pygame.SYSTEM_CURSOR_HAND
    else:
        cursor = pygame.SYSTEM_CURSOR_ARROW

    if on_extra == True:
        s = pygame.Surface((1280, 720))
        s.set_alpha(127.5)
        s.fill((0, 0, 0))
        screen.blit(s, (0,0))
        pygame.draw.rect(screen, '#ffffff', pygame.Rect(390, 200, 500, 300)) # window
        pygame.draw.rect(screen, button_color, a_button) # a - container
        pygame.draw.rect(screen, button_color, p_button) # p - container
        screen.blit(img9, (545, 235)) # message
        screen.blit(img10, (516, 335)) # a
        screen.blit(img11, (722, 335)) # p
        if (x > a_button.x and x < (a_button.x + a_button.width) and y > a_button.y and y < (a_button.y + a_button.height)) or (x > p_button.x and x < (p_button.x + p_button.width) and y > p_button.y and y < (p_button.y + p_button.height)):
            cursor = pygame.SYSTEM_CURSOR_HAND
        else:
            cursor = pygame.SYSTEM_CURSOR_ARROW

    if image_effect_on == True:
        image_effect(input_path, output_path, effect)        
    pygame.display.flip()

pygame.quit()
quit()