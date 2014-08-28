from Compilador.ply import yacc
import time

class AnalisadorSintatico():

    def __init__(self, tokenList, thread):
        self.tokenList = tokenList
        self.thread = thread

    def scan(self,codigo):

        tokens = self.tokenList
        thread = self.thread

        def p_assign_mover_frente(p):
            '''assign : FRENTE '''
            thread.robo.move()

        def p_assign_mover_direita(p):
            '''assign : DIREITA '''
            thread.robo.moveright()

        def p_assign_mover_esquerda(p):
            '''assign : ESQUERDA '''
            thread.robo.moveleft()

        def p_assign_mover_volta(p):
            '''assign : VOLTA '''
            thread.robo.moveup()

        def p_se_stmt(p):
            '''assign : SE COLUNAESQUERDA NUMERO COLUNADIREITA
                    |   SE COLUNAESQUERDA VERDADEIRO COLUNADIREITA
                    |   SE COLUNAESQUERDA FALSO COLUNADIREITA
                    |   SE COLUNAESQUERDA SENSORFRENTE COLUNADIREITA'''

            print p[3]


        def p_error(p):
            print p

        for linha in codigo:
            linha = linha.upper()

            yacc.yacc()
            yacc.parse(linha)

            thread.clock.tick(150)
            thread.screen.blit(thread.background, thread.robo)
            thread.playersprites.update()
            thread.playersprites.draw(thread.screen)

            time.sleep(1)
