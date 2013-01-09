import sys
import pygame
from pygame.locals import *
import state

class Policia_Llamada(state.State):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/image/paisaje.jpg")
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        self.historia = pygame.mixer.Sound("data/sound/llama_policia.wav")
        self.historia.play()
        pygame.time.delay(int(self.historia.get_length()*1000))
        #self.historia y play
        #delay
    
    def exit(self):
        self.historia.stop()
        #self.historia.stop
    
    def reason(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
