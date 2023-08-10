import pygame,os
from const import *

class Game:
    def __init__(self):
        self.current_turn = 'O' # O is the first player
        self.no_X = 0
        self.no_O = 0
        self.board = [["" for i in range(ROWS)] for j in range(ROWS)] # nxn board
        self.isPiecesInitialized = False
        self.isgameOver = False
        self.winner = None
        self.cross_image = pygame.image.load(os.path.join(f'./img/black_pawn.png'))
        self.dot_image = pygame.image.load(os.path.join(f'./img/white_pawn.png'))

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

                img_center = col * SQ_SIZE + SQ_SIZE//2 , row* SQ_SIZE + SQ_SIZE//2

                # Now, draw the appropriate piece image based on the turn (cross or dot)
                img=None
                if self.board[row][col] == 'X': 
                    img = self.cross_image
                elif self.board[row][col] == 'O':
                    img = self.dot_image
                if img:
                    surface.blit(img,img.get_rect(center=img_center))

    def initializePiece(self,row,col):
        if self.board[row][col] == '':
            current = self.current_turn
            self.board[row][col] = current
            if self.current_turn == 'X':
                self.no_X += 1
                self.current_turn = 'O' #switch turn
            else:
                self.no_O += 1
                self.current_turn = 'X' #switch turn

            if self.no_X + self.no_O > 2*(ROWS-1):
                self.isgameOver = self.check_for_win(current)
                if self.isgameOver:
                    self.winner = current
                    print(f'{current} wins')
            if self.no_X + self.no_O == 2*ROWS:
                self.isPiecesInitialized = True
        else:
            print('Only one piece can be placed in a square')
            return
    
    def check_for_win(self,player):
        #check for row win
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != player:
                    break
            else:
                return True
            
        #check for column win
        for col in range(COLS):
            for row in range(ROWS):
                if self.board[row][col] != player:
                    break
            else:
                return True
            
        #check for diagonal win
        for i in range(ROWS): #check for left diagonal
            if self.board[i][i] != player:
                break
        else:
            return True
        for i in range(ROWS): #check for right diagonal
            if self.board[i][ROWS-i-1] != player:
                break
        else:
            return True
    
        return False