from model.Interpretador.IExpressao import IExpressao

class Repita(IExpressao):

    def __init__(self, quantidade, expressao):
        self.quantidade = quantidade
        self.expressao = expressao

    def execute(self):
        for x in range(0, int(self.quantidade)):
            self.expressao.execute()
