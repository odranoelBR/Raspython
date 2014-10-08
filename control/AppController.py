import wx
from view.TelaPrincipal import TelaPrincipal

class AppController():

    def iniciar(self):
        app = wx.App(False)
        telaprincipal = TelaPrincipal(None, title='Raspython', size=(560, 768))

        telaprincipal.Show()
        app.MainLoop()

