from model.Interpretador.ply import lex

class AnalisadorLexico():

    def __init__(self,statusbar):
        self.statusbar = statusbar
    def getTokenList(self):

        tokens = [
            'DIREITA','ESQUERDA','FRENTE','VOLTA',
            'SE','SENAO',
            'NUMERO',
            'ENQUANTO', 'FACA',
            'SENSORFRENTE',
            'VERDADEIRO',
            'FALSO',
            'COLUNAESQUERDA',
            'COLUNADIREITA',
            'VALOR',
            'CHAVEESQUERDA',
            'CHAVEDIREITA',
            'FIMINSTRUCAO'
            ]
        return tokens

    def scan(self,codigo):

        tokens = self.getTokenList()

        t_FIMINSTRUCAO = r';'
        t_COLUNAESQUERDA = r'\('
        t_COLUNADIREITA = r'\)'
        t_DIREITA = 'DIREITA'
        t_VERDADEIRO = 'VERDADEIRO'
        t_FALSO = 'FALSO'
        t_ESQUERDA = 'ESQUERDA'
        t_FRENTE = 'FRENTE'
        t_VOLTA = 'VOLTA'
        t_SE = 'SE'
        t_SENAO = 'SENAO'
        t_ENQUANTO = 'ENQUANTO'
        t_FACA = 'FACA'
        t_SENSORFRENTE = 'SENSORFRENTE'
        t_NUMERO = r'\d+'
        t_ignore = ' \t'
        def t_error(t):
            self.statusbar.SetBackgroundColour('#FF7373')
            self.statusbar.SetStatusText('Caracter Ilegal' % t.value[0])

            t.lexer.skip(1)

        lex.lex()

        codigo = codigo.upper()
        lex.input(codigo)

        while True:
            tok = lex.token()
            if not tok: break
            # Use token


