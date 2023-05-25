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
        # Dealer busted
        self.dealerbusted = False
        # Dealer phase
        self.dealerphasefihished = False
        # Player hand
        self.playerhand = list()
        # Player busted
        self.playerbusted = False
        # Player phase
        self.playerphasefihished = False
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
        soften = True
        soft = 0
        nonsoft = 0
        for handcard in hand:
            nonsoft += handcard
            if handcard == 1 and soften:
                soft = soft + handcard + 10
                soften = False
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

    def drawcardtohand(self, hand):
        drawcard = self.getrandomcard()
        hand.append(drawcard)
        return drawcard

    def isbusted(self, hand):
        calculatedpoints = self.calculatepoint(hand)
        if calculatedpoints[0] > 21 and calculatedpoints[1] > 21:
            return True
        return False

    #########################################################
    def calculateresult(self, dealerhand, playerhand):
        if self.playerphasefihished and self.dealerphasefihished:
            dealerhandpoint = self.calculatepoint(dealerhand)
            self.dealerbusted = self.isbusted()
            playerhandpoint = self.calculatepoint(playerhand)

    #########################################################

    def preparenewround(self):
        self.dealerhand.clear()
        self.playerhand.clear()
        self.dealerbusted = False
        self.playerbusted = False
        self.dealerphasefihished = False
        self.playerphasefihished = False

    # 0 STOP 1 DRAW CARD 2 DOUBLE
    def playernextmove(self, playermove):
        # print("playernext")
        if playermove == 0:
            self.playerphasefihished = True
            self.finishdealerhand()
        elif playermove == 1:
            # print(self.playerhand)
            drawcard = self.drawcardtohand(self.playerhand)
            # print(self.playerhand)
            isbusted = self.isbusted(self.playerhand)
            if isbusted:
                self.playerbusted = isbusted
                self.playerphasefihished = True
            return drawcard
        elif playermove == 2:
            drawcard = self.drawcardtohand(self.playerhand)
            isbusted = self.isbusted(self.playerhand)
            self.playerbusted = isbusted
            self.playerphasefihished = True
            self.finishdealerhand()
            return drawcard

    def finishdealerhand(self):
        hand = self.calculatepoint(self.dealerhand)
        print(hand)
        if hand[0] >= 17 and hand[1] >= 17:
            self.dealerphasefihished = True
        isbusted = self.isbusted(self.dealerhand)
        if isbusted:
            self.dealerbusted = isbusted
        if self.dealerphasefihished:
            return
        if hand[0] < 17 and hand[1] < 17:
            self.drawcardtohand(self.dealerhand)
            self.finishdealerhand()