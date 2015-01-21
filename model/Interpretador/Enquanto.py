from model.Interpretador.IExpressao import IExpressao

class Enquanto(IExpressao):

    def __init__(self, condicao, expressao):
        self.condicao = condicao
        self.expressao = expressao

    def execute(self):
       while self.condicao:
           self.expressao.execute()
