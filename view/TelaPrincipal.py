import os
import wx
import sys

from model.Evento import Evento
from view.PainelJogo import PainelJogo
from view.ToolBar import ToolBar

class TelaPrincipal(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(TelaPrincipal, self).__init__(*args, **kwargs)

        self.BackgroundColour = '#97CD56'
        self.SetWindowStyle(wx.DOUBLE_BORDER)
        # Exibe a tela
        self.Show()
        # Adiciona os elementos da tela
        self.adicionarWidgets()
        # Injeta os eventos
        self.eventos = Evento()
        # Anexa os eventos que podem acontecer
        self.anexarEventos()
        # Centraliza o frame no monitor
        self.Centre()

        for control, x, y, width, height in \
                 [
                 (self.toolbar, 15, 5, 965, 50),
                 (self.caixadigitacao, 580, 60, 400, 300),
                 (self.botao, 740, 380, 80, 40),
                 (self.PainelJogo, 15, 60, 550, 500)]:
            control.SetDimensions(x=x, y=y, width=width, height=height)



    def adicionarWidgets(self):

        self.toolbar = ToolBar(self)

        self.PainelJogo = PainelJogo(self, -1, (550, 500))

        self.botao = wx.Button(self, label="Rodar")

        self.caixadigitacao = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.caixadigitacao.BackgroundColour = '#FFFFFF'

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(2)
        self.statusbar.SetStatusWidths([565,435])
        self.statusbar.SetBackgroundColour('#48372D')
        self.statusbar.Refresh()

    def anexarEventos(self):
        for control, event, handler in \
                [(self.botao, wx.EVT_BUTTON, self.onClick),
                ]:
            control.Bind(event, handler)

    def onClick(self,event):
        self.eventos.clickRodar(self)
