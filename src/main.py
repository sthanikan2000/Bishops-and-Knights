import pygame , sys
from const import *
from game import Game

class Main():

    #Constructor
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))   
        pygame.display.set_caption('Tic Tac Toe')

        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game

        while True:
            game.show_bg(screen) # Draw the background squares

            #Check whether application is quit by user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
          

            pygame.display.update()

main=Main()
main.mainloop()