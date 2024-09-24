'''
Jogo do Pedra Papel Tesoura
2024.08.13
De: Sofia Roloff
'''

#-->Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT
from random import randint
from time import sleep 

# Listas
msgInicio = ['Seja bem vind@ ao', 'Par ou Ímpar', 'desenvolvido por: Sofia Roloff', 'Boa Sorte... Você vai precisar...'] 
msgs = []
playAgain = '' 
playerScore = 0
computerScore = 0

#-->Funções
def startParImpar(): 
  while(True):
    clrScreen() 
    displayHeader(msgInicio) 
    playParImpar()
    playAgain = getUserOption('Deseja jogar novamente? [s/n]') 
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']): 
      playAgain = getUserOption('Deseja jogar novamente? [s/n]') 
    if playAgain.lower() != 's': 
      break

def displayMenu():

    msgs = ['Escolha:',
           '[1] --> Ímpar',
           '[2] --> Par']
    displayLine()
    for msg in msgs:
      displayMsg(msg)
    displayLine() 



def displayScore(typeScore, playerScore, computerScore):
  mgsg = []
  msgs.append(typeScore)
  displayHeader(typeScore)
  msgs.append(f'Player: {playerScore} --- PC: {computerScore}')
  displayHeaderT(msgs)

def determineWinner(playerChoice, computerChoice):
  play = ''
  result = ''
  choices = ['PAR', 'ÍMPAR']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr =  choices[int(computerChoice)]
  valor = numPlayer + numComputer
  if valor % 2 == playerChoice:
    result = 'Você Ganhou!'
  else:
    play = f"{computerChoiceStr} vence {playerChoiceStr}"
    result = 'Você Perdeu!'
  msgs = ['Jogada do Player: ' + playerChoiceStr,
         'Jogada do PC: ' + computerChoiceStr,
         play, result]
  displayHeaderT(msgs)
  return result

def playParImpar():  
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0', '1']):
      displayMunu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,9))
    result = determineWinner(playerChoice, computerChoice)
    if 'Ganhou' in result:
      playerScore += 1
    elif 'Perdeu' in result:
      computerScore += 1
    if playerScore < 2 and computerScore < 2:
      displayScore('PLACAR', playerScore, computerScore)
    sleep(1)
  displayScore('PLACAR FINAL', playerScore, computerScore)
  if playerScore > computerScore:
    displayMsg(['VOCÊ GANHOU!! BÃO DE MAIZE!'])
  else:
    displayHeader(['Parabéns, você perdeu!', 'Ruim de maize!'])





#-->Main