from generic import DIFFICULTY, getChoice
import blackjack
import display

while True:

  currentDifficulty =  blackjack.chooseDifficulty()
  deck = blackjack.getDeck(DIFFICULTY[currentDifficulty])
  (hands, deck) = blackjack.dealHands(deck)
  score = 25 + (5*(4-DIFFICULTY[currentDifficulty]))

  while True:
    (result, bet)  = blackjack.playRound(hands, deck, score)
    score += (result*bet)
    display.scoreScreen(hands, score, bet, result)
    
    if (score >0):
      if getChoice("\nPlay A New Round? y/n\n") == 'y': 
        if len(deck) < 4:
          deck = blackjack.getDeck(DIFFICULTY[currentDifficulty])
        hands = blackjack.dealHands(deck)
      else:
        break
    else:
      print ("\nYou ran out of points\n")
      break 
  
  if getChoice("\nStart A New Game? y/n \n") == 'n':
    break

