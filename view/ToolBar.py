import wx

class ToolBar(wx.ToolBar):

    def __init__(self, parent):
        wx.ToolBar.__init__(self, parent)
        self.parent = parent
        self.BackgroundColour = '#0A8B9E'
        self.SetSize([80, 50])
        self.sair = self.AddLabelTool(wx.ID_ANY, 'Sair', wx.Bitmap('view/img/close.png'))
        self.info = self.AddLabelTool(wx.ID_ANY, 'Info', wx.Bitmap('view/img/info.gif'))
        self.Realize()
        self.anexarEventos()

    def onQuit(self, e):
        self.parent.Close()

    def onInfo(self, e):
        wx.MessageBox('Tutorial! \n Voce deve escrever um codigo na caixa branca, que solucione o jogo.\nLembre-se de pular linhas para cada instrucao.Para isso voce conta com os comandos de movimento : \n         1 ) cima \n         2 ) baixo \n         3 ) esquerda \n         4 ) direita \n\nPossui a condicional SE exemplo :\n         SE (verdadeiro) \n         cima \n         SE (Sensorfrente) \n         baixo \n\nPossui o iterador REPITA exemplo :\n         REPITA 10 VEZES cima \n         REPITA 3 VEZES esquerda \n\nPossui o iterador ENQUANTO exemplo : \n         ENQUANTO (verdadeiro) FACA direita \n         ENQUANTO (sensorfrente) FACA esquerda \n', 'Tutorial', wx.OK | wx.ICON_INFORMATION)

    def anexarEventos(self):
        self.Bind(wx.EVT_TOOL, self.onQuit, self.sair)
        self.Bind(wx.EVT_TOOL, self.onInfo, self.info)