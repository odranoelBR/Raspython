import wx
from view.TelaPrincipal import TelaPrincipal

class AppController():

    def iniciar(self):
        app = wx.App()
        telaprincipal = TelaPrincipal(None,
                                      style = wx.NO_BORDER,
                                      title='Raspython', size=(1000, 600))

        app.MainLoop()

