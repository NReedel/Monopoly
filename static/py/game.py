# game.py
###
# *Name:      Alicyn, Chris, Nate
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Monopoly game, parent  class or main executable that links 
#             all objects. Contains all game elements
###

#--Imports--
from players import *
# from enum import Enum
import random

#--Global Data--
starting_total = int(500)
bail = int(50)
# monopoly_characters = ("cannon", "thimble", "top hat", "iron", "battleship", "boot", "race car","purse")
player_events = ("roll","build","sell","mortgage","redeem","menue")
jailed_player_events = ("roll doubles","pay jail fee","jail free card")
# bankrupt_player_events = ("")                       
# avaliable_property_events = ("")
# auction_property_events = ("")
payment = int(0) # Note: used to store return value from pay_money() and used as arg in recieve_money()
die = [0,0]
turn = int(1)
round = int(1)
starting_player_count = int(0)
all_players = []
# the_bank = bank()

#--Method Implementations--
# roll(pair : list <int>) : void 
def roll(pair): 
   # ###not part of actual code
   # if round == 1: 
   #    pair[0] = random.randint(1,1)
   #    pair[1] = random.randint(1,1)
   # else:
    ###end not part of actual code  
   pair[0] = random.randint(1,6)
   pair[1] = random.randint(1,6)
         
# move(player : players) : void
def move(player): #new, changed arg to single datatype
   global die
   # global turn 
   die = [0,0]
   roll(die) # roll
   print("\t\tplayer",player.player_number(),"rolled =",die[0],die[1])
   next_location = player.current_location()
   next_location  += (die[0]+die[1])
   if next_location >= 40:
      player.recieve_money(200)
      next_location = next_location % 40
   player.move_location(next_location) # move
   print("")

# jailed_move_attempt(player : players) : void
def jailed_move_attempt(player): #new
   global die
   # global turn 
   die = [int(0),int(0)]
   roll(die) # roll
   print("\t\tplayer",turn,"rolled = ",die[0],die[1])
   if player.rolled_doubles(die[0],die[1]) == True or player.time_jailed == 3:
      if player.time_jailed == 3 and player.rolled_doubles(die[0],die[1]) == False:
         player.time_jailed == 0
         global bail
         player.pay_money(bail)    
      print("\t\tplayer",player.player_number(),"is now out of jail")
      next_location = player.current_location()
      next_location  += (die[0]+die[1])
      die[0]=0
      die[1] =1
      if next_location >= 40:
         player.recieve_amount(200)
         next_location = next_location % 40
      player.move_location(next_location) # move
      print("")  
      return False # so in_jail = False
   else:
      print("\t\tplayer",player.player_number(),"remains in jail")
      print("")  
      return True # so in_jail = True
 
# display_player_events( target_player : player ) : void #maybe? 
   
# player_event(player : players, event : string) : void
def player_event(player,event = ""):
   if event == "roll":
      move(player)
   # if event == "build":
   # if event == "sell":
   # if event == "mortgage":
   # if event == "redeem":
   # if event == "menue":
   
# display_jailed_player_events( target_player : player ) : void #maybe?    
   
# jailed_player_event(player : players, event : string) : bool
def jailed_player_event(player,event=""): #new
   
   if event == "roll doubles":
      return True 
      # attempt_escape == True
   
   if event == "pay jail fee": 
      global bail
      player.pay_money(bail)
      player.time_jailed == 0
      print("\t\tPlayer",player.player_number(),"is now out of jail\n")
      return False #player.in_jail == False
   
   if event == "jail free card":
      player.jail_free_card -= 1
      player.time_jailed == 0
      print("\t\tPlayer",player.player_number(),"is now out of jail\n")
      return False #player.in_jail == False
   
   return True

# display_bankrupt_player_events(player : Players, event : string) : void #maybe
      
# bankrupt_player_event(player : Players, event : string) : void

# player_landed_on(player_location : int)

# avaliable_property_event(player : Players, event : string) : void

# auction_property_event(player : Players, event : string) : void

# end_round_check(remaining_players : list<players>) : void
def end_round_check(remaining_players = []):
   global turn
   if turn > len(remaining_players): # reset turns, start next round
      turn = turn % len(remaining_players) 
      global round 
      round += 1
      print("")
      print("Round ",round)
      print("")
               
      for i in range(0,len(remaining_players)):
         remaining_players[i].doubles_rolled = 0

