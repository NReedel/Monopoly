# game.py

###
# *Name:      Alicyn Knapp, Chris Schneider, Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Connects all other classes other than monopoly. Deals with 
#             turns, the players, and their interactions with each other,
#             the board and bank. 
###

#--Imports--
# from enum import Enum
import random
import json
# import sys #?
# sys.path.insert(0, '/Users/Nreed/Code/All_Code/Monopoly/static/Json') #?
from tiles import *
from dice import *
from players import *
from events import *
from board import *
from bank import *


class Game:
   #--Global Data--
   starting_total = int(500)
   bail = int(50)
   # monopoly_characters = ("cannon", "thimble", "top hat", "iron", "battleship", "boot", "race car","purse")
   payment = int(0) # Note: used to store return value from pay_money() and used as arg in recieve_money()
   game_dice = Dice(2,6)
   turn = int(1)
   round = int(1)
   starting_player_count = int(0)
   all_players = []
   bank = Bank()
   # the_Tiles = Tiles()

   def __init__(self):
       with open('tiles.json', 'r') as rf:
           for tiles in json.load(rf):
               if tiles['type'] == "street":
                   self.bank.deeds.append(DeedStreet(tiles))
               if tiles['type'] == "railroad":
                   self.bank.deeds.append(DeedRailroad(tiles))
               if tiles['type'] == "utility":
                   self.bank.deeds.append(DeedUtility(tiles))

   # #--Method Implementations--
   # move(self,Player : Players) : void
   def move(self,player): 
      
      self.game_dice.roll()
      print("\t\tplayer",player.player_number(),"rolled =",self.game_dice.print_roll()) # add roll total
      next_location = player.current_location()
      next_location  += (self.game_dice.total_rolled())
      if next_location >= 40:
         self.player.change_balance(self.bank.receive_money(player.current_money(), 200))
         next_location = next_location % 40
      player.move_location(next_location) 
      print("")

      
   #make_payment(Payer : T, Recipient :  T, paymnet : int) : void

   # jailed_move_attempt(self, player : Players) : void
   def jailed_move_attempt(self,player): 
      
      self.game_dice.roll()
      print("\t\tplayer",player.player_number(),"rolled =",self.game_dice.print_roll())
      
      if self.game_dice.rolled_same_values() == True or player.time_jailed == 3:
         
         if player.time_jailed == 3 and Dice.rolled_same_values() == False:
            player.time_jailed == 0
            global bail
            player.pay_money(bail)    
            
         print("\t\tplayer",player.player_number(),"is now out of jail")
         next_location = player.current_location()
         next_location += self.game_dice.total_rolled()
         
         if next_location >= 40:
            self.player.change_balance(self.bank.receive_money(player.current_money(), 200))
            next_location = next_location % 40
            
         player.move_location(next_location) # move
         print("")  
         return False # in_jail = False
      else:
         print("\t\tplayer",player.player_number(),"remains in jail")
         print("")  
         return True # in_jail = True

   # end_round_check(RemainingPlayers : list<Players>) : void
   def end_round_check(self,remainingPlayers = []):
      
      if self.turn > len(remainingPlayers): # reset turns, start next round
         self.turn = self.turn % len(remainingPlayers) 
         self.round += 1
         print("")
         print("Round ",self.round)
         print("")
                  
         for i in range(0,len(remainingPlayers)):
            remainingPlayers[i].same_values_rolled = 0

   # take_self.turn(Target_players : list<Players>) : void
   def take_turn(self,target_players = []):
      print("\tPlayer",self.turn, ":") 
      ###List Target_players Status 
      target_players[self.turn-1].player_status()
      ###new
      while target_players[self.turn-1].in_debt() == True: 
         ###In debt
         # global bankrupt_player_events
         bankrupt_player_events = BankruptPlayerEvents()
         print("\t\tplayer",target_players[self.turn-1].player_number(),"is in dept at","$"+str(target_players[self.turn-1].current_money()),"\n")
         target_event = bankrupt_player_events.display_event_options()
         while int(target_event) < 0 or len(bankrupt_player_events.events) <= int(target_event):
            ###redisplay if given bad input
            print("\t\tInvalid choice, try again\n")
            target_event = bankrupt_player_events.display_event_options()
         bankrupt_player_events.event(target_players[self.turn-1],bankrupt_player_events.events[int(target_event)])

         if target_players[self.turn-1].bankrupt == True:
            return 
      ###end new 
      if target_players[self.turn-1].in_jail == True:
         target_players[self.turn-1].time_jailed += 1
      has_rolled = False
      end_turn = False
      attempt_escape = False
      ###Events
      player_events =  PlayerEvents(self,has_rolled) 
      player_events.arg[1] = has_rolled #? 
      jailed_player_events =  JailedPlayerEvents(self) 
      ###Start Turn
      while end_turn == False:
         ###Jailed Player Events
         if target_players[self.turn-1].in_jail == True and has_rolled == False: 
            target_event = jailed_player_events.display_event_options(target_players[self.turn-1]) 
            while int(target_event) < 0 or len(jailed_player_events.events) <= int(target_event) or int(target_event == 2) and target_players[self.turn-1].jail_free_card == 0:
               ###redisplay if given bad input
               print("\t\tInvalid choice, try again\n")
               target_event = jailed_player_events.display_event_options(target_players[self.turn-1])
            print("")
            
            if int(target_event) == 0:
               ###jailed_player_events.event returns True automatically
               attempt_escape = jailed_player_events.event(target_players[self.turn-1],jailed_player_events.events[int(target_event)])
            else:
               ###jailed_player_events.event returns True if player stays in jail
               target_players[self.turn-1].in_jail = jailed_player_events.event(target_players[self.turn-1],jailed_player_events.events[int(target_event)])
         ###Player Events
         target_event = player_events.display_event_options() 
         while int(target_event) < 0 or len(player_events.events) <= int(target_event):
            ###redisplay if given bad input
            print("\t\tInvalid choice, try again\n")
            target_event = player_events.display_event_options()
         ###Player Menu Quit #new  
         if target_players[self.turn-1].bankrupt == True: 
            return
         ###end Player Menu Quit #new
         if int(target_event) == 0 and has_rolled == False:
            has_rolled = True
            player_events.arg[1] = has_rolled 
         elif int(target_event) == 0 and has_rolled == True:
            end_turn = True         
            
         if end_turn  == False:
            print("")
            if (attempt_escape == True and int(target_event) != 0) or attempt_escape == False:   
               player_events.event(target_players[self.turn-1],player_events.events[int(target_event)]) 
            if attempt_escape == True and int(target_event) == 0:
               print("\t\tattempt jail escape")
               target_players[self.turn-1].in_jail = self.jailed_move_attempt(target_players[self.turn-1])
               has_rolled = True
            elif self.game_dice.rolled_same_values() == True and target_players[self.turn-1].same_values_rolled == 2 and player_events.events[int(target_event)] == "roll":   
               print("\t\tsame values rolled =",target_players[self.turn-1].same_values_rolled+1)
               target_players[self.turn-1].go_to_jail()
               print("")
               target_players[self.turn-1].same_values_rolled += 1
               self.turn += 1
               self.end_round_check(target_players)
               return
      ###End Of Turn
      del player_events
      if(self.game_dice.rolled_same_values() == False or attempt_escape == True):   
         self.turn += 1
      else:
         target_players[self.turn-1].same_values_rolled += 1
         print("\n\t\tPlayer",self.turn,"goes again")
         
      print("")
      
      if self.turn > len(target_players): # reset self.turns, start next self.round
         self.end_round_check(target_players)   
   #end take_turn
#end class

      
