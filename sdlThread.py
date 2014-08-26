import threading
import pygame
from robo import Robo

import time

class SDLThread:
    def __init__(self,screen):
        self.m_bKeepGoing = self.m_bRunning = False
        self.robo = Robo()
        self.screen = screen
        self.playersprites = pygame.sprite.RenderPlain((self.robo))
        self.background = pygame.Surface(screen.get_size())
        self.time = time
        self.clock = pygame.time.Clock()
        self.playersprites.draw(screen)
        self.thread = None
        self.proximaAcao = None
        self.init = True

        self.screen.blit(self.background, self.robo)
        self.playersprites.update()


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

            #if event.type == KEYDOWN:
           # if event.key == pygame.K_DOWN:
            #    self.robo.movedown()
            #if event.key == pygame.K_LEFT:
             #   self.robo.moveleft()
            #if event.key == pygame.K_RIGHT:
                #self.robo.moveright()

            #elif event.type == KEYUP:
             #   if event.key == K_UP or event.key == K_DOWN     \
              #          or event.key == K_LEFT or event.key == K_RIGHT:
               #     self.robo.movepos = [0,0]


        self.m_bRunning = False;
        print "pygame draw loop exited"