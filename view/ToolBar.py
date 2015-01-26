import wx
from model.HelpWindow import HelpWindow
from model.RoboControllerApi import RoboControllerApi

class ToolBar(wx.ToolBar):

    def __init__(self, parent):
        wx.ToolBar.__init__(self, parent)
        self.parent = parent
        self.BackgroundColour = '#0A8B9E'
        self.SetSize([80, 50])
        self.ligarRobo = self.AddLabelTool(1, 'iniciandoConexao', wx.Bitmap('view/img/wioff.png'))
        self.info = self.AddLabelTool(2, 'Info', wx.Bitmap('view/img/info.gif'))
        self.sair = self.AddLabelTool(3, 'Sair', wx.Bitmap('view/img/close.png'))
        self.Realize()
        self.anexarEventos()
        self.roboControllerApi = RoboControllerApi()

    def onQuit(self, e):
        self.parent.Close()

    def iniciandoConexao(self,e):

        if self.roboControllerApi.testConnection():
            wx.MessageBox('Conexao com robo estabelecida com sucesso!', 'Info',
            wx.OK | wx.ICON_INFORMATION)
            self.RemoveTool(1)
            self.RemoveTool(2)
            self.RemoveTool(3)
            self.AddLabelTool(1, 'iniciandoConexao', wx.Bitmap('view/img/wion.png'))
            self.info = self.AddLabelTool(2, 'Info', wx.Bitmap('view/img/info.gif'))
            self.sair = self.AddLabelTool(3, 'Sair', wx.Bitmap('view/img/close.png'))
            self.Realize()
        else:
            wx.MessageBox('Desculpe. A conexao nao pode ser estabelecida!\n'
                          'Verifique se esta conectado no wifi do robo.', 'Info',
            wx.OK | wx.ICON_INFORMATION)

    def onInfo(self, e):
        HelpWindow(None, -1, 'HelpWindow')

    def anexarEventos(self):
        self.Bind(wx.EVT_TOOL, self.onInfo, self.info)
        self.Bind(wx.EVT_TOOL, self.iniciandoConexao, self.ligarRobo)
        self.Bind(wx.EVT_TOOL, self.onQuit, self.sair)