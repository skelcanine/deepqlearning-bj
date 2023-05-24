import numpy as np
import random
import math
import Blackjack
import pygame
import os

TABLE_WIDTH = 1024
TABLE_HEIGHT = 768
FPS = 60
DEFAULT_CARD_SIZE = (120, 180)
BACK_TO_OPEN_LENGTH = (TABLE_WIDTH * 1 / 10)
MY_CARD_POSITION = (int(TABLE_WIDTH*4/10), int(TABLE_HEIGHT*7/10))

class Table:
    class Card:
        def __init__(self, x=0, y=0, card=1):
            self.card = card
            self.x = x
            self.y = y

    def __init__(self):
        self.game = Blackjack.Blackjack()
        self.playerhand = self.game.playerhand
        self.dealerhand = self.game.dealerhand
        self.isnewround = True
        self.tabledealercardlist = list()
        self.tablemycardlist = list()

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
mybatch = list()

oldstate = env.tablegenerate(action)
done = oldstate.pop()

for i in range(5):

    if not done:
        action = DQagent.predict(oldstate)
        futurestate = env.tablegenerate(action)
        futuredone = futurestate.pop()
        batch = list()
        batch.append(oldstate)
        batch.append(action)
        batch.append(reward)
        batch.append(futurestate)
        mybatch.append(batch)
        if not futuredone:

            action = DQagent.predict(futurestate)
            oldstate = futurestate
        else:
            oldstate = env.tablegenerate(action)
    else:
        continue

for item in mybatch:
    print(item)

pygame.init()
pygame.display.set_caption('Blackjack')
screen = pygame.display.set_mode((TABLE_WIDTH, TABLE_HEIGHT))
clock = pygame.time.Clock()
clock.tick(FPS)
running = True

bgimagepath = 'resources/images/table/table1024x768.jpeg'

bacground = pygame.image.load(bgimagepath)
screen.blit(bacground, (0, 0))

"""""""""""""""""""""""
import kards

print(cards)
"""""
cards_path = 'resources/images/cards'
cards = list()
for path in os.listdir(cards_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(cards_path, path)):
        cards.append(os.path.join(cards_path, path))
print(cards)
cardback = pygame.image.load(cards.pop())
cardback = pygame.transform.scale(cardback, DEFAULT_CARD_SIZE)

movingcardback = cardback.copy()
movingcardback = pygame.transform.scale(cardback, DEFAULT_CARD_SIZE)

xmove = 0

card1 = pygame.image.load(cards[0])
card1 = pygame.transform.scale(card1, DEFAULT_CARD_SIZE)

# TEST

cardddd = env.Card(MY_CARD_POSITION[0], MY_CARD_POSITION[1], 10)

env.tablemycardlist.append(cardddd)


while running:

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # RENDER YOUR GAME HERE

    current_time = pygame.time.get_ticks()
    if current_time % 20 == 0:
        screen.blit(bacground, (0, 0))
        screen.blit(cardback, (TABLE_WIDTH - (TABLE_WIDTH * 2 / 10), TABLE_HEIGHT - (TABLE_HEIGHT * 9 / 10)))
        for mycard in env.tablemycardlist:
            tempcard = pygame.image.load(cards[mycard.card-1])
            tempcard = pygame.transform.scale(tempcard, DEFAULT_CARD_SIZE)
            screen.blit(tempcard, (mycard.x, mycard.y))

        if xmove > -550:
            if xmove * -1 <= BACK_TO_OPEN_LENGTH:
                screen.blit(movingcardback,
                            (TABLE_WIDTH - (TABLE_WIDTH * 2 / 10) + xmove, TABLE_HEIGHT - (TABLE_HEIGHT * 9 / 10)))
                xmove -= 4
            else:
                screen.blit(card1,
                            (TABLE_WIDTH - (TABLE_WIDTH * 2 / 10) + xmove, TABLE_HEIGHT - (TABLE_HEIGHT * 9 / 10)))
                xmove -= 4

    # flip() the display to put your work on screen
    pygame.display.update()

pygame.quit()
