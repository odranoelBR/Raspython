import wx
import os
from view.TelaPrincipal import TelaPrincipal

class AppController():

    def iniciar(self):
        os.environ.__setitem__('conexaoRobo', 'False')

        app = wx.App()
        telaprincipal = TelaPrincipal(None,
                                      style = wx.NO_BORDER,
                                      title='Raspython', size=(1000, 600))

        app.MainLoop()

