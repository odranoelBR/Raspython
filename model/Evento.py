
from model.Interpretador.AnalisadorLexico import AnalisadorLexico
from model.Interpretador.AnalisadorSintatico import AnalisadorSintatico

class Evento:

    def clickRodar(self, tela):
        codigo = tela.caixadigitacao.GetValue()
        codigoParaAnalisadorSintatico = codigo.replace('\n','')
        codigoParaAnalisadorSintatico = codigoParaAnalisadorSintatico.split(';')
        codigoParaAnalisadorSintatico.pop()
        lexico = AnalisadorLexico(tela)
        for instrucao in codigoParaAnalisadorSintatico:
            lexico.scan(instrucao)

        sintatico = AnalisadorSintatico(lexico.getTokenList(), tela)
        for instrucao in codigoParaAnalisadorSintatico:
            sintatico.scan(instrucao)

        tela.paineljogo.jogo.atualizar(tela)
        tela.statusbar.SetStatusText('',0)
        tela.statusbar.SetStatusText('',1)
        tela.statusbar.SetBackgroundColour('#035A66')

    def clickReset(self, tela):
        tela.caixadigitacao.Value = ''
        tela.paineljogo.jogo.robo.posicaoinicial()
        tela.paineljogo.jogo.atualizar(tela)
        tela.statusbar.SetStatusText('',0)
        tela.statusbar.SetStatusText('',1)
        tela.statusbar.SetBackgroundColour('#035A66')
