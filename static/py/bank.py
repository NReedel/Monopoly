# bank.py

#
# *Name:    Alicyn Knapp
# *Credit:  PennWest Projects! (discord server)
# *Purpose: Define Monopoly bank traits and actions
#

import json
from deeds import *


class Bank:
    ### -- Constructor ###
    def __init__(self):
        ### -- Data -- ###
        # bills = {'ones': 40, 'fives': 40, 'tens': 40, 'twenties': 50, 'fifties': 30, 'hundreds': 20, 'five_hundreds': 20}
        self.deeds = list()

        with open('properties.json', 'r') as rf:
            for i in json:
                pass

        houses = 32
        hotels = 12

    ### -- Methods -- ###
    def pay_money(self, current_balance = int(0), amount_paid = int(0)):
        """ Subtracts amount paid to bank from current balance and returns the new balance """
        # print('Paid $', amount_paid, ' to The Bank.')
        return current_balance - amount_paid

    def receive_money(self, current_balance = int(0), amount_received = int(0)):
        """ Adds amount received from bank to current balance and returns the new balance """
        # print('Received $', amount_received, ' from The Bank.')
        return amount_received + current_balance

    '''
    def salary_payout():
        """ Returns the amount of money received when a player passes GO """
        return 200
    '''

    # bonus_payout()
    """ Returns community chest and chance card payouts """
    
    # mortgage_payout(deed)
    """ Returns the mortgage value of the given deed """

    # conduct_auction()
    """ Holds an auction between players for a deed """

    # deed_purchase()
    """ Handles the purchase of a deed between the deed price and player balance """

    # house_purchase()
    """ Handles the purchase of a house on a deed between the deed house price and the player balance """

    # hotel_purchase()
    """ Handles the purchase of a hotel on a deed between the deed hotel price and the player balance """
    """     and checks that the deed has 4 houses before hotel purchase """
        
    # tax_fines_collections()
    """ Collects taxes from special tiles and fines from Community Chest/Chance """

    # unmortgage_collections()
    """ Collects unmortgage deed funds from player """

    # bankrupt_balance_collections()
    """ Collects deeds, money, houses/hotels, and Get Out Of Jail Free card(s) from player. """
    """ Auctions deeds and conducts most if not all post-bankruptcy management """
