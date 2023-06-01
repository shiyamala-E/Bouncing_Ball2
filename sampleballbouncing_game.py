import pygame

import time

pygame.init() #Initializes pygame

screen=pygame.display.set_mode((500,300)) #Sets the Pygame Window 500*300

y=1 #y co-ordinate of the centre of the ball

direction=1 #To decide whether to Increment/Decrement y value

counter=0 #To count the number of bounces

while True:

    screen.fill((255,255,255))#White Screen

    pygame.draw.circle(screen,(255,0,0),(250,y),13,0)#Draws the red ball at (250,y)

    pygame.display.update()#Updates the above in the Pygame window

    time.sleep(.006)#To pause for .006 seconds 

    if y==300: #The ball is at the bottom of window

        direction=-1 #Move up by decrementing by 1

    elif y==0: #The ball is at the top of the window

        direction=1 #Move down by incrementing by 1

        counter=counter+1 #One bounce completed

    y=y+direction # Updates the next y co-ordinate of centre of ball

    if counter==3: #Three bounces are over

        pygame.quit() #Uninitializes pygame and window closes

        break #Control comes out of while loop
