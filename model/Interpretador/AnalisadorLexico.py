from model.Interpretador.ply import lex

class AnalisadorLexico:

    def __init__(self, tela):
        self.tela = tela

    def getTokenList(self):
        tokens = ['DIREITA',
         'ESQUERDA',
         'CIMA',
         'BAIXO',
         'SE',
         'SENAO',
         'E',
         'OU',
         'VEZES',
         'ENQUANTO',
         'FACA',
         'SENSORCIMA',
         'SENSORESQUERDA',
         'SENSORDIREITA',
         'SENSORBAIXO',
         'NEGACAO',
         'NUMERO',
         'VERDADEIRO',
         'FALSO',
         'REPITA',
         'COLUNAESQUERDA',
         'COLUNADIREITA',
         'CHAVESESQUERDA',
         'CHAVESDIREITA']
        return tokens

    def scan(self, codigo):
        tokens = self.getTokenList()
        t_REPITA = 'REPITA'
        t_VEZES = 'VEZES'
        t_COLUNAESQUERDA = '\\('
        t_COLUNADIREITA = '\\)'
        t_DIREITA = 'DIREITA'
        t_VERDADEIRO = 'VERDADEIRO'
        t_FALSO = 'FALSO'
        t_ESQUERDA = 'ESQUERDA'
        t_BAIXO = 'BAIXO'
        t_CIMA = 'CIMA'
        t_SE = 'SE'
        t_E = 'E'
        t_OU = 'OU'
        t_SENAO = 'SENAO'
        t_ENQUANTO = 'ENQUANTO'
        t_FACA = 'FACA'
        t_SENSORCIMA = 'SENSORCIMA'
        t_SENSORESQUERDA = 'SENSORESQUERDA'
        t_SENSORDIREITA = 'SENSORDIREITA'
        t_SENSORBAIXO = 'SENSORBAIXO'
        t_CHAVESESQUERDA = '\\{'
        t_CHAVESDIREITA = '\\}'
        t_NEGACAO = '\\!'
        t_NUMERO = '\\d+'
        t_ignore = ' \t'

        def t_error(t):
            self.tela.statusbar.SetBackgroundColour('#FF8379')
            self.tela.statusbar.SetStatusText('Existe um caracter ilegal ou desconhecido!%s ' % t.value, 0)
            t.lexer.skip(5)

        lex.lex()
        codigo = codigo.upper()
        lex.input(codigo)
        while True:
            tok = lex.token()
            if not tok:
                break