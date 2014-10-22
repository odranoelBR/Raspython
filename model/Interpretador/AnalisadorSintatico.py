from model.Interpretador.ply import yacc

class AnalisadorSintatico():

    def __init__(self, tokenList, tela):
        self.tokenList = tokenList
        self.tela = tela

    def scan(self,codigo):
        thread = self.tela.paineljogo

        def p_assign_mover_frente(p):
            '''assign : CIMA '''
            thread.jogo.robo.move()

        def p_assign_mover_direita(p):
            '''assign : DIREITA '''
            thread.jogo.robo.moveright()

        def p_assign_mover_esquerda(p):
            '''assign : ESQUERDA '''
            thread.jogo.robo.moveleft()

        def p_assign_mover_volta(p):
            '''assign : BAIXO '''
            thread.jogo.robo.moveback()


        def p_stmt(p):
            '''assign:  se_stmt
                    |   enquanto_stmt
                    |   comando_stmt
                    |   faca_stmt'''

        def p_se_stmt(p):
            '''se : SE boolean_expression stmt'''
            if (p[2]):
                parsearCodigo(p[3])

        def p_se_senao_stmt(p):
            '''assign : SE expressao  blocoExecutar SENAO blocoExecutar'''
            if (p[2]):
                parsearCodigo(p[3])
            else:
                parsearCodigo(p[5])

        def p_enquanto_stmt(p):
            '''assign : ENQUANTO expressao FACA blocoExecutar'''
            while (p[2]):
                parsearCodigo(p[4])
                atualizarJogo()

        def p_faca_stmt(p):
            '''assign : FACA NUMERO VEZES blocoExecutar'''
            quantidade = p[2]
            for x in xrange(int(quantidade)):
                parsearCodigo(p[4])
                atualizarJogo()


        def p_boolean_expression(p):
            '''boolean_expression : COLUNAESQUERDA VERDADEIRO COLUNADIREITA
                                |   COLUNAESQUERDA FALSO COLUNADIREITA
                                |   COLUNAESQUERDA SENSORFRENTE COLUNADIREITA'''
            if(p[2] == 'FALSO'):
                p[0] = False
            else:
                p[0] = True

        def p_comando_stmt(p):
            '''comando_stmt :  DIREITA
                            |   CIMA
                            |   ESQUERDA
                            |   BAIXO'''
            p[0] = p[1]


        def p_error(p):
            self.tela.statusbar.SetBackgroundColour('#FF7373')
            self.tela.statusbar.SetStatusText("Sua instrucao e invalida!",1)

        def parsearCodigo(codigo):
            codigo = codigo.upper()
            yacc.parse(codigo)

        def atualizarJogo():
            thread.jogo.atualizar(self.tela)

        tokens = self.tokenList
        self.parser = yacc.yacc()

        parsearCodigo(codigo)
        atualizarJogo()
