import numpy as np
import random
import math

DECK_COUNT = 8
ONE_DECK_SIZE = 52
DECK_DICTIONARY = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}


class Table:
    def __init__(self):
        self.game = Blackjack()

    def checkdeckcardcount(self):
        pass

    def resettable(self):
        self.game = Blackjack()

    def newround(self):
        pass


class Blackjack:
    def __init__(self):
        # Randomness of cut card
        __stopPercentage = random.randint(45, 55)
        # Calculate deck size
        self.totalCardCount = DECK_COUNT * ONE_DECK_SIZE
        # Cut card in deck
        self.cardCountStop = math.floor((self.totalCardCount / 100) * __stopPercentage)
        # Set current card count
        self.currentCardCount = self.totalCardCount
        # Create deck dictionary
        self.deckofgamecards = DECK_DICTIONARY.copy()
        # Multiply by deck count to match
        for key in self.deckofgamecards:
            self.deckofgamecards[key] *= DECK_COUNT
        '''
        for x, y in self.deckofgamecards.items():
            print(x, y)
        print(self.currentCardCount)
        '''

    def getrandomcard(self):
        card, cardcount = random.choice(list(self.deckofgamecards.items()))
        if cardcount != 0:
            cardcount -= 1
            self.deckofgamecards[card] = cardcount
        else:
            card = self.getrandomcard()
        return card


env = Blackjack()

# print(env.cardCountStop)
print(env.getrandomcard())