# take_turn(target_players : list<players>) : void
def take_turn(target_players = []): ### ! make target_players target_playerss
   global turn 
   global round 
   print("\tPlayer",turn, ":") 
   ###List Target_players Assets 
   target_players[turn-1].player_status() 
   if target_players[turn-1].in_debt() == True: # if target_players is in dept
      print("\t\tplayer",target_players[turn-1].player_number(),"is in dept at $",target_players[turn-1].current_money())
      give_up = "y"
      # give_up = input("\tWould the target_players like to continue y/n? ")
      if give_up == "y":
         target_players[turn-1].bankrupt = True
         return 
   # while target_players[turn-1].in_dept() == True: 
   if target_players[turn-1].in_jail == True:
      target_players[turn-1].time_jailed += 1
   ###List target_players Actions (dynamic actions) 
   has_rolled = False
   end_turn = False
   ###start turn
   while end_turn == False:
      ###jailed player events
      attempt_escape = False
      if target_players[turn-1].in_jail == True and has_rolled == False: 
         global bail
         print("\t\tSelect Jailed player action:")
         print("\t\t   0)",jailed_player_events[0])
         print("\t\t   1)",jailed_player_events[1],"$",bail) # needs if statment for being broke
         if target_players[turn-1].jail_free_card > 0: 
            print("\t\t   2)", jailed_player_events[2])
         target_event = input("\t\tchoice -> ")
         while int(target_event) < 0 or len(jailed_player_events) <= int(target_event) or int(target_event == 2) and target_players[turn-1].jail_free_card == 0:
            print("\t\tInvalid choice, try again")
            print("\t\t\nSelect Jailed Target_players action:")
            if has_rolled == False: 
               print("\t\t   0)",jailed_player_events[0])
            print("\t\t   1)",jailed_player_events[1],"$",bail) # needs if statment for being broke
            if target_players[turn-1].jail_free_card > 0: 
               print("\t\t   2)", jailed_player_events[2])
            target_event = input("\t\tchoice -> ")
         print("")
         if int(target_event) == 0:
            ###jailed_player_event returns True automatically
            attempt_escape =  jailed_player_event(target_players[turn-1],jailed_player_events[int(target_event)])
         else:
            ###jailed_player_event returns True if target_players stays in jail
            target_players[turn-1].in_jail= jailed_player_event(target_players[turn-1],jailed_player_events[int(target_event)])
      ###player events     
      print("\t\tSelect players action:")  
      if has_rolled == True: 
         print("\t\t   0) pass turn")
      else: 
         print("\t\t   0)",player_events[0])
      ###more events to come!   
      target_event = input("\t\tchoice -> ")
      while int(target_event) < 0 or len(player_events) < int(target_event):
         ###redisplay if given bad input
         print("\t\tInvalid choice, try again")
         print("\n\t\tSelect players action:")  
         if has_rolled == True: 
            print("\t\t   0) pass turn")
         else: 
            print("\t\t   0)",player_events[0])   
         target_event = input("\t\tchoice -> ")
         
      if int(target_event) == 0 and has_rolled == False:
         has_rolled = True
      elif int(target_event) == 0 and has_rolled == True:
         end_turn = True         
         
      if end_turn  == False:
         print("")
         
         if (attempt_escape == True and int(target_event) != 0) or attempt_escape == False:   
            player_event(target_players[turn-1],player_events[int(target_event)])
        
         if attempt_escape == True and int(target_event) == 0:
            print("\t\tattempt jail escape")
            target_players[turn-1].in_jail = jailed_move_attempt(target_players[turn-1])
            has_rolled = True
         elif target_players[turn-1].rolled_doubles(die[0],die[1]) == True and target_players[turn-1].doubles_rolled == 2 and player_events[int(target_event)] == "roll":
            print("\t\tplayer",turn,"\"doubles rolled\" = ",target_players[turn-1].doubles_rolled+1)
            target_players[turn-1].go_to_jail()
            print("")
            target_players[turn-1].doubles_rolled += 1
            turn += 1
            end_round_check(target_players)
            return
   ###end of turn
   if(target_players[turn-1].rolled_doubles(die[0],die[1]) == False):
      turn += 1
        
   else:
      target_players[turn-1].doubles_rolled += 1
      print("\n\t\tPlayer",turn,"goes again, \"doubles rolled\" = ",target_players[turn-1].doubles_rolled)
   
   if turn > len(target_players): # reset turns, start next round
      ###(not part of actual code)      
      # payment = target_players[turn-2].pay_money(300)
      # target_players[0].recieve_money(payment)
      # payment = 0
      ###(end not part of actual code)
      end_round_check(target_players)   
   else:
      print("")
#end take_turn
   
#--Main Executable--
###Menue
while starting_player_count < 2 or starting_player_count > 6: # initial starting players
   initialPlayers = input("Enter number of players(2-6): ")
   starting_player_count = int(initialPlayers) 

for i in range(0,starting_player_count): # initialize dynamic players list
   all_players.append(players(starting_total, i+1))
   
###Start Game
end_game = bool(False)
print("\nRound ",round,"\n")
while end_game == False: # Taking turn
   take_turn(all_players)
   if all_players[turn-1].bankrupt == True: 
      ###remove player
      print("\t\tplayer",turn,"is bankrupt and is now out of the game.")
      all_players.pop(turn-1)
      print("\n\tcurrently",len(all_players),"player(s) remaining")
      turn += 1
      end_round_check(all_players)
      if len(all_players) == 1:
         ###End Game    
         end_game = True
         print("\tPlayer", all_players[0].player_number(),"wins!\n")
         print("Game Over\n")


