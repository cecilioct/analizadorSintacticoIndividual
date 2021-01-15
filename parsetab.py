
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNARleftSUMARESTAleftMULTDIVrightUMINUSAND ASIGNAR CADENA COMA COMDOB CORDER CORIZQ COUT DECIMAL DISTINTO DIV ENTERO FINALLY FLOAT GET IDENTIFICADOR IGUAL INCLUDE INT LLADER LLAIZQ MAYORDER MAYORIGUAL MAYORIZQ MAYORQUE MENORIGUAL MENORQUE MIENTRAS MINUSMINUS MODULO MULT NAMESPACE NOT NUMERAL OR PARA PARDER PARIZQ PLUSPLUS POTENCIA PUNTOCOMA RESTA RETURN SI SINO SUMA THEN USING VOID decladeclaracion : decla IDENTIFICADOR ASIGNAR expresion PUNTOCOMAdeclaracion : expresion\n    expresion : expresion SUMA PARIZQ expresion SUMA expresion PARDER \n              | expresion SUMA PARIZQ expresion RESTA expresion PARDER \n              | expresion RESTA PARIZQ expresion SUMA expresion PARDER \n              | expresion RESTA PARIZQ expresion RESTA expresion PARDER \n              | expresion MULT PARIZQ expresion SUMA expresion PARDER \n              | expresion MULT PARIZQ expresion RESTA expresion PARDER \n              | expresion SUMA PARIZQ expresion MULT expresion PARDER \n              | expresion RESTA PARIZQ expresion MULT expresion PARDER \n    \n    expresion  :   expresion SUMA expresion\n                |   expresion RESTA expresion\n                |   expresion MULT expresion\n                |   expresion DIV expresion\n                |   expresion POTENCIA expresion\n                |   expresion MODULO expresion\n               \n\n    expresion : RESTA expresion %prec UMINUS\n    expresion  : PARIZQ expresion PARDER\n                | LLAIZQ expresion LLADER\n                | CORIZQ expresion CORDER\n    \n    expresion   :  expresion MENORQUE expresion \n                |  expresion MAYORQUE expresion \n                |  expresion MENORIGUAL expresion \n                |   expresion MAYORIGUAL expresion \n                |   expresion IGUAL expresion \n                |   expresion DISTINTO expresion\n                |  PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER\n                |  PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER \n                |  PARIZQ  expresion PARDER MAYORIGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER IGUAL PARIZQ expresion PARDER\n                |  PARIZQ  expresion PARDER DISTINTO PARIZQ expresion PARDER\n    \n    expresion   :   expresion AND expresion \n                |   expresion OR expresion \n                |   expresion NOT expresion \n                |  PARIZQ expresion AND expresion PARDER\n                |  PARIZQ expresion OR expresion PARDER\n                |  PARIZQ expresion NOT expresion PARDER\n    \n    expresion : ENTERO\n              | FLOAT       \n    expresion : COMDOB expresion COMDOBexpresion : IDENTIFICADOR\n    expresion : MIENTRAS PARIZQ IDENTIFICADOR MENORQUE expresion PARDER\n              | MIENTRAS PARIZQ IDENTIFICADOR MAYORQUE  expresion PARDER\n              | SI PARIZQ IDENTIFICADOR MENORQUE expresion PARDER\n              | SI PARIZQ IDENTIFICADOR MAYORQUE expresion PARDER\n              | PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MAYORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER\n              \n\n    '
    
