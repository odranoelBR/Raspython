import string
from model.Interpretador.AnalisadorLexico import AnalisadorLexico
from model.Interpretador.AnalisadorSintatico import AnalisadorSintatico

class Evento:

    def clickRodar(self, tela):
        codigo = tela.caixadigitacao.GetValue()
        codigoParaAnalisadorLexico = string.replace(codigo,'\t\n' ,' ')
        codigoParaAnalisadorSintatico = codigo.split(';')
        codigoParaAnalisadorSintatico.pop()

        ## Fazemdo a analise lexica
        lexico = AnalisadorLexico(tela)
        lexico.scan(codigoParaAnalisadorLexico)

        ## Fazendo a analise sintatica
        sintatico = AnalisadorSintatico(lexico.getTokenList(), tela)

        for instrucao in codigoParaAnalisadorSintatico:
            sintatico.scan(instrucao)

        tela.PainelJogo.jogo.atualizar()