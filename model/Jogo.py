import pygame
from model.Sprites.Ground import Ground
from model.Sprites.Saida import Saida
from model.Sprites.Wall import Wall
from model.Sprites.Robo import Robo
import time

class Jogo():

    def __init__(self, tplSize):

        # Criando tela no jogo
        self.screen = pygame.display.set_mode(tplSize)
        self.screen.fill([30,168,16])

        # Criacao da surface
        self.background = pygame.Surface(self.screen.get_size())

        # Adicionando o sprite robo no jogo
        self.robo = Robo()
        self.saida = Saida(0,450)

        # Criando / adicionaondo paredes
        self.grupowalls = pygame.sprite.Group()
        self.gerarparedes()

        # Criando / adicionado o chao
        self.ground = pygame.sprite.Group()
        self.gerarChao()
        self.ground.draw(self.screen)

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

    def atualizar(self,tela):
        clock = pygame.time.Clock()
        clock.tick(150)
        self.screen.blit(self.background, self.robo)
        self.playersprites.update(self.grupowalls)

        self.saida.update(self.playersprites, tela)

        self.ground.draw(self.screen)
        self.grupowalls.draw(self.screen)
        self.playersprites.draw(self.screen)
        pygame.display.flip()

        time.sleep(0.6)

    def apagarrobo(self):
        pygame.sprite.RenderClear(self.robo)

    def gerarChao(self):
        for x in range(0,500,150):
            self.ground.add(Ground(50,x,50,50,'ground'))
            self.ground.add(Ground(50,x+50,50,50,'ground1'))
            self.ground.add(Ground(50,x+100,50,50,'ground2'))

        for x in range(0,500,150):
            self.ground.add(Ground(150,x,50,50,'ground'))
            self.ground.add(Ground(150,x+100,50,50,'ground1'))
            self.ground.add(Ground(150,x+50,50,50,'ground2'))

        for x in range(0,500,150):
            self.ground.add(Ground(250,x,50,50,'ground'))
            self.ground.add(Ground(250,x+50,50,50,'ground1'))
            self.ground.add(Ground(250,x+100,50,50,'ground2'))

        for x in range(0,500,150):
            self.ground.add(Ground(350,x,50,50,'ground'))
            self.ground.add(Ground(350,x+100,50,50,'ground1'))
            self.ground.add(Ground(350,x+50,50,50,'ground2'))

        for x in range(0,500,150):
            self.ground.add(Ground(450,x,50,50,'ground'))
            self.ground.add(Ground(450,x+50,50,50,'ground1'))
            self.ground.add(Ground(450,x+100,50,50,'ground2'))

        for x in range(0,500,150):
            self.ground.add(Ground(500,x,50,50,'ground'))
            self.ground.add(Ground(500,x+100,50,50,'ground1'))
            self.ground.add(Ground(500,x+50,50,50,'ground2'))

        self.ground.add(Ground(100,0,50,50,'ground1'))
        self.ground.add(Ground(200,450,50,50,'ground1'))
        self.ground.add(Ground(300,0,50,50,'ground1'))
        self.ground.add(Ground(400,450,50,50,'ground1'))

