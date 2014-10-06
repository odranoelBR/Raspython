import threading
import pygame
from Labirinto import Labirinto

from robo import Robo

import time

class SDLThread:
    def __init__(self,screen):
        self.m_bKeepGoing = self.m_bRunning = False

        self.screen = screen

        # Criacao do robo
        self.robo = Robo()

        self.playersprites = pygame.sprite.RenderPlain(self.robo)

        # Criacao da surface
        self.background = pygame.Surface(screen.get_size())
        self.background.convert()
        self.background.fill((255,255,255))
        self.time = time
        self.clock = pygame.time.Clock()

        self.thread = None
        self.proximaAcao = None
        self.init = True

        camadaLabirinto = pygame.Surface(screen.get_size())
        camadaLabirinto = camadaLabirinto.convert_alpha()
        camadaLabirinto.fill((0,0,0,0,))
        self.labirinto = Labirinto(camadaLabirinto)

        # Desenha sprites na surface
        while 1 :
            self.playersprites.draw(screen)
            self.playersprites.update()
            self.screen.blit(self.background, (0,0))
            self.labirinto.update()
            self.labirinto.draw(screen)

            pygame.display.flip()


    def Start(self):
        #I rewrote this to use the higherlevel threading module
        self.m_bKeepGoing = self.m_bRunning = True
        self.thread = threading.Thread(group=None, target=self.Run, name=None,
                                       args=(), kwargs={})
        self.thread.start()

    def Stop(self):
        self.m_bKeepGoing = False
        #this important line make sure that the draw thread exits before
        #pygame.quit() is called so there is no errors
        self.thread.join()

    def IsRunning(self):
        return self.m_bRunning

    def Run(self):
        while self.m_bKeepGoing:
            self.clock.tick(150)


        self.m_bRunning = False;
        print "pygame draw loop exited"