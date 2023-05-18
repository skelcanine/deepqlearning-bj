import numpy as np
import random
import math
import Blackjack


class Table:
    def __init__(self):
        self.game = Blackjack.Blackjack()
        self.playerhand = self.game.playerhand
        self.dealerhand = self.game.dealerhand
        self.isnewround = True

    def checkdeckcardcount(self):
        if self.game.currentCardCount < self.game.cardCounttoStop:
            self.resettable()

    def resettable(self):
        self.game = Blackjack.Blackjack()
        self.isnewround = True

    def newround(self):
        self.checkdeckcardcount()
        self.isnewround = True
        self.game.preparenewround()

    def startnewround(self):
        self.game.drawcardtohand(self.playerhand)
        self.game.drawcardtohand(self.dealerhand)
        self.game.drawcardtohand(self.playerhand)
        self.game.drawcardtohand(self.dealerhand)
        self.isnewround = False

    def tablegenerate(self, playermove):
        doneflag = 0
        if self.isnewround:
            print("new round")
            self.isnewround = False
            self.startnewround()

            return self.state() + [doneflag]

        if (
                self.game.playerphasefihished and self.game.dealerphasefihished) or self.game.dealerbusted or self.game.playerbusted:
            print("finish or bust")
            self.newround()
            self.startnewround()

        elif self.game.playerphasefihished:
            if not self.game.dealerphasefihished:
                print("finishing dealer")
                self.game.finishdealerhand()
        else:
            print("playermove")
            if playermove == 0:
                self.game.playernextmove(playermove)
                doneflag = 1
                return self.state() + [doneflag]

            if playermove == 1:
                self.game.playernextmove(playermove)
                if (
                        self.game.playerphasefihished and self.game.dealerphasefihished) or self.game.dealerbusted or self.game.playerbusted:
                    doneflag = 1
                    return self.state() + [doneflag]
            if playermove == 2:
                self.game.playernextmove(playermove)
                if (
                        self.game.playerphasefihished and self.game.dealerphasefihished) or self.game.dealerbusted or self.game.playerbusted:
                    doneflag = 1
                    return self.state() + [doneflag]

        return self.state() + [doneflag]

    def state(self):
        statelist = list()
        for i in range(1, 11):
            statelist.append(self.game.deckofgamecards[i])

        statelist += self.game.calculatepoint(self.playerhand)
        if self.game.playerphasefihished:
            statelist += self.game.calculatepoint(self.dealerhand)
        else:
            dealercardlist = self.game.calculatepoint(self.dealerhand)
            statelist.append(dealercardlist[0])
            statelist.append(0)

        return statelist


env = Table()
"""
print(env.tablegenerate(2))
print(env.tablegenerate(2))
print(env.tablegenerate(1))
print(env.tablegenerate(1))
print(env.tablegenerate(1))
print(env.tablegenerate(1))
"""


class Agent:
    def __init__(self):
        pass

    def train(self, batchx):
        pass

    def predict(self, action):
        result = 1
        return result


def calculatereward():
    pass


DQagent = Agent()
action = 1
reward = 0

for i in range(8):
    oldstate = env.tablegenerate(action)
    done = oldstate.pop()

    if not done:
        action = DQagent.predict(action)
    else:
        continue






    mybatch = list()
    oldstate = env.tablegenerate(action)
    futurestate = DQagent.predict(action)
    mybatch.append(oldstate)
    mybatch.append(action)
    mybatch.append(reward)
    mybatch.append(futurestate)
    print(mybatch)
