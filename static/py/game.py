# game.py
###
# *Name:      Alicyn, Chris, Nate
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Connects all other classes other than monopoly. Deals with 
#             turns, the players, and their interactions with each other,
#             the board and bank. 
###

#--Imports--
from dice import *
from players import *
# from enum import Enum
import random
class Game:
   #--Global Data--
   starting_total = int(500)
   bail = int(50)
   # monopoly_characters = ("cannon", "thimble", "top hat", "iron", "battleship", "boot", "race car","purse")
   player_events = ("roll","build","sell","mortgage","redeem","trade","menue")
   jailed_player_events = ("roll doubles","pay jail fee","jail free card")
   payment = int(0) # Note: used to store return value from pay_money() and used as arg in recieve_money()
   game_dice = Dice(2,1)
   turn = int(1)
   round = int(1)
   starting_player_count = int(0)
   all_players = []
   # the_Bank = Bank()
   # the_Tiles = Tiles()

   # #--Method Implementations--
   # move(self,Player : Players) : void
   def move(self,player): 
      
      self.game_dice.roll()
      print("\t\tplayer",player.player_number(),"rolled =",self.game_dice.print_roll()) # add roll total
      next_location = player.current_location()
      next_location  += (self.game_dice.total_rolled())
      if next_location >= 40:
         player.receive_money(200)
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
            player.receive_amount(200)
            next_location = next_location % 40
            
         player.move_location(next_location) # move
         print("")  
         return False # in_jail = False
      else:
         print("\t\tplayer",player.player_number(),"remains in jail")
         print("")  
         return True # in_jail = True
   

      
   # player_event(self player : Players, event : string) : void
   def player_event(self,player,event = ""):
      
      if event == "roll":
         self.move(player)
         
      # if event == "build":
      # if event == "sell":
      # if event == "mortgage":
      # if event == "redeem":
      # if event == "trade"
      # if event == "menue":
   
      
   # jailed_player_event(player : Players, event : string) : bool
   def jailed_player_event(self,player,event=""): #new
      
      if event == "roll doubles":
         return True # attempt_escape == True
      
      if event == "pay jail fee":   
         player.pay_money(self.bail)
         player.time_jailed == 0
         print("\t\tPlayer",player.player_number(),"is now out of jail\n")
         return False #player.in_jail == False
      
      if event == "jail free card":
         player.jail_free_card -= 1
         player.time_jailed == 0
         print("\t\tPlayer",player.player_number(),"is now out of jail\n")
         return False #player.in_jail == False
      
      return True

   # player_landed_on(player_location : int)

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
      if target_players[self.turn-1].in_debt() == True: # if Target_players is in dept
         print("\t\tplayer",target_players[self.turn-1].player_number(),"is in dept at $",target_players[self.turn-1].current_money())
         give_up = "y"
         # give_up = input("\tWould the Target_players like to continue y/n? ")
         if give_up == "y":
            target_players[self.turn-1].bankrupt = True
            return 
      # while Target_players[self.turn-1].in_dept() == True: 
      if target_players[self.turn-1].in_jail == True:
         target_players[self.turn-1].time_jailed += 1
      ###List Target_players Events (dynamic actions) 
      has_rolled = False
      end_turn = False
      attempt_escape = False
      ###start self.turn
      while end_turn == False:
         ###jailed player events
         if target_players[self.turn-1].in_jail == True and has_rolled == False: 
            global bail
            print("\t\tSelect Jailed player action:")
            print("\t\t   0)",self.jailed_player_events[0])
            print("\t\t   1)",self.jailed_player_events[1],"$",self.bail) # needs if statment for being broke
            if target_players[self.turn-1].jail_free_card > 0: 
               print("\t\t   2)", self.jailed_player_events[2])
            target_event = input("\t\tchoice -> ")
            
            while int(target_event) < 0 or len(self.jailed_player_events) <= int(target_event) or int(target_event == 2) and target_players[self.turn-1].jail_free_card == 0:
               print("\t\tInvalid choice, try again")
               print("\t\t\nSelect Jailed Target_players action:")
               if has_rolled == False: 
                  print("\t\t   0)",self.jailed_player_events[0])
               print("\t\t   1)",self.jailed_player_events[1],"$",bail) # needs if statment for being broke
               if target_players[self.turn-1].jail_free_card > 0: 
                  print("\t\t   2)", self.jailed_player_events[2])
               target_event = input("\t\tchoice -> ")
               
            print("")
            
            if int(target_event) == 0:
               ###jailed_player_event reself.turns True automatically
               attempt_escape = self.jailed_player_event(target_players[self.turn-1],self.jailed_player_events[int(target_event)])
            else:
               ###jailed_player_event reself.turns True if Target_players stays in jail
               target_players[self.turn-1].in_jail= self.jailed_player_event(target_players[self.turn-1],self.jailed_player_events[int(target_event)])
         
         ###player events     
         print("\t\tSelect players action:")  
         
         if has_rolled == True: 
            print("\t\t   0) pass turn")
         else: 
            print("\t\t   0)",self.player_events[0])
         ###more events to come!   
         target_event = input("\t\tchoice -> ")
         while int(target_event) < 0 or len(self.player_events) < int(target_event):
            ###redisplay if given bad input
            print("\t\tInvalid choice, try again")
            print("\n\t\tSelect players action:")
            
            if has_rolled == True: 
               print("\t\t   0) pass turn")
            else: 
               print("\t\t   0)",self.player_events[0])
                  
            target_event = input("\t\tchoice -> ")
            
         if int(target_event) == 0 and has_rolled == False:
            has_rolled = True
         elif int(target_event) == 0 and has_rolled == True:
            end_turn = True         
            
         if end_turn  == False:
            print("")
            
            if (attempt_escape == True and int(target_event) != 0) or attempt_escape == False:   
               self.player_event(target_players[self.turn-1],self.player_events[int(target_event)])

            if attempt_escape == True and int(target_event) == 0:
               print("\t\tattempt jail escape")
               target_players[self.turn-1].in_jail = self.jailed_move_attempt(target_players[self.turn-1])
               has_rolled = True
            elif self.game_dice.rolled_same_values() == True and target_players[self.turn-1].same_values_rolled == 2 and self.player_events[int(target_event)] == "roll":   
               print("\t\tsame values rolled = ",target_players[self.turn-1].same_values_rolled+1)
               target_players[self.turn-1].go_to_jail()
               print("")
               target_players[self.turn-1].same_values_rolled += 1
               self.turn += 1
               self.end_round_check(target_players)
               return
      ###end of self.turn
      if(self.game_dice.rolled_same_values() == False or attempt_escape == True):   
         self.turn += 1
      else:
         target_players[self.turn-1].same_values_rolled += 1
         print("\n\t\tPlayer",self.turn,"goes again")
         
      if self.turn > len(target_players): # reset self.turns, start next self.round
         ##(not part of actual code)
         # payment = 300      
         # Target_players[self.turn-2].pay_money(payment)
         # Target_players[0].receive_money(payment)
         # payment = 0
         ##(end not part of actual code)  
         ###(not part of actual code)      
         # payment = int(300)
         # Target_players[self.turn-2].set_balance(int(Target_players[self.turn-2].current_money()) - int(payment))
         # print("\t\tplayer",Target_players[self.turn-2].player_number(),"payed",payment)
         # Target_players[0].set_balance(int(Target_players[0].current_money()) + int(payment))
         # print("\t\tplayer",Target_players[0].player_number(),"payed",payment)
         # print()
         ###(end not part of actual code)
         self.end_round_check(target_players)   
      else:
         print("")
   #end take_turn
#end class

      
