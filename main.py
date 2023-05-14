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
        pass


env = Table()

# print(env.cardCountStop)
print(env.getrandomcard())
