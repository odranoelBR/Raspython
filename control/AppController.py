import wx
from view.TelaPrincipal import TelaPrincipal

class AppController():

    def iniciar(self):
        app = wx.App()
        telaprincipal = TelaPrincipal(None, style = wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN | wx.FRAME_NO_TASKBAR ,
                                      title='Raspython', size=(580, 800))

        telaprincipal.Show()
        app.MainLoop()

