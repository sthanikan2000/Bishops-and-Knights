import pygame , sys
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

            #Check whether mouse is clicked or not
            if clicked: 
                if event.type == pygame.MOUSEBUTTONUP:
                    clicked = False

            #If game is over
            elif event.type == pygame.MOUSEBUTTONDOWN and game.isgameOver == True : 
                clicked = True
                print("Game is already win by ",game.winner)

            #If game is not over and pieces are not initialized
            elif event.type == pygame.MOUSEBUTTONDOWN and game.isPiecesInitialized == False:
                clicked = True
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQ_SIZE
                clicked_col = mouseX // SQ_SIZE

                #placing piece on the board
                game.initializePiece(clicked_row, clicked_col)

            #If game is not over and pieces are initialized
            elif event.type == pygame.MOUSEBUTTONDOWN and game.isPiecesInitialized == True and game.dragger.dragging == False:
                clicked = True
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQ_SIZE
                clicked_col = mouseX // SQ_SIZE

                #activate dragger
                game.activate_dragger(clicked_row, clicked_col)

            #If game is not over and pieces are initialized and dragger is activated
            elif event.type == pygame.MOUSEBUTTONDOWN and game.isPiecesInitialized == True and game.dragger.dragging == True:
                clicked = True
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // SQ_SIZE
                clicked_col = mouseX // SQ_SIZE

                # clicked on the same square as dragger
                if game.dragger.col==clicked_col and game.dragger.row==clicked_row:
                    game.deactivate_dragger()

                # clicked on a different square and that square is empty
                elif game.board[clicked_row][clicked_col] == '':    
                    if game.is_valid_move(clicked_row,clicked_col):
                        print(f'Piece {game.current_turn} moved')
                        game.move_piece(clicked_row,clicked_col)
                    else:
                        game.deactivate_dragger()
                        print('Invalid move: You can only move to an adjacent square')
                else:
                    game.deactivate_dragger()
                    print('Invalid move: You can only move to an empty square')

            elif event.type == pygame.MOUSEBUTTONDOWN :
                clicked = True
                print("Nothing to DO")
            pygame.display.update()
            


main=Main()
main.mainloop()