from model.Interpretador.IExpressao import IExpressao

class Se(IExpressao):

    def __init__(self, condicao, expressao):
        self.condicao = condicao
        self.expressao = expressao

    def execute(self):
        if self.condicao :
            self.expressao.execute()
