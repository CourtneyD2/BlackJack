from os import system, name
from generic import HIDE, VALUE, SUIT, HAND_VALUE, CARDS_IN_HAND, suits, NORMAL, TOUGH, HECTIC, CHAOS

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
####UTILITY FUNCTIONS
clear = lambda : system('cls' if name=='nt' else 'clear')

###SETUP 
def getDifficultyInput () :
  clear()
  print(logo) 
  return input (f'What difficulty would you like to play on \n {NORMAL}\n {TOUGH}\n {HECTIC}\n {CHAOS}\n-------\n').upper() 

###Screens
def playScreen (hands, bet, score):
  clear()
  print(logo)    
  Hands(hands)
  print(f"YOUR SCORE : {score}\n")
  print(f"You Bet : {bet}\n")

def makeBetScreen(score):
  clear()
  print(logo)
  return input (f"How much do you want to bet, minimum 1 and maximum {score} \n")

def scoreScreen (hands, score, bet, result):
  clear()
  message = f"You WON, gaining {bet*result} points" if result > 0 else f"You LOST, You lost {bet} points" if result < 0 else "Its a Tie"
  print (logo)
  Hands(hands)
  print(f"\n{message}, your new Score is {score}")

####HAND FUNCTIONS#####
def Hands(hands):
  for hand in hands:
    print (f"{hand[CARDS_IN_HAND]} {hand[HAND_VALUE]}")

def playerHandAscii (cards):
  lines = [[] for i in range(7)]
  for card in cards:
    hidden = card[HIDE]
    rank, space = (card[VALUE], '') if card[VALUE] == '10' else (card[VALUE][0], ' ')
    lines = faceDownCard(lines) if hidden else faceUpCard (lines,rank, space, card[SUIT])   

  result =[]
  for index, line in enumerate(lines):
    result.append(''.join(lines[index]))
  return('\n'.join(result))

def faceUpCard (lines, rank, space, suit):
  lines[0].append('┌─────────┐')
  lines[1].append('│{}{}       │'.format(rank, space)) 
  lines[2].append('│         │')
  lines[3].append('│    {}    │'.format(suits[suit]))
  lines[4].append('│         │')
  lines[5].append('│       {}{}│'.format(space, rank))
  lines[6].append('└─────────┘')
  return lines

def faceDownCard (lines):  
  lines[0].append('┌─────────┐')
  lines[1].append('│░░░░░░░░░│') 
  lines[2].append('│░░░░░░░░░│')
  lines[3].append('│░░░░░░░░░│')
  lines[4].append('│░░░░░░░░░│')
  lines[5].append('│░░░░░░░░░│')
  lines[6].append('└─────────┘')
  return lines