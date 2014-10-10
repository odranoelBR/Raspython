import time
import pygame

from model.Interpretador.ply import yacc


class AnalisadorSintatico():

    def __init__(self, tokenList, thread):
        self.tokenList = tokenList
        self.thread = thread

    def scan(self,codigo):
        thread = self.thread

        def p_assign_mover_frente(p):
            '''assign : FRENTE '''
            thread.jogo.robo.move()

        def p_assign_mover_direita(p):
            '''assign : DIREITA '''
            thread.jogo.robo.moveright()

        def p_assign_mover_esquerda(p):
            '''assign : ESQUERDA '''
            thread.jogo.robo.moveleft()

        def p_assign_mover_volta(p):
            '''assign : VOLTA '''
            thread.jogo.robo.moveback()

        def p_se_stmt(p):
            '''assign : SE expressao  blocoExecutar '''
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


        def p_expressao(p):
            '''expressao :  COLUNAESQUERDA VERDADEIRO COLUNADIREITA
                        |   COLUNAESQUERDA FALSO COLUNADIREITA
                        |   COLUNAESQUERDA SENSORFRENTE COLUNADIREITA'''
            if(p[2] == 'FALSO'):
                p[0] = False
            else:
                p[0] = True

        def p_blocoExecutar(p):
            '''blocoExecutar :  DIREITA
                            |   FRENTE
                            |   ESQUERDA
                            |   VOLTA'''
            p[0] = p[1]

        def p_error(p):
            print p

        def parsearCodigo(codigo):
            codigo = codigo.upper()
            yacc.parse(codigo)

        def atualizarJogo():
            thread.clock.tick(150)
            thread.jogo.screen.blit(thread.jogo.background, thread.jogo.robo)
            thread.jogo.playersprites.update(thread.jogo.grupowalls)
            thread.jogo.grupowalls.draw(thread.jogo.screen)
            thread.jogo.playersprites.draw(thread.jogo.screen)
            pygame.display.flip()

            time.sleep(1)

        tokens = self.tokenList
        self.parser = yacc.yacc()

        parsearCodigo(codigo)
        atualizarJogo()
