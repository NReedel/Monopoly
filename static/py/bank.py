# bank.py

#
# *Name:    Alicyn Knapp
# *Credit:  PennWest Projects! (discord server)
# *Purpose: Define Monopoly bank traits and actions
#

import json
from . import deeds


class Bank:
    ### -- Constructor ###
    def __init__(self):
        ### -- Data -- ###
        # bills = {'ones': 40, 'fives': 40, 'tens': 40, 'twenties': 50, 'fifties': 30, 'hundreds': 20, 'five_hundreds': 20}
        self.deeds = list()
        self.id = "bank" 
        houses = 32
        hotels = 12

    ### -- Methods -- ###
    
   # recieve_money(self, amount : int) : void
    def receive_money(self,amount):
        amount = 0
        return
   
   # pay_money(self, amount : int ) : void
    def pay_money(self,amount):
        amount = 0
        return
    
   # buy_property(deed : deeds) : void
    def add_property(self,deed):
      self.deeds.append(deed)
      
   # remove_property(property : int, reciever : string ) : # maybe
    def remove_property(self,index):
      for i in range(len(self.deeds)):
         if index == self.deeds[i].index:
            target_deed = self.deeds[i]
            self.deeds.pop(i)
            return target_deed

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
