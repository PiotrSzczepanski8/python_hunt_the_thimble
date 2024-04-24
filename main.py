from variables import *

import pygame

pygame.init()

font = pygame.font.SysFont("Arial", 50)

pygame.display.set_caption(game_name)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and game_ended == False:
            steps += 1
            if event.key == pygame.K_w:
                player_y -= 1
                if player_y < 1:
                    print("Auć! uderzasz w ścianę!")
                    player_y = 1
            if event.key == pygame.K_s:
                player_y += 1
                if player_y > GAME_HEIGHT:
                    print("Auć! uderzasz w ścianę!")
                    player_y = GAME_HEIGHT
            if event.key == pygame.K_a:
                player_x -= 1
                if player_x < 1:
                    print("Auć! uderzasz w ścianę!")
                    player_x = 1
            if event.key == pygame.K_d:
                player_x += 1
                if player_x > GAME_WIDTH:
                    print("Auć! uderzasz w ścianę!")
                    player_x = GAME_WIDTH

            distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

            print('before', distance_before_move)
            print('after', distance_after_move)

            if distance_after_move == 0:
                text = 'Zwycięstwo'
                game_ended = True
            elif distance_before_move > distance_after_move:
                text = 'Ciepło'
            elif distance_before_move < distance_after_move:
                text = 'Zimno'

            distance_before_move = distance_after_move

            img = font.render(text, True, '#212121')
        
    screen.fill(background_color)
    pygame.draw.rect(screen, '#212121', pygame.Rect(margin_left, margin_top, GAME_WIDTH*50, GAME_HEIGHT*50))
    for i in range(GAME_WIDTH):
        pygame.draw.line(screen, background_color, ((margin_left + i*50), margin_top), (margin_left + i*50, margin_top+GAME_HEIGHT*50), 3)
    for i in range(GAME_WIDTH):
        pygame.draw.line(screen, background_color, ((margin_left), margin_top + i*50), (margin_left+GAME_WIDTH*50, margin_top + i*50), 3)
    pygame.draw.rect(screen, player_color, pygame.Rect(margin_left + player_x*50+2-50, margin_top+player_y*50+2-50, 47, 47))
    if 'img' in globals():
        screen.blit(img, (50, 200))
    pygame.display.flip()

pygame.quit()
quit() # code end 

# references:
while not player_found_key:
    steps += 1
    print()
    print('Możesz udać się w kierunkach określonych jako [w/a/s/d')

    move = input('Dokąd idziesz? ')
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > GAME_HEIGHT:
                print("Auć! uderzasz w ścianę!")
                player_y = GAME_HEIGHT
        case 's':
            player_y -= 1
            if player_y < 0:
                print("Auć! uderzasz w ścianę!")
                player_y = 0
        case 'a':
            player_x -= 1
            if player_x < 0:
                print("Auć! uderzasz w ścianę!")
                player_x = 0
        case 'd':
            player_x += 1
            if player_x > GAME_WIDTH:
                print("Auć! uderzasz w ścianę!")
                player_x = GAME_WIDTH
        case 'q':
            print('Koniec gry!')
            quit()
        case '_':
            print('Nie wiem dokąd idziesz...')
            continue
    
    if player_x == key_x and player_y == key_y:
        print('Klucz jest Twój, możesz iść otworzyć skarb')
        print(f'Wykonałeś/wykonałeś {steps} ruchów.')
        quit()
    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    print('before', distance_before_move)
    print('after', distance_after_move)

    if distance_before_move > distance_after_move:
        print('Ciepło')
    else:
        print('Zimno')
    distance_before_move = distance_after_move