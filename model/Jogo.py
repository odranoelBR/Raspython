import pygame
from model.Sprites.Wall import Wall
from model.Sprites.robo import Robo

class Jogo:

    def __init__(self, tplSize):

        # Criando tela no jogo
        self.screen = pygame.display.set_mode(tplSize)
        # Criacao da surface
        self.background = pygame.Surface(self.screen.get_size())
        # Adicionando o sprite robo no jogo
        self.robo = Robo()
        self.grupowalls = pygame.sprite.Group()


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


        self.grupowalls.clear(self.screen, self.background)
        self.grupowalls.update()
        self.grupowalls.draw(self.screen)


        # Renderizando o robo no jogo
        self.playersprites = pygame.sprite.RenderPlain(self.robo)
        self.playersprites.draw(self.screen)
        pygame.display.flip()



