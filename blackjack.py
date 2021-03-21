from generic import HIDE, HAND, HAND_VALUE, CARDS_IN_HAND, VALUE, suits, SUIT, card_values, DEALER, PLAYER, BLACKJACK, isValidDifficulty, formatDifficultyChoice

import display
import re
from random import uniform
from math import floor
from display import playerHandAscii
from time import sleep

####SETUP FUNCTIONS#####
def getDeck(numberOfDecks):
  deck = []
  for number in range (numberOfDecks+1):
    for key in card_values:
      for suit in suits:
        newCard ={}
        newCard[SUIT] = suit
        newCard[VALUE] = key
        newCard[HIDE] = False
        deck.append(newCard)
  return deck

def dealHand (deck, size):
  hand = []
  for number in range(0,size):
    (card,deck) = drawCard(deck)
    hand.append(card)
  player = updateHand(hand)  
  return (player, deck)

def chooseDifficulty():
  choice = ' '
  while not (isValidDifficulty(choice[0])):
    choice = display.getDifficultyInput() or ' ' 
  return formatDifficultyChoice(choice) 

def dealHands (deck):
  hands = []
  for player in range(DEALER,PLAYER+1):
    (playerDealt,deck) = dealHand (deck,2)
    if player == DEALER:
      playerDealt[HAND][0][HIDE] = True
      playerDealt = updateHand(playerDealt[HAND])  
    hands.append(playerDealt)
  return (hands, deck)

#####GAME LOGIC ####
def playRound(hands, deck, score):  
  bet = placeABet(score)
  Turn = PLAYER
  while True:
    display.playScreen(hands, bet, score)    
    if Turn == PLAYER:
      (hands, deck, Turn) = playersTurn(hands, deck)
    elif Turn == DEALER :
      (hands,deck, Turn) = dealersTurn(hands, deck)
    else:
      break
  return (determineResult(hands), bet)

def playersTurn (hands,deck):
  if hands[PLAYER][HAND_VALUE] >= BLACKJACK or (Stay(input('hit or stay: h/s ') )):
    hands[DEALER][HAND][0][HIDE] = False
    hands[DEALER] = updateHand(hands[DEALER][HAND]) 
    return (hands, deck, DEALER)
  else:
    (card,deck) = drawCard(deck)
    hands = addCard(thisCard = card, toPlayer = PLAYER, forHands = hands)
    return (hands, deck, PLAYER)

def dealersTurn(hands,deck):
  if hands[PLAYER][HAND_VALUE] <= BLACKJACK and hands[DEALER][HAND_VALUE] < hands[PLAYER][HAND_VALUE] and hands[DEALER][HAND_VALUE] < 17:
    (card,deck) = drawCard(deck)
    hands = addCard(thisCard = card, toPlayer = DEALER, forHands = hands) 
    sleep(2)
    return (hands,deck, DEALER)
  else:
    return (hands,deck, -1)   

def determineResult(hands):
  if (hands[PLAYER][HAND_VALUE] == BLACKJACK != hands[DEALER][HAND_VALUE] and len(hands[PLAYER][HAND]) == 2):
    return 1.5
  if (hands[PLAYER][HAND_VALUE] > hands[DEALER][HAND_VALUE] or hands[DEALER][HAND_VALUE] > BLACKJACK) and hands[PLAYER][HAND_VALUE] <= BLACKJACK :
    return 1
  elif hands[PLAYER][HAND_VALUE] > BLACKJACK or (hands[PLAYER][HAND_VALUE] < hands[DEALER][HAND_VALUE] and hands[DEALER][HAND_VALUE] <= BLACKJACK) :
    return -1
  else:
    return 0
  
def playerHandValue (cards):
  handValue = 0
  aceCount = 0
  for card in cards:
    hidden = card[HIDE]
    handValue += card_values[card[VALUE]] if not hidden else handValue +0
    aceCount = aceCount+1 if card[VALUE] =='Ace' else aceCount+0
  for aces in range(1,aceCount+1) :
    if handValue > 21:
      handValue -= 10
  return handValue

####GAME ACTIONS####
Stay = lambda option: option == 'stay' or option == 'sty' or option == 'sta' or option == 'say' or option == 'tay' or option == 'st' or option == 'ay' or option == 'sy' or option == 's'

def drawCard(deck):
  dealt = floor(uniform(0,len(deck)))
  card = deck[dealt]
  del deck[dealt] 
  return (card, deck)

def updateHand (hand):
  player = {}
  player[HAND] = hand
  player[HAND_VALUE] = playerHandValue(player[HAND])
  player[CARDS_IN_HAND] = playerHandAscii(player[HAND])
  return player

def addCard (thisCard, toPlayer, forHands):
  forHands[toPlayer][HAND].append(thisCard)
  forHands[toPlayer] = updateHand(forHands[toPlayer][HAND]) 
  return forHands

def placeABet(score):
  bet = ''
  while True:
    display.clear()
    bet = display.makeBetScreen(score)
    if (re.search("^[0-9]*$", bet) and bet != '') :
      bet = int(bet)
      if (bet > 0 and bet <=score):
        return bet


