
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '!\xe0]\x1a\xd9\x08n\xba\xc3!o+\xc07}M'
    
_lr_action_items = {'COLUNADIREITA':([12,13,14,],[21,22,23,]),'VERDADEIRO':([9,],[13,]),'ENQUANTO':([0,],[1,]),'FRENTE':([0,10,11,21,22,23,24,],[2,15,15,-10,-8,-9,15,]),'SENAO':([15,16,17,18,19,],[-12,24,-13,-14,-11,]),'FACA':([8,21,22,23,],[11,-10,-8,-9,]),'FALSO':([9,],[14,]),'COLUNAESQUERDA':([1,4,],[9,9,]),'SENSORFRENTE':([9,],[12,]),'SE':([0,],[4,]),'VOLTA':([0,10,11,21,22,23,24,],[5,18,18,-10,-8,-9,18,]),'DIREITA':([0,10,11,21,22,23,24,],[3,19,19,-10,-8,-9,19,]),'ESQUERDA':([0,10,11,21,22,23,24,],[7,17,17,-10,-8,-9,17,]),'$end':([2,3,5,6,7,15,16,17,18,19,20,25,],[-1,-2,-4,0,-3,-12,-5,-13,-14,-11,-7,-6,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expressao':([1,4,],[8,10,]),'blocoExecutar':([10,11,24,],[16,20,25,]),'assign':([0,],[6,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assign","S'",1,None,None,None),
  ('assign -> FRENTE','assign',1,'p_assign_mover_frente','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',18),
  ('assign -> DIREITA','assign',1,'p_assign_mover_direita','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',22),
  ('assign -> ESQUERDA','assign',1,'p_assign_mover_esquerda','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',26),
  ('assign -> VOLTA','assign',1,'p_assign_mover_volta','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',30),
  ('assign -> SE expressao blocoExecutar','assign',3,'p_se_stmt','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',34),
  ('assign -> SE expressao blocoExecutar SENAO blocoExecutar','assign',5,'p_se_senao_stmt','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',39),
  ('assign -> ENQUANTO expressao FACA blocoExecutar','assign',4,'p_enquanto_stmt','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',46),
  ('expressao -> COLUNAESQUERDA VERDADEIRO COLUNADIREITA','expressao',3,'p_expressao','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',53),
  ('expressao -> COLUNAESQUERDA FALSO COLUNADIREITA','expressao',3,'p_expressao','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',54),
  ('expressao -> COLUNAESQUERDA SENSORFRENTE COLUNADIREITA','expressao',3,'p_expressao','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',55),
  ('blocoExecutar -> DIREITA','blocoExecutar',1,'p_blocoExecutar','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',62),
  ('blocoExecutar -> FRENTE','blocoExecutar',1,'p_blocoExecutar','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',63),
  ('blocoExecutar -> ESQUERDA','blocoExecutar',1,'p_blocoExecutar','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',64),
  ('blocoExecutar -> VOLTA','blocoExecutar',1,'p_blocoExecutar','/home/muniz/Desenvolvimento/rasp/Raspython/model/Interpretador/AnalisadorSintatico.py',65),
]
