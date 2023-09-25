###############################################################
# deck.py
###############################################################

###
# *Name:    Alicyn Knapp
# *Credit:  PennWest Projects! (discord server)
# *Purpose: Define card deck attributes and actions
###

# from queue import *
from random import *

###############################################################

class Deck:
    # -- Constructor --
    def __init__(self):
        # self.deck = SimpleQueue()
        self.deck = []
        self.shuffler = Random()

    # -- Methods --
    def shuffle(self):
        ''' Shuffles the cards in the deck '''
        print("\t\tShuffling the deck... ")
        self.shuffler.shuffle(self.deck)


    # draw_card(self) : T (card_type)
    def draw_card(self):
        ''' Removes a card and places the drawn card at the back of the deck. Returns the card drawn. '''
        print("\t\tDrawing a card... ")

        # index = 0 is starting point for FIFO
        self.card_drawn = self.deck.pop(0)

        self.deck.append(self.card_drawn)

        return self.card_drawn


    # purely for monopoly game testing purposes
    def print_deck(self):
        for cards in self.deck:
            print(cards.index, "\t", cards.event_name)
