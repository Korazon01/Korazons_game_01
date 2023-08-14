import pygame
import copy
import random
import sys
from support import screen,the_game,the_state,start_01,welcome_window,start_02,start_03,choose_moment,bad_answer,right_answer,the_gaming,the_win,ogusok_dead,end_window_win,opisanie
import support

clock = pygame.time.Clock()

pygame.init()


while the_game:

    screen.fill('black')

    if the_state == None:welcome_window(screen)

    elif the_state == 'start_01':start_01(screen)
    elif the_state == 'start_02':start_02(screen)
    elif the_state == 'start_03':start_03(screen)

    elif the_state == 'the_choose':choose_moment(screen)

    elif the_state == 'refuse':bad_answer(screen)
    elif the_state == 'agree':
        right_answer(screen)
    elif the_state == 'ogusok_invalid':
        opisanie(screen)



    elif the_state == 'win':the_win(screen)
    elif the_state == 'ogusok_dead':ogusok_dead(screen)
    elif the_state == 'the_end':end_window_win(screen)


    elif the_state == 'the_game':
        result = the_gaming(screen)
        if result == 'lose':
            the_state = 'refuse'
        elif result == 'win':
            the_state = 'win'



    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            the_game = False
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if the_state == None:
                    the_state = 'start_01'
                elif the_state == 'start_01':
                    the_state = 'start_02'

                elif the_state == 'start_02':
                    the_state = 'start_03'

                elif the_state == 'start_03':
                    the_state = 'the_choose'

                elif the_state == 'refuse':
                    the_state = 'the_choose'

                elif the_state == 'agree':
                    the_state = 'ogusok_invalid'

                elif the_state == 'ogusok_invalid':
                    the_state = 'the_game'

                elif the_state == 'win':
                    the_state = 'ogusok_dead'

                elif the_state == 'ogusok_dead':
                    the_state = 'the_end'


            if event.key in [pygame.K_1,pygame.K_2]:
                if the_state in ['the_choose']:

                    if event.key == pygame.K_2:
                        the_state = 'refuse'
                    elif event.key == pygame.K_1:
                        the_state = 'agree'


            if event.key in[pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:
                if the_state != 'the_game':continue

                if event.key == pygame.K_LEFT:support.the_direct = 'left'
                elif event.key == pygame.K_RIGHT:support.the_direct = 'right'
                elif event.key == pygame.K_UP:support.the_direct = 'up'
                else:support.the_direct = 'down'


    clock.tick(10)










