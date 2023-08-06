# game.py

###
# *Name:      Alicyn Knapp, Chris Schneider, Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Connects all other classes other than monopoly. Deals with 
#             turns, the players, and their interactions with each other,
#             the board and bank. 
###

#--Imports--
from dice import *
from players import *
from tiles import *
from bank import *
from events import *
from board import *
# from enum import Enum
import random
import copy
# import json

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
   # for i in range(len(all_players)):
   #    all_players[i].location_name = str(board.tile[0].tile_name)
   # Events
   player_events = PlayerEvents()
   jailed_player_events = JailedPlayerEvents()
   bankrupt_player_events = BankruptPlayerEvents()
   
   ###--Constructor--
   def __init__(self):
      # Load Json here, use your own link 💬
      with open('/mnt/c/Users/Nreed/Code/All_Code/Monopoly/static/Json/tiles.json', 'r') as rf:
      # with open('tiles.json', 'r') as rf:
         for tiles in json.load(rf):
            if tiles['type'] == "street":
               self.bank.deeds.append(DeedStreet(tiles))
            if tiles['type'] == "railroad":
               self.bank.deeds.append(DeedRailroad(tiles))
            if tiles['type'] == "utility":
               self.bank.deeds.append(DeedUtility(tiles))

   ###--Method Implementations--
   # move(self,Player : Players,  spaces_moving: int) : void
   def move(self,player,spaces_moving): 
      next_location = player.current_location() + (spaces_moving)
      if next_location >= 40:
         player.receive_money(200)
         next_location = next_location % 40
         
      player.move_location(next_location, self.board.location(next_location)) 
      print("")
      # new
      if self.board.tile[next_location].tile_type != "special" and self.board.tile[next_location].owned_by == "bank" : # not a special tile
         print("\t\tthis property can be bought\n")
         if self.board.tile[next_location].avaliable_deed() == True:
         # AvaliablePropertyEvents
            avaliable_property_events = AvaliablePropertyEvents(self)
            target_event = avaliable_property_events.display_event_options(self.board.tile[next_location].property_cost)
            avaliable_property_events.event(avaliable_property_events.events[int(target_event)])
            
         # AuctionPropertyEvents 
         # else:
            # pay rent
         del avaliable_property_events
         print()
      # end new
      
   # transfer_payment(payer : T, recipient :  T, paymnet : int) : void
   def transfer_payment(self,payer, recipient, payment): # new
      payer.pay_money(payment)
      recipient.receive_money(payment)

   # transfer_deed(owner: T, recipient :  T) : void
   def transfer_deed(self,owner, recipient, location): # new
      # owner_deeds = copy.deepcopy(owner.deeds) # maybe
      recipient_deeds = copy.deepcopy(recipient.deeds)
      target_deed = owner.remove_property(location)
      # if recipient.id != "bank":
      # recipient.add_property(target_deed)
      recipient_deeds.append(target_deed)
      recipient.deeds = copy.deepcopy(recipient_deeds)
      # self.all_players[self.turn-1].deeds.append(target_deed)
      print("\t\t\""+str(target_deed.name)+"\"","received")
      self.board.tile[location].owned_by = recipient.id
      del target_deed
      del recipient_deeds

   # jailed_move_attempt(self, player : Players) : void
   def jailed_move_attempt(self,player): 
      
      self.game_dice.roll()
      print("\t\tplayer",player.id,"roll =",self.game_dice.print_roll())
      
      if self.game_dice.rolled_same_values() == True or player.time_jailed == 3:
         
         if player.time_jailed == 3 and self.game_dice.rolled_same_values() == False:
            player.time_jailed = 0
            global bail
            player.pay_money(self.bail)    
            
         print("\t\tplayer",player.id,"is now out of jail")
         next_location = player.current_location()
         next_location += self.game_dice.total_rolled()
         
         if next_location >= 40:
            player.receive_amount(200)
            next_location = next_location % 40
            
         player.move_location(next_location) # move
         print("")  
         return False # in_jail = False
      
      else:
         print("\t\tplayer",player.id,"remains in jail")
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
      target_players[self.turn-1].player_status()
      
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
         if target_players[self.turn-1].bankrupt == False: # new
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

      
