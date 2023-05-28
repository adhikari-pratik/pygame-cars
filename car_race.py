import pygame
import random
import math
from pygame import mixer

pygame.init()

count = 0
highscore = 0
score = 0
chance = 4
lives = []

left_margin = 325
right_margin = 675

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Cars")
car_img = pygame.image.load("backgrounds\car.png")

spawn_x_1 = random.randint(left_margin, right_margin-64)
spawn_y_1 = random.randint(0, 200)
spawn_x_2 = random.randint(left_margin, right_margin-64)
spawn_y_2 = random.randint(0, 200)
coin_x = random.randint(left_margin+16, right_margin-16)
coin_y = random.randint(0, 200)

initial_pos_x = random.choice((left_margin+64, right_margin-64))
initial_pos_y = 636
new_pos_x = initial_pos_x
new_pos_y = initial_pos_y

text_score = pygame.font.Font("freesansbold.ttf", 32)
text_score_last = pygame.font.Font("freesansbold.ttf", 42)
text_gameover = pygame.font.Font("freesansbold.ttf", 78)
text_highscore = pygame.font.Font("freesansbold.ttf", 42)
text_newhighscore = pygame.font.Font("freesansbold.ttf", 45)

run = True
gameover = False

# restart button
button_x = range(800, 881)
button_y = range(500, 581)
# exit button
exit_y = range(200, 280)
# lives
life_x = [950, 900, 850, 800]
life_y = 10


def life():
    global life_x, life_y
    global lives
    heart = pygame.image.load("backgrounds\heart.png")
    for i in range(chance):
        lives.append(pygame.transform.scale(heart, (40, 40)))
    for i in range(chance):
        screen.blit(lives[i], (life_x[i], life_y))


def quit_game():
    img_quit = pygame.image.load("backgrounds\sign-out.png")
    img_quit = pygame.transform.scale(img_quit, (80, 80))
    screen.blit(img_quit, (800, 200))
    if event.type == pygame.MOUSEBUTTONDOWN:
        exit_pos = pygame.mouse.get_pos()
        return exit_pos
    else:
        return 1, 0


def background():
    back_ground = pygame.image.load("backgrounds/river_topview.jpg")
    road = pygame.image.load("backgrounds/road_new.jpg")
    new_background_1 = pygame.transform.scale(back_ground, (325, 700))
    new_background_2 = pygame.transform.scale(back_ground, (325, 700))
    screen.blit(new_background_1, (0, 0))
    screen.blit(new_background_2, (right_margin, 0))
    new_road = pygame.transform.rotate(road, 90)
    new_road = pygame.transform.scale(new_road, (350, 700))
    screen.blit(new_road, (325, 0))


def restart_button():

    restart = pygame.image.load("backgrounds/reload.png")
    restart = pygame.transform.scale(restart, (80, 80))
    screen.blit(restart, (800, 500))
    if event.type == pygame.MOUSEBUTTONDOWN:
        get_pos = pygame.mouse.get_pos()
        print(get_pos)
        return get_pos
    else:
        return 1, 1


def game_over():
    # global gameover
    # gameover = True
    global highscore
    show = True

    text_x = 260
    text_y = 325
    print_game_over = text_gameover.render("GAME OVER", True, red)
    screen.blit(print_game_over, (text_x, text_y))

    score_x = 420
    score_y = 275
    print_score = text_score_last.render("SCORE: " + str(score), True, green)
    screen.blit(print_score, (score_x, score_y))

    highscore_x = 350
    highscore_y = 175

    if score < highscore:
        show = False

    if show:
        highscore = score
        print_newhighscore = text_newhighscore.render("NEW HIGHSCORE: " + str(highscore), True, blue)
        screen.blit(print_newhighscore, (highscore_x-64, highscore_y))
    else:
        print_highscore = text_highscore.render("HIGHSCORE: " + str(highscore), True, green)
        screen.blit(print_highscore, (highscore_x, highscore_y))

    e_x_1 = left_margin
    e_y_1 = 8000
    e_x_2 = left_margin
    e_y_2 = 8000
    co_x = left_margin + 16
    co_y = -8000
    return e_x_1, e_y_1, e_x_2, e_y_2, co_x, co_y


