import os
import threading
import wx
import time
from model.Jogo import Jogo
import pygame
pygame_init_flag = False

class PainelJogo(wx.Panel):

    def __init__(self, parent, ID, tplSize):
        global pygame
        wx.Panel.__init__(self, parent, ID, size=tplSize)
        os.environ['SDL_WINDOWID'] = str(self.GetHandle())
        self.continuar = True
        self.jogo = Jogo(tplSize)
        self.clock = pygame.time.Clock()
        self.Start()

    def Start(self):
        self.m_bKeepGoing = self.m_bRunning = True
        self.thread = threading.Thread(group=None, target=self.Run, name=None, args=(), kwargs={})
        self.thread.start()
        return

    def __del__(self):
        self.Stop()
        print 'Thread do jogo parou!'
        pygame.quit()

    def Stop(self):
        self.m_bKeepGoing = False
        self.thread.join()

    def IsRunning(self):
        return self.m_bRunning

    def Run(self):
        while self.m_bKeepGoing:
            pygame.display.flip()
            self.m_bRunning = False
            time.sleep(1)

        print 'Loop do jogo foi finalizado!'