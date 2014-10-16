import wx
from view.TelaPrincipal import TelaPrincipal

class AppController():

    def iniciar(self):
        app = wx.App()
        telaprincipal = TelaPrincipal(None, title='Raspython', size=(580, 800))

        telaprincipal.Show()
        app.MainLoop()

