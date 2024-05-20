from variables import *

import pygame

pygame.init()

font = pygame.font.SysFont("Arial", 30)
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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_ended == False and event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d] and on_extra == False:
            if event.key == pygame.K_w:
                player_y -= 1
                if player_y < 1:
                    text2 = "Auć! uderzasz w ścianę!"
                    player_y = 1
                else:
                    text2 = None
            if event.key == pygame.K_s:
                player_y += 1
                if player_y > GAME_HEIGHT:
                    text2 = "Auć! uderzasz w ścianę!"
                    player_y = GAME_HEIGHT
                else:
                    text2 = None
            if event.key == pygame.K_a:
                player_x -= 1
                if player_x < 1:
                    text2 = "Auć! uderzasz w ścianę!"
                    player_x = 1
                else:
                    text2 = None
            if event.key == pygame.K_d:
                player_x += 1
                if player_x > GAME_WIDTH:
                    text2 = "Auć! uderzasz w ścianę!"
                    player_x = GAME_WIDTH
                else:
                    text2 = None

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
            if 'text2' in globals():
                    img2 = font.render(text2, True, '#212121')
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
                print('A')
                on_extra = False
            if p_button.collidepoint(event.pos) and on_extra == True:
                print('P')
                on_extra = False

    screen.fill(background_color)
    pygame.draw.rect(screen, '#212121', pygame.Rect(margin_left, margin_top, GAME_WIDTH*50, GAME_HEIGHT*50))
    
    for i in range(GAME_WIDTH):
        pygame.draw.line(screen, background_color, ((margin_left + i*50), margin_top), (margin_left + i*50, margin_top+GAME_HEIGHT*50), 3)
    
    for i in range(GAME_WIDTH):
        pygame.draw.line(screen, background_color, ((margin_left), margin_top + i*50), (margin_left+GAME_WIDTH*50, margin_top + i*50), 3)
    
    pygame.draw.rect(screen, player_color, pygame.Rect(margin_left + player_x*50+2-50, margin_top+player_y*50+2-50, 47, 47))

    if 'img' in globals():
        screen.blit(img, (480, 10))

    if 'img2' in globals():
        if img2 != None:
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

    # on_extra = True # window test
    if on_extra == True:
        s = pygame.Surface((1280, 720))
        s.set_alpha(127.5)
        s.fill((0, 0, 0))
        screen.blit(s, (0,0))
        pygame.draw.rect(screen, '#ffffff', pygame.Rect(390, 200, 500, 300)) # window
        pygame.draw.rect(screen, '#888888', a_button) # a - container
        pygame.draw.rect(screen, '#888888', p_button) # p - container
        screen.blit(img9, (545, 235)) # message
        screen.blit(img10, (516, 335)) # a
        screen.blit(img11, (722, 335)) # p


    pygame.display.flip()

pygame.quit()
quit()