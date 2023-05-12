import numpy as np
import random
import math
import Blackjack

DECK_COUNT = 8
ONE_DECK_SIZE = 52
DECK_DICTIONARY = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 16}


class Table:
    def __init__(self):
        self.game = Blackjack.Blackjack()

    def checkdeckcardcount(self):
        pass

    def resettable(self):
        self.game = Blackjack.Blackjack()

    def newround(self):
        pass





env = Blackjack()

# print(env.cardCountStop)
print(env.getrandomcard())
