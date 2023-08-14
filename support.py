import pygame
import copy
import random

the_game = None
the_state = None
the_location = None
the_direct = None
the_snake = None
the_apple = None
apples_location = None
schef_window = None
the_head = None
count = None
the_target = None

def restart():
    global the_game,the_state,the_snake,the_location,the_direct,the_apple,apples_location,schef_window,the_head,count,the_target

    the_game = True
    the_state = None
    the_snake = pygame.Surface((50, 50))
    the_snake.fill('#31f700')
    the_location = [[0,0]]
    the_direct = None
    the_apple = pygame.Surface((50,50))
    the_apple.fill('white')
    apples_location = [300,300]
    schef_window = pygame.image.load('die_fotos/schef_window.jpg')
    the_head = pygame.Surface((50,50))
    the_head.fill('#187a00')
    count = 1
    the_target = 25
restart()



def welcome_window(screen):
    welcome_window_text = pygame.font.Font(None, 70).render('To start the game push Enter', False, 'red')
    screen.blit(welcome_window_text,(50,360))


def start_01(screen):
    the_start_image_01 = pygame.image.load('die_fotos/shef_want_to_cook.webp')
    text_start_image_01_01 = pygame.font.Font(None,70).render('Наконец-то приготовлю своё ',False,'black')
    text_start_image_01_02 = pygame.font.Font(None, 70).render('любимое оливье из огузка',False, 'black')

    screen.blit(the_start_image_01,(0,0))
    screen.blit(text_start_image_01_01,(50,600))
    screen.blit(text_start_image_01_02, (50, 650))

    text_3 = pygame.font.Font(None, 50).render('push enter...', False, 'violet')
    screen.blit(text_3, (500, 750))

def start_02(screen):
    the_start_image_02 = pygame.image.load('die_fotos/schef.png')
    text_start_image_02 = pygame.font.Font(None, 90).render('А где яйца инвалиды!!! ', False, 'red')

    screen.blit(the_start_image_02, (0, 0))
    screen.blit(text_start_image_02, (5, 650))

    text_3 = pygame.font.Font(None, 50).render('push enter...', False, 'violet')
    screen.blit(text_3, (500, 750))

def start_03(screen):
    the_start_image_03 = pygame.image.load('die_fotos/schef_ask.webp')
    text_start_image_03_01 = pygame.font.Font(None, 70).render('Инвалид найди яйца для оливье,', False, 'red')
    text_start_image_03_02 = pygame.font.Font(None, 70).render('иначе я съем тебя вместо огузка', False, 'red')

    screen.blit(the_start_image_03, (0, 0))
    screen.blit(text_start_image_03_01, (0, 600))
    screen.blit(text_start_image_03_02, (0, 650))

    text_3 = pygame.font.Font(None, 50).render('push enter...', False, 'violet')
    screen.blit(text_3, (500, 750))

def choose_moment(screen):
    the_choose_moment = pygame.image.load('die_fotos/the_schref_choose.jpg')

    screen.blit(the_choose_moment,(0,0))


def bad_answer(screen):
    bad_answer_image = pygame.image.load('die_fotos/angry_schef.webp')
    text_1 = pygame.font.Font(None, 70).render('Шеф сделает оливье из вас', False, 'red')
    text_2 = pygame.font.Font(None, 150).render('GAME OVER', False, 'red')
    text_3 = pygame.font.Font(None, 50).render('To come back push enter...', False, 'violet')
    screen.blit(bad_answer_image, (0, 0))
    screen.blit(text_1, (10, 600))
    screen.blit(text_2, (50, 300))
    screen.blit(text_3, (340, 750))


def right_answer(screen):
    right_answer_image = pygame.image.load('die_fotos/ogusok.webp')
    text_1 = pygame.font.Font(None, 70).render('Я огузок и я спратал яйца,', False, 'red')
    text_2 = pygame.font.Font(None, 70).render('чтобы шеф меня не сожрал', False, 'red')
    text_3 = pygame.font.Font(None, 50).render('To find eggs push enter...', False, 'violet')
    screen.blit(right_answer_image, (0, 0))
    screen.blit(text_1, (10, 600))
    screen.blit(text_2, (10, 650))
    screen.blit(text_3, (340, 750))

def opisanie(screen):
    text_1 = pygame.font.Font(None, 100).render('To find eggs push:', False, 'red')
    text_2 = pygame.font.Font(None, 100).render('left,right,down,up', False, 'red')
    screen.blit(text_1, (60, 300))
    screen.blit(text_2, (60, 400))


def the_win(screen):
    happy_schef = pygame.image.load('die_fotos/happy_shef.webp')
    text_1 = pygame.font.Font(None, 85).render('Молодец инвалид, теперь', False, 'red')
    text_2 = pygame.font.Font(None, 85).render('я съем огузка а не тебя', False, 'red')
    screen.blit(happy_schef,(0,0))
    screen.blit(text_1, (10, 600))
    screen.blit(text_2, (10, 650))

    text_3 = pygame.font.Font(None, 50).render('push enter...', False, 'violet')
    screen.blit(text_3, (500, 750))

def ogusok_dead(screen):
    happy_schef = pygame.image.load('die_fotos/ogusok_dead.jpg')
    text_1 = pygame.font.Font(None, 90).render('огузок: НЕЕЕЕЕЕЕЕЕЕТ!!!', False, 'red')

    screen.blit(happy_schef, (0, 0))
    screen.blit(text_1, (10, 600))

    text_3 = pygame.font.Font(None, 50).render('push enter...', False, 'violet')
    screen.blit(text_3, (500, 750))

def end_window_win(screen):
    screen.fill('black')

    the_end_text = pygame.font.Font(None,250).render('You win',False,'red')

    screen.blit(the_end_text,(50,300))

def make_apple():
    while True:
        new_apple = [random.randint(0,15)*50,random.randint(0,15)*50]
        check = True
        for i in the_location:
            if new_apple == i:
                check = False

        if check:return new_apple




def make_move():

    if not the_direct:
        the_location[0] = [0,0]
        return

    shift = copy.deepcopy(the_location)[:-1]

    if the_direct == 'left':
        if the_location[0][0] == 0: the_location[0][0] = 750
        else: the_location[0][0] -= 50
    elif the_direct == 'right':
        if the_location[0][0] == 750: the_location[0][0] = 0
        else: the_location[0][0] +=50
    elif the_direct == 'up':
        if the_location[0][1] == 0: the_location[0][1] = 750
        else:  the_location[0][1] -=50
    elif  the_direct == 'down':
        if  the_location[0][1] == 750: the_location[0][1] = 0
        else: the_location[0][1] += 50

    for part in range(len(the_location)-1):
        the_location[part+1] = shift[part]



def the_gaming(screen):
    global apples_location,the_state,count,the_count

    make_move()

    for i in range(1,len(the_location)):
        if the_location[i] == the_location[0]:
            restart()
            return 'lose'


    if the_location[0] == apples_location:
        the_location.append(apples_location)
        apples_location = make_apple()
        count+=1

        if len(the_location) == the_target:
            restart()
            return 'win'

    screen.blit(schef_window,(0,0))

    for part in range(len(the_location)):
        screen.blit(the_snake,tuple(the_location[part]))

    screen.blit(the_apple, tuple(apples_location))
    screen.blit(the_head,the_location[0])

    the_count = pygame.font.Font(None, 70).render(str(count)+" of "+str(the_target), False, 'violet')

    screen.blit(the_count, (10,10))




screen = pygame.display.set_mode((800,800))