_lr_action_items = {'decla':([0,],[2,]),'RESTA':([0,3,4,5,6,7,8,9,10,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,68,69,70,71,78,79,80,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,144,148,],[6,-42,17,6,6,6,6,-39,-40,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,17,-17,17,17,17,6,-11,6,-12,6,-13,6,-14,17,17,17,17,17,17,17,17,17,17,17,-18,6,6,6,-19,-20,-41,17,88,90,94,17,17,17,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-36,-37,-38,17,17,17,17,17,-11,-12,-13,-12,-11,-13,-11,-12,17,17,17,17,17,17,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,6,17,-47,]),'PARIZQ':([0,5,6,7,8,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,72,73,74,75,76,77,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[5,5,5,5,5,5,36,37,38,41,43,45,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,95,96,97,98,99,100,5,5,5,5,5,41,43,45,43,41,45,41,43,5,5,5,5,5,5,5,]),'LLAIZQ':([0,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'CORIZQ':([0,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'ENTERO':([0,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'FLOAT':([0,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'COMDOB':([0,3,5,6,7,8,9,10,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,35,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,143,148,],[11,-42,11,11,11,11,-39,-40,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-17,64,11,-11,11,-12,11,-13,11,-14,-15,-16,-21,-22,-23,-24,-25,-26,-33,-34,-35,-18,11,11,11,-19,-20,-41,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-36,-37,-38,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,11,-47,]),'IDENTIFICADOR':([0,2,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,36,37,38,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,127,143,145,],[3,15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,65,66,67,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,142,3,146,]),'MIENTRAS':([0,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'SI':([0,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'PARA':([0,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'$end':([1,3,4,9,10,32,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,86,101,102,103,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,148,],[0,-42,-2,-39,-40,-17,-11,-12,-13,-14,-15,-16,-21,-22,-23,-24,-25,-26,-33,-34,-35,-18,-19,-20,-41,-1,-36,-37,-38,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,-47,]),'SUMA':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,16,-39,-40,16,-17,16,16,16,-11,-12,-13,-14,16,16,16,16,16,16,16,16,16,16,16,-18,-19,-20,-41,16,87,91,93,16,16,16,-36,-37,-38,16,16,16,16,16,-11,-12,-13,-12,-11,-13,-11,-12,16,16,16,16,16,16,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,16,-47,]),'MULT':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,18,-39,-40,18,-17,18,18,18,18,18,-13,-14,18,18,18,18,18,18,18,18,18,18,18,-18,-19,-20,-41,18,89,92,18,18,18,18,-36,-37,-38,18,18,18,18,18,18,18,-13,18,18,-13,18,18,18,18,18,18,18,18,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,18,-47,]),'DIV':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,19,-39,-40,19,-17,19,19,19,19,19,-13,-14,19,19,19,19,19,19,19,19,19,19,19,-18,-19,-20,-41,19,19,19,19,19,19,19,-36,-37,-38,19,19,19,19,19,19,19,-13,19,19,-13,19,19,19,19,19,19,19,19,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,19,-47,]),'POTENCIA':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,20,-39,-40,20,-17,20,20,20,-11,-12,-13,-14,20,20,20,20,20,20,20,20,20,20,20,-18,-19,-20,-41,20,20,20,20,20,20,20,-36,-37,-38,20,20,20,20,20,-11,-12,-13,-12,-11,-13,-11,-12,20,20,20,20,20,20,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,20,-47,]),'MODULO':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,21,-39,-40,21,-17,21,21,21,-11,-12,-13,-14,21,21,21,21,21,21,21,21,21,21,21,-18,-19,-20,-41,21,21,21,21,21,21,21,-36,-37,-38,21,21,21,21,21,-11,-12,-13,-12,-11,-13,-11,-12,21,21,21,21,21,21,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,21,-47,]),'MENORQUE':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,65,66,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,22,-39,-40,22,-17,22,22,22,-11,-12,-13,-14,22,22,22,22,22,22,22,22,22,22,22,72,-19,-20,-41,81,83,22,22,22,22,22,22,22,-36,-37,-38,22,22,22,22,22,-11,-12,-13,-12,-11,-13,-11,-12,22,22,22,22,22,22,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,22,-47,]),'MAYORQUE':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,65,66,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,144,148,],[-42,23,-39,-40,23,-17,23,23,23,-11,-12,-13,-14,23,23,23,23,23,23,23,23,23,23,23,73,-19,-20,-41,82,84,23,23,23,23,23,23,23,-36,-37,-38,23,23,23,23,23,-11,-12,-13,-12,-11,-13,-11,-12,23,23,23,23,23,23,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,143,23,-47,]),'MENORIGUAL':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,24,-39,-40,24,-17,24,24,24,-11,-12,-13,-14,24,24,24,24,24,24,24,24,24,24,24,74,-19,-20,-41,24,24,24,24,24,24,24,-36,-37,-38,24,24,24,24,24,-11,-12,-13,-12,-11,-13,-11,-12,24,24,24,24,24,24,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,24,-47,]),'MAYORIGUAL':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,25,-39,-40,25,-17,25,25,25,-11,-12,-13,-14,25,25,25,25,25,25,25,25,25,25,25,75,-19,-20,-41,25,25,25,25,25,25,25,-36,-37,-38,25,25,25,25,25,-11,-12,-13,-12,-11,-13,-11,-12,25,25,25,25,25,25,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,25,-47,]),'IGUAL':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,26,-39,-40,26,-17,26,26,26,-11,-12,-13,-14,26,26,26,26,26,26,26,26,26,26,26,76,-19,-20,-41,26,26,26,26,26,26,26,-36,-37,-38,26,26,26,26,26,-11,-12,-13,-12,-11,-13,-11,-12,26,26,26,26,26,26,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,26,-47,]),'DISTINTO':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,27,-39,-40,27,-17,27,27,27,-11,-12,-13,-14,27,27,27,27,27,27,27,27,27,27,27,77,-19,-20,-41,27,27,27,27,27,27,27,-36,-37,-38,27,27,27,27,27,-11,-12,-13,-12,-11,-13,-11,-12,27,27,27,27,27,27,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,27,-47,]),'AND':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,28,-39,-40,59,-17,28,28,28,-11,-12,-13,-14,28,28,28,28,28,28,28,28,28,28,28,-18,-19,-20,-41,28,59,59,59,28,28,28,-36,-37,-38,28,28,28,28,28,-11,-12,-13,-12,-11,-13,-11,-12,28,28,28,28,28,28,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,28,-47,]),'OR':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,29,-39,-40,60,-17,29,29,29,-11,-12,-13,-14,29,29,29,29,29,29,29,29,29,29,29,-18,-19,-20,-41,29,60,60,60,29,29,29,-36,-37,-38,29,29,29,29,29,-11,-12,-13,-12,-11,-13,-11,-12,29,29,29,29,29,29,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,29,-47,]),'NOT':([3,4,9,10,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,69,70,71,78,79,80,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,30,-39,-40,61,-17,30,30,30,-11,-12,-13,-14,30,30,30,30,30,30,30,30,30,30,30,-18,-19,-20,-41,30,61,61,61,30,30,30,-36,-37,-38,30,30,30,30,30,-11,-12,-13,-12,-11,-13,-11,-12,30,30,30,30,30,30,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,30,-47,]),'PARDER':([3,9,10,31,32,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,69,70,71,78,79,80,101,102,103,104,105,106,107,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,147,148,],[-42,-39,-40,58,-17,-11,-12,-13,-14,-15,-16,-21,-22,-23,-24,-25,-26,-33,-34,-35,-18,-19,-20,-41,58,58,58,101,102,103,-36,-37,-38,123,124,125,126,-11,-12,-13,-12,-11,-13,-11,-12,136,137,138,139,140,141,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,148,-47,]),'LLADER':([3,9,10,32,33,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,101,102,103,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,148,],[-42,-39,-40,-17,62,-11,-12,-13,-14,-15,-16,-21,-22,-23,-24,-25,-26,-33,-34,-35,-18,-19,-20,-41,-36,-37,-38,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,-47,]),'CORDER':([3,9,10,32,34,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,101,102,103,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,148,],[-42,-39,-40,-17,63,-11,-12,-13,-14,-15,-16,-21,-22,-23,-24,-25,-26,-33,-34,-35,-18,-19,-20,-41,-36,-37,-38,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,-47,]),'PUNTOCOMA':([3,9,10,32,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,58,62,63,64,68,101,102,103,108,123,124,125,126,128,129,130,131,132,133,134,135,136,137,138,139,140,141,144,148,],[-42,-39,-40,-17,-11,-12,-13,-14,-15,-16,-21,-22,-23,-24,-25,-26,-33,-34,-35,-18,-19,-20,-41,86,-36,-37,-38,127,-43,-44,-45,-46,-3,-4,-9,-6,-5,-10,-7,-8,-27,-28,-29,-30,-31,-32,145,-47,]),'ASIGNAR':([15,67,],[39,85,]),'PLUSPLUS':([146,],[147,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,39,41,43,45,59,60,61,81,82,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,100,143,],[4,31,32,33,34,35,40,42,44,46,47,48,49,50,51,52,53,54,55,56,57,68,69,70,71,78,79,80,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,144,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> decla IDENTIFICADOR ASIGNAR expresion PUNTOCOMA','declaracion',5,'p_declaracion_asignar','analizador_sintactico.py',18),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','analizador_sintactico.py',22),
  ('expresion -> expresion SUMA PARIZQ expresion SUMA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',28),
  ('expresion -> expresion SUMA PARIZQ expresion RESTA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',29),
  ('expresion -> expresion RESTA PARIZQ expresion SUMA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',30),
  ('expresion -> expresion RESTA PARIZQ expresion RESTA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',31),
  ('expresion -> expresion MULT PARIZQ expresion SUMA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',32),
  ('expresion -> expresion MULT PARIZQ expresion RESTA expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',33),
  ('expresion -> expresion SUMA PARIZQ expresion MULT expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',34),
  ('expresion -> expresion RESTA PARIZQ expresion MULT expresion PARDER','expresion',7,'p_expresion_formulascomplejas','analizador_sintactico.py',35),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',41),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',42),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',43),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',44),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',45),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_operaciones','analizador_sintactico.py',46),
  ('expresion -> RESTA expresion','expresion',2,'p_expresion_uminus','analizador_sintactico.py',53),
  ('expresion -> PARIZQ expresion PARDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',58),
  ('expresion -> LLAIZQ expresion LLADER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',59),
  ('expresion -> CORIZQ expresion CORDER','expresion',3,'p_expresion_grupo','analizador_sintactico.py',60),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',66),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',67),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',68),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',69),
  ('expresion -> expresion IGUAL expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',70),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_logicas','analizador_sintactico.py',71),
  ('expresion -> PARIZQ expresion PARDER MENORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',72),
  ('expresion -> PARIZQ expresion PARDER MAYORQUE PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',73),
  ('expresion -> PARIZQ expresion PARDER MENORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',74),
  ('expresion -> PARIZQ expresion PARDER MAYORIGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',75),
  ('expresion -> PARIZQ expresion PARDER IGUAL PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',76),
  ('expresion -> PARIZQ expresion PARDER DISTINTO PARIZQ expresion PARDER','expresion',7,'p_expresion_logicas','analizador_sintactico.py',77),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',86),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',87),
  ('expresion -> expresion NOT expresion','expresion',3,'p_expresion_booleana','analizador_sintactico.py',88),
  ('expresion -> PARIZQ expresion AND expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',89),
  ('expresion -> PARIZQ expresion OR expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',90),
  ('expresion -> PARIZQ expresion NOT expresion PARDER','expresion',5,'p_expresion_booleana','analizador_sintactico.py',91),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','analizador_sintactico.py',110),
  ('expresion -> FLOAT','expresion',1,'p_expresion_numero','analizador_sintactico.py',111),
  ('expresion -> COMDOB expresion COMDOB','expresion',3,'p_expresion_cadena','analizador_sintactico.py',116),
  ('expresion -> IDENTIFICADOR','expresion',1,'p_expresion_nombre','analizador_sintactico.py',122),
  ('expresion -> MIENTRAS PARIZQ IDENTIFICADOR MENORQUE expresion PARDER','expresion',6,'p_expresion_bucles','analizador_sintactico.py',131),
  ('expresion -> MIENTRAS PARIZQ IDENTIFICADOR MAYORQUE expresion PARDER','expresion',6,'p_expresion_bucles','analizador_sintactico.py',132),
  ('expresion -> SI PARIZQ IDENTIFICADOR MENORQUE expresion PARDER','expresion',6,'p_expresion_bucles','analizador_sintactico.py',133),
  ('expresion -> SI PARIZQ IDENTIFICADOR MAYORQUE expresion PARDER','expresion',6,'p_expresion_bucles','analizador_sintactico.py',134),
  ('expresion -> PARA PARIZQ IDENTIFICADOR ASIGNAR expresion PUNTOCOMA IDENTIFICADOR MAYORQUE expresion PUNTOCOMA IDENTIFICADOR PLUSPLUS PARDER','expresion',13,'p_expresion_bucles','analizador_sintactico.py',135),
]
