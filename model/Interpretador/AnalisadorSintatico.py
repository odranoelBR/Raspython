from model.Interpretador.Booleano import Booleano
from model.Interpretador.Repita import Repita
from model.Interpretador.Enquanto import Enquanto
from model.Interpretador.SeSenao import SeSenao
from model.Interpretador.Movimento import Movimento
from model.Interpretador.Se import Se
from model.Interpretador.SubExpressao import SubExpressao
from model.Interpretador.ply import yacc

class AnalisadorSintatico:

    def __init__(self, tokenList, tela):
        self.tokenList = tokenList
        self.tela = tela

    def scan(self, codigo):
        thread = self.tela.paineljogo
        tela = self.tela

        def p_instrucao(p):
            """assign : expression"""
            p[1].execute()

        def p_expression(p):
            """expression : terminal_expression
            |   non_terminal_expression"""
            p[0] = p[1]

        def p_sub_expression(p):
            """sub_expression : expression
            |   expression sub_expression"""
            if len(p) > 2:
                p[0] = SubExpressao(p.slice)
            else:
                p[0] = p[1]

        def p_terminal_expression(p):
            """terminal_expression :  DIREITA
            |   CIMA
            |   ESQUERDA
            |   BAIXO"""
            p[0] = Movimento(p[1], thread, tela)

        def p_non_terminal_expression(p):
           """non_terminal_expression : se_stmt
           |    se_senao_stmt
           |    enquanto_stmt
           |    repita_stmt"""
           p[0] = p[1]

        def p_se_stmt(p):
            """se_stmt : SE blocoLogico CHAVESESQUERDA sub_expression CHAVESDIREITA"""
            p[0] = Se(p[2], p[4])

        def p_se_senao_stmt(p):
            """se_senao_stmt : SE blocoLogico  CHAVESESQUERDA sub_expression CHAVESDIREITA SENAO CHAVESESQUERDA sub_expression CHAVESDIREITA"""
            p[0] = SeSenao(p[2], p[4], p[8])

        def p_enquanto_stmt(p):
            """enquanto_stmt : ENQUANTO blocoLogico FACA CHAVESESQUERDA sub_expression CHAVESDIREITA"""
            p[0] = Enquanto(p[2], p[5])

        def p_repita_stmt(p):
            """repita_stmt : REPITA NUMERO VEZES CHAVESESQUERDA sub_expression CHAVESDIREITA"""
            p[0] = Repita(p[2], p[5])

        def p_blocoLogico(p):
            """blocoLogico : COLUNAESQUERDA logico COLUNADIREITA"""
            p[0] = p[2]

        def p_booleanos(p):
            """booleanos :  VERDADEIRO
            |    FALSO
            |    sensorCima
            |    sensorDireita
            |    sensorEsquerda
            |    sensorBaixo
            |    NEGACAO VERDADEIRO
            |    NEGACAO FALSO
            |    NEGACAO sensorCima
            |    NEGACAO sensorDireita
            |    NEGACAO sensorEsquerda
            |    NEGACAO sensorBaixo """
            if len(p) > 2:
                p[0] = Booleano(True,p[2],thread,tela)
            else:
                p[0] = Booleano(False,p[1],thread,tela)

        def p_logico(p):
            """logico : booleanos
            |   booleanos E logico
            |   booleanos OU logico"""
            if len(p) > 2:
               if p[2] == 'E':
                   if p[1].execute() and p[3].execute():
                       p[0] = Booleano(False, 'VERDADEIRO',thread,tela)
                   else:
                       p[0] = Booleano(False, 'FALSO',thread,tela)
               else:
                   if p[1].execute() or p[3].execute():
                       p[0] = Booleano(False, 'VERDADEIRO',thread,tela)
                   else:
                       p[0] = Booleano(False, 'FALSO',thread,tela)

            else:
                p[0] = p[1]

        def p_sensorCima(p):
            """sensorCima : SENSORCIMA"""
            p[0] = 'SENSORCIMA'

        def p_sensorEsquerda(p):
            """sensorEsquerda : SENSORESQUERDA"""
            p[0] = 'SENSORESQUERDA'

        def p_sensorDireita(p):
            """sensorDireita : SENSORDIREITA"""
            p[0] = 'SENSORDIREITA'

        def p_sensorBaixo(p):
            """sensorBaixo : SENSORBAIXO"""
            p[0] = 'SENSORBAIXO'

        def p_error(p):
            self.tela.statusbar.SetBackgroundColour('#FF7373')
            self.tela.statusbar.SetStatusText('Sua instrucao e invalida!', 1)
            raise SyntaxError(p)

        def parsearCodigo(codigo):
            codigo = codigo.upper()
            yacc.parse(codigo)
            atualizarJogo()


        def atualizarJogo():
            thread.jogo.atualizar(self.tela)

        tokens = self.tokenList
        self.parser = yacc.yacc()
        parsearCodigo(codigo)
        atualizarJogo()