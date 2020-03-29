"""simple car game using Pygame"""

# importing the python gme library and initializing
import pygame as pg
import drawing
import random
from pygame import mixer

pg.init()

# game music
mixer.music.load('game.wav')
mixer.music.play(-1)

# defining colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY =  (200, 150, 110)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
font_style = pg.font.SysFont('bahnschrift', 50)
score_font = pg.font.SysFont('comicsansms', 35)

# defining variables
pl_carx = 350
pl_cary = 500
opp_carx = random.randrange(300,400)
opp_cary = random.randrange(50,650)
opp_carx1 = random.randrange(450,550)
opp_cary1 = random.randrange(50,650)
opp_carx2 = random.randrange(550,650)
opp_cary2 = random.randrange(50,650)
background_x = 0
background_y = 500
backchng = 10
end_game = pg.image.load("accident.jpg")
end_game1 = pg.transform.scale(end_game,(1000, 700))
score = 0





# creating a window
size = (1000, 700)
screen = pg.display.set_mode(size)
pg.display.set_caption("Car_game Developed By Aamir Ahmed")

# this loop will carry until the user exit the game
run = True
game_finish = False

# the clock is used to control the screen refresh rate
clock = pg.time.Clock()

# game loop
while run:
    while game_finish == True :
        screen.blit(end_game1, (0,0))

        msg = font_style.render("You lost!!!!!" + "\n press (c) for play again and (q) for quit " , True, RED)
        screen.blit(msg,(50,50))
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    game_finish = False
                    run = False
                elif event.key == pg.K_c:
                    run = True
                    game_finish =False
    for event in pg.event.get(): # user action
        if event .type == pg.QUIT: # if user closed
            run = False # exit this loop

        elif event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:

                    pl_carx -= 20

                elif event.key == pg.K_RIGHT:
                    pl_carx += 20

                elif event.key == pg.K_UP:

                    pl_cary -= 20
                elif event.key == pg.K_DOWN:

                    pl_cary += 20
    # game logic should start from here

    # drawing part
    # first clear the screen
    screen.fill(GREY)
    # for drawing different objects


    background_y += backchng
    if background_y > 100:
        background_y = -50
    drawing.draw_dashed_line(screen, BLACK, [430, 10], [430, (background_y+600)])
    drawing.draw_dashed_line(screen, BLACK, [560, 10], [560, (background_y+600)])

    pg.draw.rect(screen, GREEN, [0, 0, 300, (1000+background_y)], 0)
    pg.draw.rect(screen, GREEN, [700, 0, 300, (1000+background_y)], 0)

    clock.tick(30)


    TreeImg = pg.image.load('tree.jpg')
    screen.blit(TreeImg, (50, (50+background_y)))
    screen.blit(TreeImg, (200, 150+background_y))
    screen.blit(TreeImg, (190, 370+background_y))
    screen.blit(TreeImg, (80, 260+background_y))
    screen.blit(TreeImg, (50, 500+background_y))
    screen.blit(TreeImg, (200, 600+background_y))
    screen.blit(TreeImg, (730, 50+background_y))
    screen.blit(TreeImg, (880, 150+background_y))
    screen.blit(TreeImg, (880, 370+background_y))
    screen.blit(TreeImg, (730, 260+background_y))
    screen.blit(TreeImg, (730, 500+background_y))
    screen.blit(TreeImg, (880, 600+background_y))

    carImg = pg.image.load("car.jpg")
    carimg = pg.transform.scale(carImg,(50,80))
    screen.blit(carimg,(pl_carx,pl_cary))

    opp_car = pg. image.load("oppcar.png")
    opp_car1 = pg.transform.scale(opp_car, (40, 70))
    screen.blit(opp_car1,(opp_carx,opp_cary))
    opp_cary += 10
    opp_carx += 0
    if opp_cary > 700 or 300 < opp_carx >700:
        opp_cary = 50
        opp_carx = random.randrange(300,600)

    screen.blit(opp_car1, (opp_carx1, opp_cary1))
    opp_cary1 += 10
    opp_carx1 += 0
    if opp_cary1 > 700 or 300 < opp_carx1 > 700:
        opp_cary1 = 50
        opp_carx1 = random.randrange(300, 600)

    screen.blit(opp_car1, (opp_carx2, opp_cary2))
    opp_cary2 += 10
    opp_carx2 += 0
    if opp_cary2 > 700 or 300 < opp_carx2 > 700:
        opp_cary2 = 50
        opp_carx2 = random.randrange(300, 600)

    collision = pg.image.load("collision.png")
    collisionx = pg.transform.scale(collision,(300,500))
    if (pl_cary == opp_cary or pl_carx == opp_carx) or (pl_cary == opp_cary1 and pl_carx == opp_carx1) or (pl_cary == opp_cary2 and pl_carx == opp_carx2) :
        screen.blit(collisionx, (200, 100))
        game_finish = True


    value = score_font.render("your score: " + str(score), True, BLACK)
    score += 1
    screen.blit(value, [0, 0])



    # update the screen
    pg.display.flip()

    # refresh rate
    clock.tick(30)

pg.quit()
quit()







