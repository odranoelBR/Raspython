import string
from model.Interpretador.AnalisadorLexico import AnalisadorLexico
from model.Interpretador.AnalisadorSintatico import AnalisadorSintatico

class Evento:

    def clickRodar(self, tela):

        codigo = tela.caixadigitacao.GetValue()
        codigo = string.replace(codigo, '\t', '')
        codigo = string.replace(codigo, '\n', '')
        codigo = codigo.split(' ')

        ## Fazemdo a analise lexica
        lexico = AnalisadorLexico(tela)
        for token in codigo:
            lexico.scan(token)


        ## Fazendo a analise sintatica
        sintatico = AnalisadorSintatico(lexico.getTokenList(), tela)

        #for instrucao in codigoParaAnalisadorSintatico:
        for token in codigo:
            sintatico.scan(token)

        tela.paineljogo.jogo.atualizar(tela)