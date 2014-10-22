import string
from model.Interpretador.AnalisadorLexico import AnalisadorLexico
from model.Interpretador.AnalisadorSintatico import AnalisadorSintatico

class Evento:

    def clickRodar(self, tela):
        codigo = tela.caixadigitacao.GetValue()
        codigoParaAnalisadorSintatico = codigo.split('\n')

        ## Fazemdo a analise lexica
        lexico = AnalisadorLexico(tela)
        for instrucao in codigoParaAnalisadorSintatico:
            lexico.scan(instrucao)

        ## Fazendo a analise sintatica
        sintatico = AnalisadorSintatico(lexico.getTokenList(), tela)

        for instrucao in codigoParaAnalisadorSintatico:
            sintatico.scan(instrucao)

        tela.paineljogo.jogo.atualizar(tela)