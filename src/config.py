import os,pygame
from sound import Sound

class Configurations:
    row = 3
    col = 3
    sq_size = 100
    width = row * sq_size
    height = col * sq_size

    #images
    cross = pygame.image.load(os.path.join(f'./resources/images/black_knight.png')) # To represent the cross 
    dot = pygame.image.load(os.path.join(f'./resources/images/white_bishop.png')) # To represent the dot
    game_icon = pygame.image.load(os.path.join(f'./resources/images/game.jpg')) # To represent the game icon
    #sounds
    start_sound = Sound( os.path.join('./resources/sounds/start.mp3') )
    drag_sound = Sound( os.path.join('./resources/sounds/dragger.mp3') )
    illegal_sound = Sound( os.path.join('./resources/sounds/illegal.mp3') )
    move_sound = Sound( os.path.join('./resources/sounds/move.mp3') )
    win_sound = Sound( os.path.join('./resources/sounds/win.mp3') )
    

    
    def change_dimensions(self,type): # type is whether increase or decrease
        if type == 'increase':
            print('Increasing')
            Configurations.row += 1
            Configurations.col += 1
            Configurations.width = Configurations.row * Configurations.sq_size
            Configurations.height = Configurations.col * Configurations.sq_size
            print("Board size is increased")
            return True
        elif type == 'decrease':
            if Configurations.row > 3:
                Configurations.row -= 1
                Configurations.col -= 1
                Configurations.width = Configurations.row * Configurations.sq_size
                Configurations.height = Configurations.col * Configurations.sq_size
                print("Board size is decreased")  
                return True                  
            else:
                print('Cannot decrease further')
                Configurations.illegal_sound.play()
                return False