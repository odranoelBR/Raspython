from model.Interpretador.IExpressao import IExpressao

class SubExpressao(IExpressao):

    def __init__(self, instrucoes):
        self.instrucoes = instrucoes

    def execute(self):
        self.recursive(self.instrucoes)


    def recursive(self, lista):
        i = 0
        for instrucao in lista:

            if i != 0:
                if (not isinstance(instrucao.value, SubExpressao )):
                    instrucao.value.execute()
                else:
                    self.recursive(instrucao.value.instrucoes)
            i = i+1