from variables import *

import pygame

pygame.init()

font = pygame.font.SysFont("Arial", 50)

pygame.display.set_caption(game_name)
pygame.display.set_icon(icon)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_ended == False and event.key in [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d]:
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

            if 'text' in globals():
                img = font.render(text.upper(), True, '#212121')
            if 'text2' in globals():
                    img2 = font.render(text2, True, '#212121')
            if 'steps_text' in globals():
                img3 = font.render(steps_text, True, '#212121')
            if 'distance_before_move' in globals():
                img4 = font.render('distance before move:', True, '#212121')
                img5 = font.render(f'{distance_before_move}', True, '#212121')
            if 'distance_after_move' in globals():
                img6 = font.render('distance after move:', True, '#212121')
                img7 = font.render(f'{distance_after_move}', True, '#212121')
        
            distance_before_move = distance_after_move

    screen.fill(background_color)
    pygame.draw.rect(screen, '#212121', pygame.Rect(margin_left, margin_top, GAME_WIDTH*50, GAME_HEIGHT*50))
    
    for i in range(GAME_WIDTH):
        pygame.draw.line(screen, background_color, ((margin_left + i*50), margin_top), (margin_left + i*50, margin_top+GAME_HEIGHT*50), 3)
    
    for i in range(GAME_WIDTH):
        pygame.draw.line(screen, background_color, ((margin_left), margin_top + i*50), (margin_left+GAME_WIDTH*50, margin_top + i*50), 3)
    
    pygame.draw.rect(screen, player_color, pygame.Rect(margin_left + player_x*50+2-50, margin_top+player_y*50+2-50, 47, 47))
    
    if 'img' in globals():
        screen.blit(img, (30, 120))

    if 'img2' in globals():
        if img2 != None:
           screen.blit(img2, (30, 630))

    if 'img3' in globals():
        screen.blit(img3, (30, 210))

    if 'img4' in globals() and 'img5' in globals():
        screen.blit(img4, (30, 290))
        screen.blit(img5, (30, 350))
    if 'img6' in globals() and 'img7' in globals():
        screen.blit(img6, (30, 480))
        screen.blit(img7, (30, 550))

    pygame.display.flip()

pygame.quit()
quit()