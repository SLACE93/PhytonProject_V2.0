import pygame

import state
import sakura

pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sakura")

class RBR():
    def __init__(self):
        self.sm = state.StateMachine(self, sakura.Sakura_Pres())

    def start(self):
        while True:
            self.sm.update()

if __name__ == "__main__":
    game = RBR()
    game.start()
    