import os
import threading
import wx
from model.Jogo import Jogo
from model.Sprites.robo import Robo

global pygame # when we import it, let's keep its proper name!
import pygame
pygame_init_flag = False

class ThreadJogo(wx.Panel):
    def __init__(self,parent,ID,tplSize):
        wx.Panel.__init__(self, parent, ID, size=tplSize)

        os.environ['SDL_WINDOWID'] = str(self.GetHandle())

        self.jogo = Jogo()
        # Criando tela no jogo
        self.jogo.screen = pygame.display.set_mode(tplSize)
        # Adicionando o sprite robo no jogo
        self.jogo.robo = Robo()
        # Renderizando o robo no jogo
        self.jogo.playersprites = pygame.sprite.RenderPlain(self.jogo.robo)
        # Criacao da surface
        self.jogo.background = pygame.Surface(self.jogo.screen.get_size())
        self.jogo.background.convert()
        self.jogo.background.fill((255,255,255))
        self.jogo.time = pygame.time
        self.clock = pygame.time.Clock()

        self.Start()

    def Start(self):
        #I rewrote this to use the higherlevel threading module
        self.m_bKeepGoing = self.m_bRunning = True
        self.thread = threading.Thread(group=None, target=self.Run, name=None,
                                       args=(), kwargs={})
        self.thread.start()

    def __del__(self):
        self.thread.Stop()
        print "Thread Parou!"
        pygame.quit()

    def Run(self):
        while self.m_bKeepGoing:
            self.clock.tick(150)

        self.m_bRunning = False;
        print "Loop do jogo parou de executar!"

