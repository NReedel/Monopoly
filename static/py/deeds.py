# deeds.py

###
# *Name: Alicyn Knapp
# *Credit: PennWest Projects! (discord server)
# *Purpose: Define Monopoly deed attributes and actions
###

from enum import Enum

# Used as indices?
class Deed_Names(Enum):
    BALTIC = 0
    BOARDWALK = 1

class Deeds:
    ''' -- Constructor '''
    def __init__(self):
        ''' -- Data -- '''
        self.__baltic = {
            'name': 'Baltic Avenue',
            'price': 60,
            'house_hotel': 50,
            'mortgage': 30,
            'unmortgage': 33
            }

        self.__boardwalk = {
            'name': 'Boardwalk',
            'price': 400,
            'house_hotel': 200,
            'mortgage': 200,
            'unmortgage': 220
            }

        self.__deeds_list = [
            self.__baltic,
            self.__boardwalk
            # will expand as more deeds are added
            ]

    def get_deed_list(self):
        return self.__deeds_list

    def get_deed_price(self, deed_name):
        # search algorithm to find where deed_name == deed['name']
        pass


    # give_deed()
    # return_deed()
