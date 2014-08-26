import ast
from Compilador.ply import lex, yacc

def scan(codigo,thread):

    codigo = codigo.upper()

    tokens = [
        'DIREITA','ESQUERDA','FRENTE','VOLTA',
        'SE','SENAO',
        'ENQUANTO', 'FACA',
        'SENSORFRENTE',
        'IMPRIMA',
        'VALORMOV',
        'SE',
        'COLUNA'
    ]

    t_ignore = ' \t'

    def t_error(t):
        print("Caracter Ilegal %s" % t.value[0])
        t.lexer.skip(1)

    t_COLUNA = r':'
    t_DIREITA = 'DIREITA'
    t_ESQUERDA = 'ESQUERDA'
    t_FRENTE = 'FRENTE'
    t_VOLTA = 'VOLTA'
    t_SE = 'SE'
    t_SENAO = 'SENAO'
    t_ENQUANTO = 'ENQUANTO'
    t_FACA = 'FACA'
    t_SENSORFRENTE = 'SENSORFRENTE'
    t_IMPRIMA = 'IMPRIMA'
    t_VALORMOV = r'\d+'

    RESERVED = {
      "if": "SE",
      }
    lex.lex()
    lex.input(codigo)

    while True:
        tok = lex.token()
        if not tok: break
        # Use token

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




    def p_error(p):
        print p


    yacc.yacc()
    yacc.parse(codigo)