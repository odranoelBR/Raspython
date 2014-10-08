import os
import wx

from model.Threads.sdlThread import SDLThread


global pygame # when we import it, let's keep its proper name!
import pygame
pygame_init_flag = False

class SDLPanel(wx.Panel):
    def __init__(self,parent,ID,tplSize):
        wx.Panel.__init__(self, parent, ID, size=tplSize)
        global pygame_init_flag

        os.environ['SDL_WINDOWID'] = str(self.GetHandle())

        pygame_init_flag = True #make sure we know that pygame has been imported
        window = pygame.display.set_mode(tplSize)

        pygame.display.flip()
        self.thread = SDLThread(window)
        self.thread.Start()

    def __del__(self):
        self.thread.Stop()
        print "thread stoped"
        #very important line, this makes sure that pygame exits before we
        #reinitialize it other wise we get errors
        pygame.quit()