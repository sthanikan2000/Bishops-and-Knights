import pygame,os

# from const import *  # ****************************
 
from config import Configurations
from dragger import Dragger

class Game:
    def __init__(self):
        self.config= Configurations()

        self.current_turn = 'O' # O is the first player: white bishop
        self.no_X = 0
        self.no_O = 0
        self.board = [["" for i in range(self.config.col)] for j in range(self.config.row)] # nxn board
        self.isPiecesInitialized = False

        self.isgameOver = False
        self.winner = None
        self.won_config = None

        self.cross_image = pygame.image.load(os.path.join(f'./img/black_knight.png')) # To represent the cross 
        self.dot_image = pygame.image.load(os.path.join(f'./img/white_bishop.png')) # To represent the dot
        # self.cross_image=pygame.transform.scale(self.cross_image, (80, 80))
        # self.dot_image=pygame.transform.scale(self.dot_image, (80, 80))

        self.dragger = Dragger()

    #show background sqaures
    def show_bg(self,surface): #Here surface is the screen
        ROWS = self.config.row
        COLS = self.config.col
        SQ_SIZE = self.config.sq_size

        for row in range(ROWS):
            for col in range(COLS):
                if self.isgameOver and self.won_config[0] == 'row' and self.won_config[1] == row:
                    color = (255,0,0)
                elif self.isgameOver and self.won_config[0] == 'col' and self.won_config[1] == col:
                    color = (255,0,0)
                elif self.isgameOver and self.won_config[0] == 'left_diagonal' and row == col:
                    color = (255,0,0)
                elif self.isgameOver and self.won_config[0] == 'right_diagonal' and row + col == ROWS-1:
                    color = (255,0,0)
                elif self.dragger.dragging and row== self.dragger.row and col==self.dragger.col:
                    color = (194,194,210)
                elif (row+col)%2==0: #if row+col is even
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
        ROWS = self.config.row
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
        ROWS = self.config.row
        COLS = self.config.col

        #check for row win
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != player:
                    break
            else:
                self.won_config = ('row',row)
                return True
            
        #check for column win
        for col in range(COLS):
            for row in range(ROWS):
                if self.board[row][col] != player:
                    break
            else:
                self.won_config = ('col',col)
                return True
            
        #check for diagonal win
        for i in range(ROWS): #check for left diagonal
            if self.board[i][i] != player:
                break
        else:
            self.won_config = ('left_diagonal',None)
            return True
        for i in range(ROWS): #check for right diagonal
            if self.board[i][ROWS-i-1] != player:
                break
        else:
            self.won_config = ('right_diagonal',None)
            return True
    
        return False

    def activate_dragger(self,row,col):
        if self.board[row][col] == self.current_turn:
            self.dragger.dragging = True
            self.dragger.update_dragger(row,col)
            print('Dragger activated')
        elif self.board[row][col] == '':
            print('Empty square')
        else:
            print('You can only move your own piece')

    def deactivate_dragger(self):
        self.dragger.dragging = False
        self.dragger.update_dragger(None,None)
        print('Dragger deactivated')

    def is_valid_move(self,next_row,next_col):
        if (next_row in [self.dragger.row-1,self.dragger.row+1]) and next_col == self.dragger.col:
            return True
        elif (next_col in [self.dragger.col-1,self.dragger.col+1]) and next_row == self.dragger.row:
            return True
        elif (next_row in [self.dragger.row-1,self.dragger.row+1]) or (next_col in [self.dragger.col-1,self.dragger.col+1]):
            return True 
        return False
    
    def move_piece(self,next_row,next_col):
        self.board[next_row][next_col] = self.current_turn
        self.board[self.dragger.row][self.dragger.col] = ''
        self.deactivate_dragger()
        self.isgameOver = self.check_for_win(self.current_turn)
        if self.isgameOver:
            self.winner = self.current_turn
            print(f'{self.current_turn} wins')
        self.current_turn = 'O' if self.current_turn == 'X' else 'X' #switch turn
    