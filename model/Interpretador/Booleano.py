from model.Interpretador.IExpressao import IExpressao

class Booleano(IExpressao):

    def __init__(self, negacao, expressao, thread, tela):
        self.negacao = negacao
        self.expressao = expressao
        self.thread = thread
        self.tela = tela

    def execute(self):
        retorno = False

        if self.expressao == 'SENSORDIREITA' :
            if self.thread.jogo.robo.temColisaoDireita(self.tela.paineljogo.jogo.grupowalls):
                retorno = True
        if self.expressao == 'SENSORESQUERDA' :
            if self.thread.jogo.robo.temColisaoEsquerda(self.tela.paineljogo.jogo.grupowalls):
                retorno = True
        if self.expressao == 'SENSORCIMA' :
            if self.thread.jogo.robo.temColisaoEsquerda(self.tela.paineljogo.jogo.grupowalls):
                retorno = True
        if self.expressao == 'SENSORBAIXO' :
            if self.thread.jogo.robo.temColisaoEsquerda(self.tela.paineljogo.jogo.grupowalls):
                retorno = True

        if self.expressao == 'VERDADEIRO':
            retorno = True
        if self.expressao == 'FALSO':
            retorno = False

        if self.negacao:
            return not retorno

        return retorno