import pygame
from model.Sprites.Ground import Ground
from model.Sprites.Saida import Saida
from model.Sprites.Wall import Wall
from model.Sprites.Robo import Robo
import time

class Jogo:

    def __init__(self, tplSize):
        self.screen = pygame.display.set_mode(tplSize)
        self.screen.fill([30, 168, 16])
        self.background = pygame.Surface(self.screen.get_size())
        self.robo = Robo()
        self.saida = Saida(50, 0)
        self.grupowalls = pygame.sprite.Group()
        self.gerarparedes()
        self.ground = pygame.sprite.Group()
        self.gerarChao()
        self.ground.draw(self.screen)
        self.grupowalls.clear(self.screen, self.background)
        self.grupowalls.update()
        self.grupowalls.draw(self.screen)
        self.saida = pygame.sprite.RenderPlain(self.saida)
        self.saida.draw(self.screen)
        self.playersprites = pygame.sprite.RenderPlain(self.robo)
        self.playersprites.draw(self.screen)
        pygame.display.flip()

    def gerarparedes(self):
        for x in range(0, 400, 100):
            self.grupowalls.add(Wall(350, x + 100, 100, 100))
        for x in range(0, 400, 100):
            self.grupowalls.add(Wall(150, x + 0, 100, 100))
        for x in range(0, 500, 100):
            self.grupowalls.add(Wall(-50, x + 0, 100, 100))

    def atualizar(self, tela):
        clock = pygame.time.Clock()
        clock.tick(150)
        self.screen.blit(self.background, self.robo)
        self.playersprites.update(self.grupowalls)
        self.saida.update(self.playersprites, tela)
        self.ground.draw(self.screen)
        self.grupowalls.draw(self.screen)
        self.saida.draw(self.screen)
        self.playersprites.draw(self.screen)
        pygame.display.flip()
        time.sleep(0.3)

    def apagarrobo(self):
        pygame.sprite.RenderClear(self.robo)

    def gerarChao(self):
        for x in range(0, 500, 150):
            self.ground.add(Ground(50, x, 50, 50, 'ground'))
            self.ground.add(Ground(50, x + 50, 50, 50, 'ground1'))
            self.ground.add(Ground(50, x + 100, 50, 50, 'ground2'))

        for x in range(0, 500, 150):
            self.ground.add(Ground(150, x, 50, 50, 'ground'))
            self.ground.add(Ground(150, x + 100, 50, 50, 'ground1'))
            self.ground.add(Ground(150, x + 50, 50, 50, 'ground2'))

        for x in range(0, 500, 150):
            self.ground.add(Ground(250, x, 50, 50, 'ground'))
            self.ground.add(Ground(250, x + 50, 50, 50, 'ground1'))
            self.ground.add(Ground(250, x + 100, 50, 50, 'ground2'))

        for x in range(0, 500, 150):
            self.ground.add(Ground(350, x, 50, 50, 'ground'))
            self.ground.add(Ground(350, x + 100, 50, 50, 'ground1'))
            self.ground.add(Ground(350, x + 50, 50, 50, 'ground2'))

        for x in range(0, 500, 150):
            self.ground.add(Ground(450, x, 50, 50, 'ground'))
            self.ground.add(Ground(450, x + 50, 50, 50, 'ground1'))
            self.ground.add(Ground(450, x + 100, 50, 50, 'ground2'))

        for x in range(0, 500, 150):
            self.ground.add(Ground(500, x, 50, 50, 'ground'))
            self.ground.add(Ground(500, x + 100, 50, 50, 'ground1'))
            self.ground.add(Ground(500, x + 50, 50, 50, 'ground2'))

        self.ground.add(Ground(100, 0, 50, 50, 'ground1'))
        self.ground.add(Ground(200, 450, 50, 50, 'ground1'))
        self.ground.add(Ground(300, 0, 50, 50, 'ground1'))
        self.ground.add(Ground(400, 450, 50, 50, 'ground1'))