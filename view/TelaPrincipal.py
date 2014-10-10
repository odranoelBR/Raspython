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
                 [(self.caixadigitacao, 5, 510, 450, 240),
                 (self.botao, 470, 600, 80, 40),
                 (self.ThreadJogo, 5, 5, 550, 500)]:
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
        codigo = string.replace(codigo,'\t\n' ,' ')

        codigoParaAnaliseLexica = codigo.split(' ')
        codigoParaAnaliseSintantica = codigo.split(';')

        ## Fazemdo a analise lexica
        lexico = AnalisadorLexico()
        for token in codigoParaAnaliseLexica:
            lexico.scan(token)

        ## Fazendo a analise sintatica
        sintatico = AnalisadorSintatico(lexico.getTokenList(), self.ThreadJogo)
        for instrucao in codigoParaAnaliseSintantica:
            sintatico.scan(instrucao)

        pygame.display.flip()