def show_score():
    text_x = 10
    text_y = 10
    pygame.draw.rect(screen, white, rect=(text_x, text_y, 168, 32))
    print_score = text_score.render("SCORE: " + str(score), True, green)
    screen.blit(print_score, (text_x, text_y))


# def finish_game():
#     global gameover
#
#     e_x_1 = left_margin
#     e_y_1 = 8000
#     e_x_2 = left_margin
#     e_y_2 = 8000
#     co_x = left_margin+16
#     co_y = 8000
#     gameover = True
#     return e_x_1, e_y_1, e_x_2, e_y_2, co_x, co_y


# def track():
#
#     pygame.draw.line(screen, green, (left_margin, 0), (left_margin, 700), width=6)
#     pygame.draw.line(screen, green, (right_margin, 0), (right_margin, 700), width=6)
#
#     pygame.draw.line(screen, white, (500, 0), (500, 100), width=2)
#     pygame.draw.line(screen, white, (500, 150), (500, 250), width=2)
#     pygame.draw.line(screen, white, (500, 300), (500, 400), width=2)
#     pygame.draw.line(screen, white, (500, 450), (500, 550), width=2)
#     pygame.draw.line(screen, white, (500, 600), (500, 700), width=2)


def obstacles_1():
    global spawn_y_1
    global spawn_x_1

    if (spawn_y_1 > 690) and (spawn_y_1 < 5000):
        spawn_x_1 = random.randint(left_margin, right_margin-80)
        spawn_y_1 = random.randint(0, 100)
    if spawn_y_1 <= 690:
        spawn_y_1 += 3.2
    pygame.draw.rect(screen, red, rect=(spawn_x_1, spawn_y_1, 80, 80))
    # print(spawn_x, spawn_y)
    return spawn_x_1, spawn_y_1


def obstacles_2():
    global spawn_y_2
    global spawn_x_2

    if (spawn_y_2 > 690) and (spawn_y_2 < 5000):
        spawn_x_2 = random.randint(left_margin, right_margin-80)
        spawn_y_2 = random.randint(0, 164)
    if spawn_y_2 <= 690:
        spawn_y_2 += 3.2
    pygame.draw.rect(screen, red, rect=(spawn_x_2, spawn_y_2, 80, 80))
    # print(spawn_x, spawn_y)
    return spawn_x_2, spawn_y_2


def coins():
    global coin_x
    global coin_y
    global chance

    if (coin_y > 700) and (coin_y < 2000):
        coin_x = random.randint(left_margin+16, right_margin-16)
        coin_y = random.randint(0, 200)
        chance -= 1

    if coin_y <= 700:
        coin_y += 2
    pygame.draw.circle(screen, yellow, (coin_x, coin_y), 15)
    return coin_x, coin_y


def collision_1():
    # global score
    global gameover
    detect_x, detect_y = obstacles_1()

    distance_obstacle = math.sqrt(((new_pos_x - detect_x) ** 2) + ((new_pos_y - detect_y) ** 2))
    if distance_obstacle < 50:
        gameover = True
        collide_sound = mixer.Sound("backgrounds/mixkit-car-explosion-debris-1562.wav")
        collide_sound.play(maxtime=1000)
    #     return True
    # else:
    #     return False


def collision_2():
    # global score
    global gameover
    detect_x, detect_y = obstacles_2()

    distance_obstacle = math.sqrt(((new_pos_x - detect_x) ** 2) + ((new_pos_y - detect_y) ** 2))
    if distance_obstacle < 50:
        gameover = True
        collide_sound = mixer.Sound("backgrounds/mixkit-car-explosion-debris-1562.wav")
        collide_sound.play(maxtime=1000)
        # return True

    # else:
        # return False


def score_coin():
    point_x, point_y = coins()
    distance_coin = math.sqrt(((new_pos_x - point_x) ** 2) + ((new_pos_y - point_y) ** 2))
    if distance_coin < 50:
        return True
    else:
        return False


def move():
    global count
    change_pos_y = 0
    change_pos_x = 0

    if event.type == pygame.KEYDOWN:
        count = 1
        if event.key == pygame.K_UP:
            change_pos_y = -2.7
        elif event.key == pygame.K_DOWN:
            change_pos_y = 2.7
        elif event.key == pygame.K_RIGHT:
            change_pos_x = 2.7
        elif event.key == pygame.K_LEFT:
            change_pos_x = -2.7
        else:
            pass

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            change_pos_y = 0
        if event.key == pygame.K_DOWN:
            change_pos_y = 0
        if event.key == pygame.K_RIGHT:
            change_pos_x = 0
        if event.key == pygame.K_LEFT:
            change_pos_x = 0
    return change_pos_x, change_pos_y
    # new_pos_x += change_pos_x
    # new_pos_y += change_pos_y
    # print(new_pos_y)


