import pygame
from const import *

class Game:
    def __init__(self) -> None:
        pass

    #show background sqaures
    def show_bg(self,surface): #Here surface is the screen
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col)%2==0: #if row+col is even
                    color = (234,235,200) #white in RGB format
                else:
                    color = (119,154,88) #black in RGB format

                rectVal = (col*SQ_SIZE,row*SQ_SIZE,SQ_SIZE,SQ_SIZE) 
                #rectVal = (x,y,width,height) 
                #x and y are the coordinates of the top left corner of the rectangle but here we are inserting squre's dimenstion to rectVal
            
                pygame.draw.rect(surface,color,rectVal)
                #pygame.draw.rect(surface,color,rectVal,thickness)

