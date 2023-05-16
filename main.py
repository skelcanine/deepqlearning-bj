import numpy as np
import random
import math
import Blackjack


class Table:
    def __init__(self):
        self.game = Blackjack.Blackjack()

    def checkdeckcardcount(self):
        if self.game.currentCardCount < self.game.cardCounttoStop:
            self.resettable()

    def resettable(self):
        self.game = Blackjack.Blackjack()

    def newround(self):
        self.game.playerhand.append(self.game.getrandomcard())
        self.game.dealerhand.append(self.game.getrandomcard())
        self.game.playerhand.append(self.game.getrandomcard())
        self.game.dealerhand.append(self.game.getrandomcard())



env = Table()

# print(env.cardCountStop)
env.newround()

print(env.game.dealerhand)
print(env.game.calculatepoint(env.game.dealerhand))
print(env.game.playerhand)
print(env.game.calculatepoint(env.game.playerhand))
