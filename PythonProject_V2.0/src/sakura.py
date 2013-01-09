import sys
import pygame
from pygame.locals import *
import state
import policia
import carta_clow

class Sakura_Pres(state.State):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/image/paisaje.jpg")
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        self.historia = pygame.mixer.Sound("data/sound/audio1.wav")
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
                if event.key == K_a:
                    return policia.Policia_Llamada()
                    #return policia.Policia_Llamada()
                if event.key == K_d:
                    return Sakura_Sucede()
                    #return sakura sucede



class Sakura_Sucede(state.State):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/image/paisaje.jpg")
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        self.historia = pygame.mixer.Sound("data/sound/audio2.wav")
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
                if event.key == K_z:
                    return policia.Policia_Llamada()
                    #return policia.Policia_Llamada()
                if event.key == K_c:
                    return Sakura_Escalera()
                    #return sakura escalera
                    

class Sakura_Escalera(state.State):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/image/paisaje.jpg")
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        self.historia = pygame.mixer.Sound("data/sound/audio3.wav")
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
                if event.key == K_a:
                    return Sakura_Libro()
                    #return sakura libro
                if event.key == K_b:
                    return policia.Policia_Llamada()
                    #return policia.Policia_Llamada()


class Sakura_Libro(state.State):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/image/paisaje.jpg")
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        self.historia = pygame.mixer.Sound("data/sound/audio4.wav")
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
                if event.key == K_a:
                    return Sakura_Noche()
                    #return sakura siguiente noche noche previo a un audio creo
                if event.key == K_d:
                    pygame.quit()
                    sys.exit()
                    #return policia.Policia_Llamada()



class Sakura_Noche(state.State):
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.background = pygame.image.load("data/image/paisaje.jpg")
        self.display.blit(self.background, (0, 0))
        pygame.display.flip()
        self.historia = pygame.mixer.Sound("data/sound/audio5.wav")
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
                if event.key == K_a:
                    return carta_clow.Carta_Agua()
                    #return sakura siguiente noche noche previo a un audio creo
                if event.key == K_v:
                    return carta_clow.Carta_Viento()
                    #return policia.Policia_Llamada()

    