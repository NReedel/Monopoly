# deeds.py

###
# *Name:    Alicyn Knapp
# *Credit:  PennWest Projects! (discord server)
# *Purpose: Define Monopoly deed attributes and actions
###


class Deeds:
    # -- Constructor --
    def __init__(self, tile):
        self.index = tile['index']
        self.name = tile['name']
        self.price = tile['price']
        self.mortgage_value = tile['deed']['mortgageValue']
        self.unmortgage_value = tile['deed']['unmortgageValue']


class DeedStreet(Deeds):
    # -- Constructor --
    def __init__(self, tile):
        super().__init__(tile)
        self.rent = tile['deed']['rent']
        self.monopoly_rent = tile['deed']['monopolyRent']
        self.rent_house_one = tile['deed']['rentHouse1']
        self.rent_house_two = tile['deed']['rentHouse2']
        self.rent_house_three = tile['deed']['rentHouse3']
        self.rent_house_four = tile['deed']['rentHouse4']
        self.rent_hotel = tile['deed']['rentHotel']
        self.house_cost = tile['deed']['houseCost']
        self.hotel_cost = tile['deed']['hotelCost']


class DeedRailroad(Deeds):
    # -- Constructor --
    def __init__(self, tile):
        super().__init__(tile)
        self.rent = tile['deed']['rent']
        self.rent_two = tile['deed']['rent2']
        self.rent_three = tile['deed']['rent3']
        self.rent_four = tile['deed']['rent4']


class DeedUtility(Deeds):
    # -- Constructor --
    def __init__(self, tile):
        super().__init__(tile)
        self.rent_multiplier_one = tile['deed']['rentMultiplier1']
        self.rent_multiplier_two = tile['deed']['rentMultiplier2']
