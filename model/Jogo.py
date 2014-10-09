import pygame
from model.Sprites.Saida import Saida
from model.Sprites.Wall import Wall
from model.Sprites.Robo import Robo

class Jogo:

    def __init__(self, tplSize):

        # Criando tela no jogo
        self.screen = pygame.display.set_mode(tplSize)

        # Criacao da surface
        self.background = pygame.Surface(self.screen.get_size())

        # Adicionando o sprite robo no jogo
        self.robo = Robo()
        self.saida = Saida(0,450)

        # Criando / adicionaondo paredes
        self.grupowalls = pygame.sprite.Group()
        self.gerarparedes()

        # Renderizando as paredes
        self.grupowalls.clear(self.screen, self.background)
        self.grupowalls.update()
        self.grupowalls.draw(self.screen)

        # Renderizando a saida no jogo
        self.saida = pygame.sprite.RenderPlain(self.saida)
        self.saida.draw(self.screen)

        # Renderizando o robo no jogo
        self.playersprites = pygame.sprite.RenderPlain(self.robo)
        self.playersprites.draw(self.screen)

        pygame.display.flip()

    def gerarparedes(self):
        for x in range(0,450,50):
            self.grupowalls.add(Wall(0,x,50,50))

        for x in range(0,450,50):
            self.grupowalls.add(Wall(100,x+50,50,50))

        for x in range(0,450,50):
            self.grupowalls.add(Wall(200,x,50,50))

        for x in range(0,450,50):
            self.grupowalls.add(Wall(300,x+50,50,50))

        for x in range(0,450,50):
            self.grupowalls.add(Wall(400,x,50,50))
