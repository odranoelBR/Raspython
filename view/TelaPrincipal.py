import wx,os
from model.Evento import Evento
from view.PainelJogo import PainelJogo
from view.ToolBar import ToolBar

class TelaPrincipal(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(TelaPrincipal, self).__init__(*args, **kwargs)
        self.BackgroundColour = '#0A8B9E'
        self.SetWindowStyle(wx.DOUBLE_BORDER)
        self.Show()
        self.adicionarWidgets()
        self.eventos = Evento()
        self.anexarEventos()
        self.Centre()
        for control, x, y, width, height in [(self.mensagem,
          5,
          5,
          450,
          50),
         (self.toolbar,
          870,
          5,
          140,
          50),
         (self.caixadigitacao,
          580,
          60,
          400,
          300),
         (self.botao,
          680,
          380,
          80,
          40),
          (self.botaoReset,
          800,
          380,
          80,
          40),

         (self.paineljogo,
          55,
          75,
          400,
          400)]:
            control.SetDimensions(x=x, y=y, width=width, height=height)

    def adicionarWidgets(self):
        self.toolbar = ToolBar(self)
        self.paineljogo = PainelJogo(self, -1, (400, 400))
        self.mensagem = wx.StaticText(self, label='O zumbi precisa comer cerebros! Ajude-o a chegar em um.', style=wx.ALIGN_CENTRE)
        font = wx.Font(16, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.mensagem.ForegroundColour = '#FFFFFF'
        self.mensagem.SetFont(font)
        self.botao = wx.Button(self, label='Rodar')
        self.botaoReset = wx.Button(self, label='Reiniciar')
        self.caixadigitacao = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.caixadigitacao.BackgroundColour = '#FFFFFF'
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([565, 435])
        self.statusbar.SetBackgroundColour('#035A66')
        self.statusbar.Refresh()

    def anexarEventos(self):
        for control, event, handler in [(self.botao, wx.EVT_BUTTON, self.onClick),
                                        (self.botaoReset, wx.EVT_BUTTON, self.onClickReset)]:
            control.Bind(event, handler)

    def onClick(self, event):
        self.eventos.clickRodar(self)

    def onClickReset(self, event):
        self.eventos.clickReset(self)
