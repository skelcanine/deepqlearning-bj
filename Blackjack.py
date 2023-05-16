import numpy as np
import random
import math

DECK_COUNT = 8
ONE_DECK_SIZE = 52
DECK_DICTIONARY = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}


class Blackjack:
    def __init__(self):
        # Randomness of cut card
        __stopPercentage = random.randint(45, 55)
        # Dealers hand
        self.dealerhand = list()
        # Player hand
        self.playerhand = list()
        # Calculate deck size
        self.totalCardCount = DECK_COUNT * ONE_DECK_SIZE
        # Cut card in deck
        self.cardCounttoStop = math.floor((self.totalCardCount / 100) * __stopPercentage)
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
            self.removecardfromdeck(card)
        else:
            card = self.getrandomcard()
        return card

    def removecardfromdeck(self, card):
        self.deckofgamecards[card] = self.deckofgamecards[card] - 1

    def calculatesoft(self, hand):
        soft = 0
        nonsoft = 0
        for handcard in hand:
            nonsoft += handcard
            if handcard == 1:
                soft = soft + handcard + 10
            else:
                soft = soft + handcard
        return [nonsoft, soft]

    def calculatepoint(self, hand):
        if 1 in hand:
            result = self.calculatesoft(hand)
            return result
        else:
            preresult = sum(hand)
            return [preresult, preresult]
