import string
import time
import wx
import pygame


from Compilador.AnalisadorLexico import AnalisadorLexico
from Compilador.AnalisadorSintatico import AnalisadorSintatico
from sdPanel import SDLPanel


class FrameWithForms(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(FrameWithForms, self).__init__(*args, **kwargs)
        self.colors = ['Se', 'Senao']
        self.Show()
        self.createControls()
        self.bindEvents()

        for control, x, y, width, height in \
                [(self.colorRadioBox, 5, 530, 775, 180),
                 (self.programa, 5, 5, 460, 500),
                 (self.botao, 850, 600, 80, 40),
                 (self.jogo, 470, 5, 530, 500)]:
            control.SetDimensions(x=x, y=y, width=width, height=height)


    def createControls(self):
        self.jogo = SDLPanel(self, -1, (530, 500))
        self.botao = wx.Button(self, label="Rodar")

        self.programa = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.colorRadioBox = wx.RadioBox(self,
                                         label="Gramatica do codigo",
                                         choices=self.colors, majorDimension=3, style=wx.RA_SPECIFY_COLS)

    def bindEvents(self):
        for control, event, handler in \
                [(self.botao, wx.EVT_BUTTON, self.onClick)
                ]:
            control.Bind(event, handler)

    def onClick(self, event):
        texto = string.split(self.programa.GetValue(), '\n')

        for linha in texto:
            ## Fazemdo a analise lexica
            lexico = AnalisadorLexico()
            lexico.scan(linha)
            ## Fazendo a analise sintatica
            sintatico = AnalisadorSintatico(lexico.getTokenList(), self.jogo.thread)
            sintatico.scan(linha)


        self.jogo.thread.clock.tick(150)
        self.jogo.thread.screen.blit(self.jogo.thread.background, self.jogo.thread.robo)
        self.jogo.thread.playersprites.update()
        self.jogo.thread.playersprites.draw(self.jogo.thread.screen)
        pygame.display.flip()

        time.sleep(1)


app = wx.App(False)
frame = FrameWithForms(None, title='Raspython', size=(1024, 768))
frame.Show()
app.MainLoop()