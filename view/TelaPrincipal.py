import string
import wx
import pygame

from model.Interpretador.AnalisadorLexico import AnalisadorLexico
from model.Interpretador.AnalisadorSintatico import AnalisadorSintatico
from model.Threads.ThreadJogo import ThreadJogo


class TelaPrincipal(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(TelaPrincipal, self).__init__(*args, **kwargs)

        self.Show() # Exibe a tela
        self.adicionarWidgets() # Adiciona os elementos da tela
        self.anexarEventos() # Anexa os eventos que pode acontecer

        for control, x, y, width, height in \
                 [(self.caixadigitacao, 5, 480, 450, 280),
                 (self.botao, 470, 600, 80, 40),
                 (self.ThreadJogo, 5, 5, 550, 440)]:
            control.SetDimensions(x=x, y=y, width=width, height=height)

    def adicionarWidgets(self):
        self.ThreadJogo = ThreadJogo(self, -1, (550, 500))
        self.botao = wx.Button(self, label="Rodar")
        self.caixadigitacao = wx.TextCtrl(self, style=wx.TE_MULTILINE)

    def anexarEventos(self):
        for control, event, handler in \
                [(self.botao, wx.EVT_BUTTON, self.onClick)
                ]:
            control.Bind(event, handler)

    def onClick(self, event):
        ##codigoExplodido = string.split(self.programa.GetValue(), '\n')
        codigo = self.caixadigitacao.GetValue()
        codigo = string.replace(codigo,'\n' ,' ')

        ## Fazemdo a analise lexica
        lexico = AnalisadorLexico()
        lexico.scan(codigo)
        ## Fazendo a analise sintatica
        sintatico = AnalisadorSintatico(lexico.getTokenList(), self.ThreadJogo)
        sintatico.scan(codigo)

        pygame.display.flip()
