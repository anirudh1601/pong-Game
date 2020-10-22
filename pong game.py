import pygame
import random
from pygame.locals import *
from tkinter import messagebox



pygame.init()
WIDTH=500
HEIGHT=500


win=pygame.display.set_mode((WIDTH,HEIGHT))
bg=pygame.image.load("bg.jfif")





# INITIALIZING VARIABLES

white=(255,255,255)

black=(0,0,0)

vel=50

x=200

y=10

x1=200

y1=450

x3=200

y3=200

score1=0

score2=0

speed=1

x3_change=5

y3_change=5






centre=[HEIGHT/2,WIDTH/2]     



clock=pygame.time.Clock()

#DEFINING FUNCTIONS

def read_pos(str):
    str=str.split(",")
    return int(str[0]),int(str[1])


def make_pos(tup):
    return str(tup[0]) +" , " + str(tup[1])




def player1(x,y):
    win.blit(bg,(0,0))
    players1=pygame.draw.rect(win,black,(x,y,100,5))
    pygame.display.update()


def player2(x,y):
    players2=pygame.draw.rect(win,black,(x1,y1,100,5))
    pygame.display.update()

def ball1(x,y):
    ball=pygame.draw.circle(win,(0,0,0),(x3,y3),15,15)
    
    pygame.display.update()



paly=True
   


# CALLING MAIN LOOP


while paly:
    clock.tick(20)
    pygame.display.set_caption("My game" + "Score player 1: " + str(score1) + " - Score player 2: " + str(score2))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            paly=False



        keys=pygame.key.get_pressed()

        if keys[pygame.K_a] and x>40:
            x-=vel
        if keys[pygame.K_d] and x<355:
            x+=vel

        if keys[pygame.K_LEFT] and x1>40:
            x1-=vel

        if keys[pygame.K_RIGHT] and x1<355:
            x1+=vel



    x3+=x3_change
    y3+=y3_change

        
    if x3<=0:
        x3_change*=-1
    if x3>=500:
        x3_change*=-1
    if y3>=480 :
        y3=100
        score2+=1
           
    if y3<=10:
        y3=200
        score1+=1

        
    if (y3>430 and x3 < x1+50 and x3> x1-50 and y3> y1-50):
        y3_change*=-1

        



    if(y3<40 and x3 < x+80 and x3> x-80):
        y3_change*=-1

    

       
         


    pygame.display.update()





        

    # CALLING FUNCTIONS


       
    player1(x,y)
    player2(x1,y1)

    ball1(x3,y3)







    # ENDING

        
pygame.quit()