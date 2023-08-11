import pygame , sys
from config import Configurations
from game import Game
from sound import Sound

class Main():

    #Constructor
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Configurations.width,Configurations.height)) 
        pygame.display.set_caption('Bishop Vs Knight')
        
        self.game = Game()

        Configurations.start_sound.play() 

    def mainloop(self):
        screen = self.screen
        game = self.game
        clicked=False #To check whether mouse is in pressed state or not
        pressed=False #To check whether key is in pressed state or not

        while True:
            game.show_bg(screen) # Draw the background squares

            #Check whether application is quit by user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #Check whether mouse is clicked or not
                elif clicked: 
                    if event.type == pygame.MOUSEBUTTONUP:
                        clicked = False
                
                elif pressed:
                    if event.type == pygame.KEYUP:
                        pressed = False

                elif event.type == pygame.KEYDOWN:
                    pressed = True
                    if event.key == pygame.K_r:
                        game=Game()
                        print("Game is restarted")
                        Configurations.start_sound.play() 

                    elif event.key == pygame.K_UP or event.key == pygame.K_i:
                        game.config.change_dimensions('increase')
                        screen = pygame.display.set_mode((Configurations.width,Configurations.height))
                        game=Game()
                        print("Board size is increased")

                    elif event.key == pygame.K_DOWN or event.key == pygame.K_d:
                        game.config.change_dimensions('decrease')
                        screen = pygame.display.set_mode((Configurations.width,Configurations.height))
                        game=Game()
                        print("Board size is decreased")                    
                    elif event.key == pygame.K_m:
                        Sound.mute = not Sound.mute
                        if Sound.mute:
                            print("Muted")	
                        else:
                            print("Unmuted")

                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    else:
                        print("Nothing to DO")
                        Configurations.illegal_sound.play()   
                    
                #If game is over
                elif event.type == pygame.MOUSEBUTTONDOWN and game.isgameOver == True : 
                    clicked = True
                    print("Game is already win by ",game.winner)
                    Configurations.illegal_sound.play()

                #If game is not over and pieces are not initialized
                elif event.type == pygame.MOUSEBUTTONDOWN and game.isPiecesInitialized == False:
                    clicked = True
                    mouseX, mouseY = pygame.mouse.get_pos()
                    clicked_row = mouseY // Configurations.sq_size
                    clicked_col = mouseX // Configurations.sq_size
                    

                    #placing piece on the board
                    game.initializePiece(clicked_row, clicked_col)

                #If game is not over and pieces are initialized
                elif event.type == pygame.MOUSEBUTTONDOWN and game.isPiecesInitialized == True and game.dragger.dragging == False:
                    clicked = True
                    mouseX, mouseY = pygame.mouse.get_pos()
                    clicked_row = mouseY // Configurations.sq_size
                    clicked_col = mouseX // Configurations.sq_size 
                    

                    #activate dragger
                    game.activate_dragger(clicked_row, clicked_col)

                #If game is not over and pieces are initialized and dragger is activated
                elif event.type == pygame.MOUSEBUTTONDOWN and game.isPiecesInitialized == True and game.dragger.dragging == True:
                    clicked = True
                    mouseX, mouseY = pygame.mouse.get_pos()
                    clicked_row = mouseY // Configurations.sq_size
                    clicked_col = mouseX // Configurations.sq_size

                    # clicked on the same square as dragger
                    if game.dragger.col==clicked_col and game.dragger.row==clicked_row:
                        game.deactivate_dragger()
                        Configurations.drag_sound.play()
                    # clicked on a different square and that square is empty
                    elif game.board[clicked_row][clicked_col] == '':    
                        if game.is_valid_move(clicked_row,clicked_col):
                            Configurations.move_sound.play()
                            print(f'Piece {game.current_turn} moved')
                            game.move_piece(clicked_row,clicked_col)
                        else:
                            game.deactivate_dragger()
                            print('Invalid move: You can only move to an adjacent square')
                            Configurations.illegal_sound.play() 
                    else:
                        game.deactivate_dragger()
                        print('Invalid move: You can only move to an empty square')
                        Configurations.illegal_sound.play() 

                elif event.type == pygame.MOUSEBUTTONDOWN :
                    clicked = True
                    print("Nothing to DO")
                    Configurations.illegal_sound.play()                    
            pygame.display.update()
            


main=Main()
main.mainloop()