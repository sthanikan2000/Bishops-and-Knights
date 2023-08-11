import pygame

class Sound:
    mute = False
    def __init__(self, path):
        pygame.mixer.init()
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        if not Sound.mute:
            pygame.mixer.Sound.play(self.sound)