# def position():
#     change_x, change_y = move()
#     new_pos_x = temp_pos_x
#     new_pos_y = temp_pos_y
#     new_pos_x += change_x
#     new_pos_y += change_y
#     print(new_pos_x, new_pos_y)
#     return new_pos_x, new_pos_y


def boundaries():
    bound_x, bound_y = move()

    if new_pos_x < left_margin:
        bound_x = 2
    if new_pos_x > right_margin-64:
        bound_x = -2
    if new_pos_y < 0:
        bound_y = 2
    if new_pos_y > 636:
        bound_y = -2

    return bound_x, bound_y


def orientation():
    if count == 0:
        player_front(initial_pos_x, initial_pos_y)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            player_front(new_pos_x, new_pos_y)
        if event.key == pygame.K_DOWN:
            player_back(new_pos_x, new_pos_y)
        if event.key == pygame.K_RIGHT:
            player_right(new_pos_x, new_pos_y)
        if event.key == pygame.K_LEFT:
            player_left(new_pos_x, new_pos_y)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            player_front(new_pos_x, new_pos_y)
        if event.key == pygame.K_DOWN:
            player_back(new_pos_x, new_pos_y)
        if event.key == pygame.K_RIGHT:
            player_right(new_pos_x, new_pos_y)
        if event.key == pygame.K_LEFT:
            player_left(new_pos_x, new_pos_y)

    if event.type == pygame.mouse:
        orientation()


def player_front(x, y):
    car_img_front = pygame.transform.rotate(car_img, 180)
    screen.blit(car_img_front, (x, y))


def player_left(x, y):
    car_img_left = pygame.transform.rotate(car_img, 270)
    screen.blit(car_img_left, (x, y))


def player_right(x, y):
    car_img_right = pygame.transform.rotate(car_img, 90)
    screen.blit(car_img_right, (x, y))


def player_back(x, y):
    screen.blit(car_img, (x, y))


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # screen.fill(black)
    background()

    # track()
    change_x, change_y = boundaries()
    new_pos_x += change_x
    new_pos_y += change_y

    collision_1()
    collision_2()

    life()

    if chance == 0:
        gameover = True

    point = score_coin()

    if point:
        coin_x = random.randint((left_margin+16), (right_margin-16))
        coin_y = random.randint(0, 200)
        score += 1
        print(score)
        score_sound = mixer.Sound("backgrounds/ZAAX5G5-videogame-gameplay-collect.wav")
        score_sound.play(maxtime=200)

    # obstacles()
    orientation()

    # if state_1 or state_2:
    #     (e1_x, e1_y, e2_x, e2_y, c_x, c_y) = finish_game()
    #     spawn_x_1 = e1_x
    #     spawn_y_1 = e1_y
    #     spawn_x_2 = e2_x
    #     spawn_y_2 = e2_y
    #     coin_x = c_x
    #     coin_y = c_y
    #     collide_sound = mixer.Sound("mixkit-car-explosion-debris-1562.wav")
    #     collide_sound.play(maxtime=1000)

    if gameover:
        (e1_x, e1_y, e2_x, e2_y, c_x, c_y) = game_over()
        spawn_x_1 = e1_x
        spawn_y_1 = e1_y
        spawn_x_2 = e2_x
        spawn_y_2 = e2_y
        coin_x = c_x
        coin_y = c_y
        quit_x, quit_y = quit_game()
        restart_x, restart_y = restart_button()
        if (restart_x in button_x) and (restart_y in button_y):
            gameover = False
            state_1 = False
            state_2 = False
            score = 0
            chance = 4
            spawn_y_2 = 800
            spawn_y_1 = 800
            coin_y = 800
            new_pos_x = initial_pos_x
            new_pos_y = initial_pos_y
        if (quit_x in button_x) and (quit_y in exit_y):
            exit()
    else:
        show_score()

    pygame.display.update()
