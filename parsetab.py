
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x1fZ\xe4\xe6\x86\xec\x13>\xb6$\x8c\xa5\r\x9e&h'
    
_lr_action_items = {'$end':([1,2,3,4,5,],[-3,-4,0,-1,-2,]),'VOLTA':([0,],[2,]),'DIREITA':([0,],[5,]),'ESQUERDA':([0,],[1,]),'FRENTE':([0,],[4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assign':([0,],[3,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assign","S'",1,None,None,None),
  ('assign -> FRENTE','assign',1,'p_assign_mover_frente','/home/muniz/Desenvolvimento/raspython/Compilador/lex.py',50),
  ('assign -> DIREITA','assign',1,'p_assign_mover_direita','/home/muniz/Desenvolvimento/raspython/Compilador/lex.py',54),
  ('assign -> ESQUERDA','assign',1,'p_assign_mover_esquerda','/home/muniz/Desenvolvimento/raspython/Compilador/lex.py',58),
  ('assign -> VOLTA','assign',1,'p_assign_mover_volta','/home/muniz/Desenvolvimento/raspython/Compilador/lex.py',62),
]
