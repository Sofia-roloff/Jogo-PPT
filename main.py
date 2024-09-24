'''
Projeto Jogo Pedra-Papel-Tesoura
De: Sofia Roloff
2024.08.13
'''

#--> Bibliotecas #--> Importa as funções do modules.py e do ppt.py
from ppt import startPPT 
from modules import clrScreen, displayLine, displayMsgCenter, displayHeaderT, getUserOption, validateUserOption 
from parimpar import startParImpar#importa a variavel de start da pasta ppt

#-->Constantes, Variaveis e listas

#-->Funções 

#-->Main
msgs =  ['Seja Bem-vind@ aos Jogos', 'PEDRA PAPEL TESOURA', 'PAR OU ÍMPAR']
displayHeaderT(msgs)
msgs = ['Digite 0 --> sair',
       'Digite 1 --> Pedra-Papel-Tesoura',
       'Digite 2 --> Par ou Ímpar']
displayHeaderT(msgs)
opUser = getUserOption('Sua escolha')
while not validateUserOption(opUser, ['0','1','2']):
  opUser = getUserOption('Sua escolha')
if (opUser == '2'):
  startParImpar()
else:
  displayMsg('Até a próxima...')

  
