VALUE = 'VALUE'
SUIT = 'SUIT'
HIDE = 'HIDE'

HAND = 'HAND'
HAND_VALUE ='HAND_VALUE'
CARDS_IN_HAND = 'CARDS_IN_HAND'

DEALER = 0
PLAYER = 1

NORMAL = 'Normal'
TOUGH = 'Tough'
HECTIC = 'Hectic'
CHAOS = 'Chaos'

FIRST = 0

DIFFICULTY = {
  NORMAL : 2,
  TOUGH : 4,
  HECTIC : 6,
  CHAOS : 8,
}

BLACKJACK = 21
MAXPLAYERS = 4

suits = {
  'Spades': '♠', 
  'Diamonds': '♦', 
  'Hearts':  '♥', 
  'Clubs':  '♣',
}

card_values = {
  'Ace': 11,  # value of the ace is high until it needs to be low
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  '10': 10,
  'Jack': 10,
  'Queen': 10,
  'King': 10,
}

formatSelection = lambda selection : 'n' if selection == 'n' or selection == 'no' else 'y' if selection == 'y' or selection == 'yes' or selection == 'ys' or selection == 'ye' else ''

isValidDifficulty  = lambda choice: choice == NORMAL[0] or choice == TOUGH[0] or choice == HECTIC[0] or choice == CHAOS[0]

formatDifficultyChoice = lambda choice: CHAOS if choice[0] == CHAOS[0] else  TOUGH if choice[0] == TOUGH[0] else HECTIC if choice[0] == HECTIC[0] else NORMAL

def getChoice(message):
  choice = ''
  while not choice:
    choice  = input(message)
  return choice