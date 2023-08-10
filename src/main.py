import pygame , sys, time
from const import *
from game import Game

class Main():

    #Constructor
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))  
        pygame.display.set_caption('Tic Tac Toe')
        
        self.clock = pygame.time.Clock()

        self.game = Game()

    
    def mainloop(self):
        screen = self.screen
        game = self.game
        clicked=False #To check whether mouse is in pressed state or not

        while True:
            game.show_bg(screen) # Draw the background squares

            #Check whether application is quit by user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            if clicked:
                if event.type == pygame.MOUSEBUTTONUP:
                    clicked = False

            elif event.type == pygame.MOUSEBUTTONDOWN and game.isPiecesInitialized == False and game.isgameOver == False :
                clicked = True
                mouseX, mouseY = pygame.mouse.get_pos()

                clicked_row = mouseY // SQ_SIZE
                clicked_col = mouseX // SQ_SIZE

                #placing piece on the board
                game.initializePiece(clicked_row, clicked_col)
            
            elif event.type == pygame.MOUSEBUTTONDOWN and game.isgameOver == True :
                clicked = True
                print("Game is already win by ",game.winner)
            elif event.type == pygame.MOUSEBUTTONDOWN :
                clicked = True
                print("Pieces are already placed on the board")
            pygame.display.update()
            


main=Main()
main.mainloop()