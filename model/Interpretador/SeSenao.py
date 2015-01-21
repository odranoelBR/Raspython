from model.Interpretador.IExpressao import IExpressao

class SeSenao(IExpressao):

    def __init__(self, condicao, expressao1, expressao2):
        self.condicao = condicao
        self.expressao1 = expressao1
        self.expressao2 = expressao2

    def execute(self):
        if self.condicao :
            self.expressao.execute()
        else:
            self.expressao2.execute()
