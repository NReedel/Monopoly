# deeds.py

###
# *Name:    Alicyn Knapp, Nate Reedel
# *Credit:  PennWest Projects! (discord server)
# *Purpose: Define Monopoly deed attributes and actions
###

from enum import Enum

class Deeds:
   # -- Constructor --
   def __init__(self, tile):
      self.index = tile['index']
      self.name = tile['name']
      self.price = tile['price']
      self.mortgage_value = tile['deed']['mortgageValue']
      self.unmortgage_value = tile['deed']['unmortgageValue']
    
class DeedStreet(Deeds):

   class StreetOption(Enum): 
      R = 0
      M_R = 1
      R_H_1 = 2
      R_H_2 = 3
      R_H_3 = 4
      R_H_4 = 5
      R_H = 6        
       
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

   #def current_rent(self, choice : int) : int 
   def current_rent(self, choice):
      # options = ["r", "m_r", "r_h_1", "r_h_2","r_h_3","r_h_4","r_H"]
      # choice = options[options_index]
      # print(choice)
      # print(self.StreetOption.MR)
      match choice:
         case self.StreetOption.R.value:
            return self.rent
         
         case self.StreetOption.M_R.value:
            return self.monopoly_rent
         
         case self.StreetOption.R_H_1.value:
            return self.rent_house_one
         
         case self.StreetOption.R_H_2.value:
            return self.rent_house_two
         
         case self.StreetOption.R_H_3.value:
            return self.rent_house_three
         
         case self.StreetOption.R_H_4.value:
            return self.rent_house_four
         
         case self.StreetOption.R_H.value:
            return self.rent_hotel
         
      return 0

class DeedRailroad(Deeds):
    
   class RailroadOption(Enum): # new
      R = 0
      R_2 = 1 
      R_3 = 2
      R_4 = 3
   
   # -- Constructor --
   def __init__(self, tile):
      super().__init__(tile)
      self.rent = tile['deed']['rent']
      self.rent_two = tile['deed']['rent2']
      self.rent_three = tile['deed']['rent3']
      self.rent_four = tile['deed']['rent4']
       
   #def current_rent(self, choice : int) : int 
   def current_rent(self, choice):
      # options = ["r", "r_2", "r_3", "r_4"]
      # choice = options[options_index]
      match choice:
         case self.RailroadOption.R.value:
            return self.rent
         
         case self.RailroadOption.R_2.value:
            return self.rent_two
         
         case self.RailroadOption.R_3.value:
            return self.rent_three
         
         case self.RailroadOption.R_4.value:
            return self.rent_four
         
      return 0

class DeedUtility(Deeds):
    
   class UtilityOption(Enum): # new
      R_M_1 = 0
      R_M_2 = 1
       
   # -- Constructor --
   def __init__(self, tile):
      super().__init__(tile)
      self.rent_multiplier_one = tile['deed']['rentMultiplier1']
      self.rent_multiplier_two = tile['deed']['rentMultiplier2']
   
   #def current_rent(self, choice : int) : int 
   def current_rent(self, choice):
      # options = ["r_m_1", "r_m_2"]
      # choice = options[options_index]
      match choice:
         case self.UtilityOption.R_M_1.value:
            return self.rent_multiplier_one
      
         case self.UtilityOption.R_M_2.value:
            return self.rent_multiplier_two
      
      return 0
