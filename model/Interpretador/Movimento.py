from model.Interpretador.IExpressao import IExpressao

class Movimento(IExpressao):

    def __init__(self, nome, thread, tela):
        self.nome = nome
        self.thread = thread
        self.tela = tela

    def execute(self):
        if self.nome == 'CIMA':
            self.thread.jogo.robo.moveFront()
        if self.nome == 'BAIXO':
            self.thread.jogo.robo.moveBack()
        if self.nome == 'ESQUERDA':
            self.thread.jogo.robo.moveLeft()
        if self.nome == 'DIREITA':
            self.thread.jogo.robo.moveRight()

        self.thread.jogo.atualizar(self.tela)
