import pygame
from model.Sprites.robo import Robo

class Jogo:

    def __init__(self, tplSize):
        # Criando tela no jogo
        self.screen = pygame.display.set_mode(tplSize)
        # Adicionando o sprite robo no jogo
        self.robo = Robo()
        # Renderizando o robo no jogo
        self.playersprites = pygame.sprite.RenderPlain(self.robo)
        self.playersprites.draw(self.screen)
        pygame.display.flip()

        # Criacao da surface
        self.background = pygame.Surface(self.screen.get_size())

