'''
Jogo do Pedra Papel Tesoura
2024.08.13
De: Sofia Roloff
'''

#-->Bibliotecas
from modules import clrScreen, displayHeader, getUserOption, validateUserOption, displayLine, displayMsg, displayMsgCenter, displayHeaderT
from random import randint
from time import sleep 

# importa as variaveis da pasta moduels para essa pasta

#-->Constantes, Variaveis e Listas
msgInicio = ['Seja bem vind@ ao', 'Jogo do Pedra-Papel-Tesoura', 'desenvolvido por: Sofia Roloff', 'Boa Sorte... Você vai precisar...'] # É uma lista para mostrar as mensagens do cabeçalho
msgs = []
playAgain = '' 
playerScore = 0
computerScore = 0

#-->Funções
def startPPT(): # Função que vai dar inicio ao jogo
  while(True): # enquanto for true, ou seja, enquanto a variavel for rodada, o start vai rodar
    clrScreen() # essa função limpa a tela deixando ela sem nenhum caractere
    displayHeader(msgInicio) # Essa função dá inicio ao cabeçalho, indicando o inicio do jogo
    #função para iniciar o game
    playPPT()
    playAgain = getUserOption('Deseja jogar novamente? [s/n]') # essa função faz com que o programa teste para saber se o user quer jogar novamente, isso será para quando o jogo for já iniciado uma vez
    while not validateUserOption(playAgain, ['s', 'n', 'S', 'N']): # para que o programa saiba a resposta do user em relação ao jogar novamente, tem uma lista de caracteres que o user pode utilizar para descrever a resposta do user. Como s para sim, e n para não.
      playAgain = getUserOption('Deseja jogar novamente? [s/n]') # vai mostrar essa mensagem na tela
    if playAgain.lower() != 's': # se o user escolher s de sim, o programa ira apenas repetir varias vezes
      break # para parar o programa
      
def displayMenu():
  
    msgs = ['Escolha:',
           '[0] --> pedra',
           '[1] --> papel',
           '[2] --> tesoura']
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
  choices = ['PEDRA', 'PAPEL', 'TESOURA']
  playerChoiceStr = choices[int(playerChoice)]
  computerChoiceStr =  choices[int(computerChoice)]
  if playerChoice == computerChoice:
    result = 'Empate!'
  elif (playerChoice == '0' and computerChoice == '2') or \
      (playerChoice == '1' and computerChoice == '0') or \
      (playerChoice == '2' and computerChoice == '1'):
    play = f"{playerChoiceStr} vence {computerChoiceStr}"
    result = 'Você Ganhou!'
  else:
    play = f"{computerChoiceStr} vence {playerChoiceStr}"
    result = 'Você Perdeu!'
  msgs = ['Jogada do Player: ' + playerChoiceStr,
         'Jogada do PC: ' + computerChoiceStr,
         play, result]
  displayHeaderT(msgs)
  return result
  
def playPPT():  
  playerScore = 0
  computerScore = 0
  while playerScore < 2 and computerScore < 2:
    displayMenu()
    playerChoice = getUserOption('Sua escolha')
    while not validateUserOption(playerChoice, ['0','1', '2']):
      displayMunu()
      playerChoice = getUserOption('Sua escolha')
    computerChoice = str(randint(0,2))
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