'''
Arquivo de Modulos
2024.08.13
De: Sofia Roloff
'''

#-->Bibliotecas
from random import choice # importa a variavel choice
from time import sleep

#-->Constantes, Variaveis e Listas
TAM = 50 #É o tamanho do espaço da tela
CAR = choice(['=', '*','&','!','@','|']) #Caractere usado para fazer um desenho ou o cabeçalho  
MAR = 4 #Tamanho da margem

#-->Funções
def clrScreen(): #Função limpa tela
  print('\n'*TAM) #Mostra o Teste 123 e depois mostra o espaço conforme o TAM #\n == linha * TAM

def displayLine(): #função para mostrar uma linha de caracteres,
  print(CAR*TAM) # mostra corretamente os caracteres e o tamanho da tela apos a linha vazia 

def displayMsg(msg): # transporta uma msg da lista de mensagens
  print(f'{CAR} {msg:<{TAM-MAR}} {CAR}') # e ent mostra corretamente o tamanho da tela a margem e os caracteres 

def displayMsgCenter(msg): # transporta outra msg, dessa vez de centro
  print(f'{CAR} {msg:^{TAM-MAR}} {CAR}') #mostra a estrutura do cabeçalho

def displayHeader(msgs): # mostra a msg de cabeçalho
  displayLine() # mostra a linha vazia 
  for item in msgs:  
    displayMsgCenter(item)
  displayLine()
  
def displayHeaderT(msgs): 
  displayLine()  
  for item in msgs:  
    displayMsgCenter(item)
    sleep(1)
  displayLine() 
  
def getUserOption(msg):
  option = input(f'{CAR} {msg}: ').strip() #O strip vai ignorar o espaço caso o user escreva bem mais ou menos
  return option # NÃO ESQUÇA DO RETURN!!!! Se não, o programa não vai repetir o que o user escreveu
def validateUserOption(option, listOptions):
  if option in listOptions:
    return True
  else:
    msgErro = ['Opção Inválida!', 'Escolha novamente...']
    displayHeader(msgErro)
    return False
  
#--> Main
