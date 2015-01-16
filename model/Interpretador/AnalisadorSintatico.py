from model.Interpretador.ply import yacc

class AnalisadorSintatico:

    def __init__(self, tokenList, tela):
        self.tokenList = tokenList
        self.tela = tela

    def scan(self, codigo):
        thread = self.tela.paineljogo

        def p_assign_mover_frente(p):
            """assign : CIMA """
            thread.jogo.robo.moveFront()

        def p_assign_mover_direita(p):
            """assign : DIREITA """
            thread.jogo.robo.moveRight()

        def p_assign_mover_esquerda(p):
            """assign : ESQUERDA """
            thread.jogo.robo.moveLeft()

        def p_assign_mover_volta(p):
            """assign : BAIXO """
            thread.jogo.robo.moveBack()

        def p_se_stmt(p):
            """assign : SE blocoLogico blocoExecutar """
            if p[2]:
                parsearCodigo(p[3])

        def p_se_senao_stmt(p):
            """assign : SE blocoLogico  blocoExecutar SENAO blocoExecutar"""
            if p[2]:
                parsearCodigo(p[3])
            else:
                parsearCodigo(p[5])

        def p_enquanto_stmt(p):
            """assign : ENQUANTO blocoLogico FACA blocoExecutar"""
            while p[2]:
                parsearCodigo(p[4])
                atualizarJogo()

        def p_faca_stmt(p):
            """assign : REPITA NUMERO VEZES blocoExecutar"""
            quantidade = p[2]
            for x in xrange(int(quantidade)):
                parsearCodigo(p[4])
                atualizarJogo()

        def p_blocoLogico(p):
            """blocoLogico : COLUNAESQUERDA logico
            | COLUNAESQUERDA NEGACAO logico"""

            if p[2] == '!':
                p[0] = not p[3]
            else:
                p[0] = p[2]

        def p_logico(p):
            """logico :  VERDADEIRO COLUNADIREITA
            |    FALSO COLUNADIREITA
            |    sensorCima COLUNADIREITA
            |    sensorDireita COLUNADIREITA
            |    sensorEsquerda COLUNADIREITA
            |    sensorBaixo COLUNADIREITA"""

            if p[1] == 'FALSO' or p[1] == False:
                p[0] = False
            else:
                p[0] = True

        def p_sensorCima(p):
            """sensorCima : SENSORCIMA"""

            p[0] = thread.jogo.robo.temColisaoCima(self.tela.paineljogo.jogo.grupowalls)

        def p_sensorEsquerda(p):
            """sensorEsquerda : SENSORESQUERDA"""

            p[0] = thread.jogo.robo.temColisaoEsquerda(self.tela.paineljogo.jogo.grupowalls)

        def p_sensorDireita(p):
            """sensorDireita : SENSORDIREITA"""

            p[0] = thread.jogo.robo.temColisaoDireita(self.tela.paineljogo.jogo.grupowalls)

        def p_sensorBaixo(p):
            """sensorBaixo : SENSORBAIXO"""

            p[0] = thread.jogo.robo.temColisaoBaixo(self.tela.paineljogo.jogo.grupowalls)


        def p_blocoExecutar(p):
            """blocoExecutar :  DIREITA
            |   CIMA
            |   ESQUERDA
            |   BAIXO"""
            p[0] = p[1]

        def p_error(p):
            self.tela.statusbar.SetBackgroundColour('#FF7373')
            self.tela.statusbar.SetStatusText('Sua instrucao e invalida!', 1)
            raise SyntaxError(p)

        def parsearCodigo(codigo):
            codigo = codigo.upper()
            yacc.parse(codigo)

        def atualizarJogo():
            thread.jogo.atualizar(self.tela)

        tokens = self.tokenList
        self.parser = yacc.yacc()
        parsearCodigo(codigo)
        atualizarJogo()