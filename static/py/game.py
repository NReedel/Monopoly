# game.py

###
# *Name:      Alicyn Knapp, Chris Schneider, Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Connects all other classes other than monopoly. Deals with 
#             turns, the players, and their interactions with each other,
#             the board and bank. 
###

#--Imports--
from tkinter import CURRENT
from dice import *
from players import *
from tiles import *
from bank import *
from events import *
from board import *
from deeds import *
# from enum import Enum
# import random
import json
import copy

class Game:
   ###--Global Data--
   starting_total = int(2500)
   bail = int(50)
   monopoly_characters = ("cannon", "thimble", "top hat", "iron", "battleship", "boot", "race car","purse") 
   payment = int(0) # maybe
   game_dice = Dice(2,6)
   turn = int(1)
   round = int(1)
   all_players = []
   bank = Bank()
   board = Board()
   # Events
   player_events = PlayerEvents()
   jailed_player_events = JailedPlayerEvents()
   bankrupt_player_events = BankruptPlayerEvents()
   
   ###--Constructor--
   def __init__(self):
      # Load Json here, use your own link 💬
      # with open('/mnt/c/Users/Nreed/Code/All_Code/Monopoly/static/Json/tiles.json', 'r') as rf:
      with open('tiles.json', 'r') as rf:
         for tiles in json.load(rf):
            if tiles['type'] == "street":
               self.bank.deeds.append(DeedStreet(tiles))
               self.board.tile[tiles['index']].owned_by = "bank" 
            if tiles['type'] == "railroad":
               self.bank.deeds.append(DeedRailroad(tiles))
               self.board.tile[tiles['index']].owned_by = "bank"
            if tiles['type'] == "utility":
               self.bank.deeds.append(DeedUtility(tiles))
               self.board.tile[tiles['index']].owned_by = "bank"
         
         self.board.tile_check(self.all_players) 

   # def transfer_all(self): 
   #    starting_deeds_size = len(self.bank.deeds) # 
   #    for i in range(0,starting_deeds_size):
   #       self.transfer_deed(self.bank,self.all_players[0],self.bank.deeds[i].index)

   ###--Method Implementations--
   # pass_GO(self, player)
   def pass_GO_check(self, player):
      # passing or landing on GO
      if next_location >= 40:
         player.receive_money(200)
         next_location = next_location % 40

        
   # move(self,Player : Players,  spaces_moving: int) : void
   def move(self,player,spaces_moving): 
      next_location = player.current_location() + (spaces_moving)
      
      self.pass_GO_check(player)
         
      player.move_location(next_location, self.board.location(next_location)) # new
      print("")
      current_tile = self.board.tile[next_location]

      if current_tile.tile_type != "special": # tile with deed
         
         if current_tile.avaliable_deed() == True : # purchasable
            print("\t\tthis property can be bought\n")
            avaliable_property_events = AvaliablePropertyEvents(self)
            cost = current_tile.property_cost
            can_buy = False
            if cost <= player.current_money():
               can_buy = True
            target_event = avaliable_property_events.display_event_options(cost, player.current_money())
            
            while ((int(target_event) < 0 or len(avaliable_property_events.events)) <= int(target_event) and can_buy == True) or (can_buy == False and (int(target_event) >= len(avaliable_property_events.events) or int(target_event) < 1)):
               print("\t\tinvalid choice, try again\n")
               target_event = avaliable_property_events.display_event_options(cost, player.current_money())
               
            avaliable_property_events.event(avaliable_property_events.events[int(target_event)])
            del avaliable_property_events
         elif current_tile.is_mortgaged == True: #mortgaged property
            print("\t\tproperty is mortgaged\n")
            return
         elif current_tile.owned_by == player.id: # self owned
            print("\t\tyou own this property\n")
         elif current_tile.owned_by != player.id and current_tile.owned_by != "bank": # pay rent
            print("\t\tyou landed on another player's property\n")
            owner_number = int(current_tile.owned_by)
            rent_type = 0 # rent # default
            ### street tiles
            if current_tile.tile_type == "street":
               if current_tile.has_monopoly == True:
                  rent_type = 1 # monopoly_rent
               if current_tile.houses > 0:
                  rent_type =  self.board.tiles[next_location].houses + 1 # rent_house_
               if current_tile.hotels > 0:
                  rent_type = 6 # rent_hotel_
            ### utilites
            if current_tile.tile_type  == "utilities":      
               if current_tile.multiplier == 2:
                  rent_type = 1
            ### railroad
            if current_tile.tile_type == "railroad":
               if current_tile.multiplier == 2:
                  rent_type = 1
               elif current_tile.multiplier == 3:
                  rent_type = 2
               elif current_tile.multiplier == 4:
                  rent_type = 3
            current_deed = self.all_players[owner_number-1].target_deed(next_location)
            payment = current_deed.current_rent(rent_type)
            #   options = ["r", "m_r", "r_h_1", "r_h_2","r_h_3","r_h_4","r_H"]
            self.transfer_payment(player,self.all_players[owner_number-1],payment)

            print("")     
            
      else: # landing on special tile
         # corner tiles (GO, Just Visiting, Go To Jail, Free Parking)
         if current_tile.corner_type == "go":
             pass
         elif current_tile.corner_type == "jail":
             pass
         elif current_tile.corner_type == "parking":
             pass
         elif current_tile.corner_type == "arrested":   # Go To Jail
             player.go_to_jail()
         # tax tiles
         elif current_tile.special_type == "tax":
             player.pay_money(current_tile.tax_amount)
         # card tiles
         elif current_tile.card_type == "chance":
             pass
         elif current_tile.card_type == "chest":
             pass

         return      
      
   # # transfer_payment(payer : T, recipient :  T, paymnet : int) : void
   def transfer_payment(self,payer, recipient, payment): 
      payer.pay_money(payment)
      recipient.receive_money(payment)

      
   # transfer_deed(owner: T, recipient :  T, location : int) : void
   def transfer_deed(self,owner, recipient, location): 
      owner_deeds = copy.deepcopy(owner.deeds) # maybe
      recipient_deeds = copy.deepcopy(recipient.deeds)

      for i in range(0,len(owner_deeds)): 
         
         if location == owner_deeds[i].index:
            target_deed = owner_deeds[i]
            i = len(owner_deeds)

      recipient_deeds.append(target_deed)
      recipient.deeds = copy.deepcopy(recipient_deeds)
      print("\t\t\""+str(target_deed.name)+"\"","received\n")
      self.board.tile[location].owned_by = recipient.id
      self.board.tile_check(self.all_players)


   # jailed_move_attempt(self, player : Players) : void
   def jailed_move_attempt(self,player): 
      
      self.game_dice.roll()
      print("\t\tplayer",player.id(),"roll =",self.game_dice.print_roll())
      
      if self.game_dice.rolled_same_values() == True or player.time_jailed == 3:
         
         if player.time_jailed == 3 and self.game_dice.rolled_same_values() == False:
            player.time_jailed = 0
            global bail
            player.pay_money(self.bail)    
            
         print("\t\tplayer",player.id(),"is now out of jail")
         next_location = player.current_location() + self.game_dice.total_rolled()
         
         self.pass_GO_check(player)
            
         player.move_location(next_location) # move
         print("")  
         return False # in_jail = False
      
      else:
         print("\t\tplayer",player.id(),"remains in jail")
         print("")  
         return True # in_jail = True

   # end_round_check(RemainingPlayers : list<Players>) : void
   def end_round_check(self,remainingPlayers = []):
      
      if self.turn > len(remainingPlayers): # reset turns, start next round
         self.turn = self.turn % len(remainingPlayers) 
         self.round += 1
         print("Round ",self.round)
         print("")
                  
         for i in range(0,len(remainingPlayers)):
            remainingPlayers[i].same_values_rolled = 0

   # take_self.turn(Target_players : list<Players>) : void
   def take_turn(self,target_players = []):
      print("\tPlayer",target_players[self.turn-1].id, ":") 
      ###List Target_players Status 
      target_players[self.turn-1].player_status(self.board.tile)  
      
      while target_players[self.turn-1].in_debt() == True: 
         ###Bakrupt Player Events 
         self.bankrupt_player_events.update(self)
         print("\t\tplayer",target_players[self.turn-1].id,"is in dept at","$"+str(target_players[self.turn-1].current_money()),"\n")
         target_event = self.bankrupt_player_events.display_event_options()
         
         while int(target_event) < 0 or len(self.bankrupt_player_events.events) <= int(target_event):
            ###redisplay if given bad input
            print("\t\tInvalid choice, try again\n")
            target_event = self.bankrupt_player_events.display_event_options()
            
         self.bankrupt_player_events.event(target_players[self.turn-1],self.bankrupt_player_events.events[int(target_event)])
         if target_players[self.turn-1].bankrupt == True:
            return 
         
      if target_players[self.turn-1].in_jail == True:
         target_players[self.turn-1].time_jailed += 1
      self.player_events.update(self)
      self.jailed_player_events.update(self)
      has_rolled = False
      end_turn = False
      attempt_escape = False
      ###Start Turn
      while end_turn == False:
         ###Jailed Player Events
         if target_players[self.turn-1].in_jail == True and has_rolled == False: 
            target_event = self.jailed_player_events.display_event_options(target_players[self.turn-1]) 
            while int(target_event) < 0 or len(self.jailed_player_events.events) <= int(target_event) or int(target_event == 2) and target_players[self.turn-1].jail_free_card == 0:
               ###redisplay if given bad input
               print("\t\tInvalid choice, try again\n")
               target_event = self.jailed_player_events.display_event_options(target_players[self.turn-1])
            print("")
            
            if int(target_event) == 0:
               ###jailed_player_events.event returns True automatically
               attempt_escape = self.jailed_player_events.event(target_players[self.turn-1],self.jailed_player_events.events[int(target_event)])
            else:
               ###jailed_player_events.event returns True if player stays in jail
               target_players[self.turn-1].in_jail = self.jailed_player_events.event(target_players[self.turn-1],self.jailed_player_events.events[int(target_event)])
         ###Player Events
         if target_players[self.turn-1].bankrupt == False: 
            target_event = self.player_events.display_event_options(has_rolled) 
            while int(target_event) < 0 or len(self.player_events.events) <= int(target_event):
               ###redisplay if given bad input
               print("\t\tInvalid choice, try again\n")
               target_event = self.player_events.display_event_options(has_rolled)
         ###Player Menu Quit 
         if target_players[self.turn-1].bankrupt == True:
            has_rolled = True
            end_turn = True
            return 
         ###end Player Menu Quit
         if int(target_event) == 0 and has_rolled == False:
            has_rolled = True
         elif int(target_event) == 0 and has_rolled == True:
            end_turn = True
         else:
            pass         
            
         if end_turn  == False:
            print("")
            if (attempt_escape == True and int(target_event) != 0) or attempt_escape == False:   
               self.player_events.event(target_players[self.turn-1],self.player_events.events[int(target_event)]) 
            if attempt_escape == True and int(target_event) == 0:
               print("\t\tattempt jail escape")
               target_players[self.turn-1].in_jail = self.jailed_move_attempt(target_players[self.turn-1])
               has_rolled = True
               
            elif self.game_dice.rolled_same_values() == True and target_players[self.turn-1].same_values_rolled == 2 and self.player_events.events[int(target_event)] == "roll":   
               print("\t\tsame values rolled =",target_players[self.turn-1].same_values_rolled+1)
               target_players[self.turn-1].go_to_jail()
               print("")
               target_players[self.turn-1].same_values_rolled += 1
               self.turn += 1
               self.end_round_check(target_players)
               return
           
      ###End Of Turn
      if(self.game_dice.rolled_same_values() == False or attempt_escape == True):   
         self.turn += 1
      else:
         target_players[self.turn-1].same_values_rolled += 1
         print("\n\t\tPlayer",target_players[self.turn-1].id,"goes again")
         
      print("")
      
      if self.turn > len(target_players): # reset self.turns, start next self.round
         self.end_round_check(target_players)
 
   # end take_turn
   

# end class   

      
