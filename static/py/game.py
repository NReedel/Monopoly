# game.py
###
# *Name:      Alicyn, Chris, Nate
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Monopoly game, parent  class or main executable that links 
#             all objects. Contains all game elements
###


#--Imports--
from players import *
import random

#--Global Data--
starting_total = int(500)
bail = int(50) #new
# monopoly_characters = ("cannon", "thimble", "top hat", "iron", "battleship", "boot", "race car","purse")
player_events = ("roll","build","sell","mortgage","redeem","menue")
jailed_player_events = ("roll doubles","pay jail fee","jail free card") #new
payment = int(0) # Note: used to store return value from pay_moneyy() and used as arg in recieve_money()
die = [0,0]
turn = int(1)
round = int(1)
starting_player_count = int(0)
all_players = []
# the_bank = bank()
# the_properties = properties()

#--Method Implementation--
# roll(pair : list <int>) : void 
def roll(pair): # might add doubles_rolled counter
   global round 
   ###not part of actual code
   if round == 1: 
      pair[0] = random.randint(1,1)
      pair[1] = random.randint(1,1)
   else:
    ###end not part of actual code  
      pair[0] = random.randint(1,6)
      pair[1] = random.randint(1,6)   
# move(player : players) : void
def move(player): #new, changed arg to single datatype
   global die
   global turn 
   die = [0,0]
   roll(die) # roll
   print("\t\tp",turn,"rolled = ",die[0],die[1])
   next_location = player.current_location()
   next_location  += (die[0]+die[1])
   
   if next_location >= 40:
      player.recieve_amount(200)
      next_location = next_location % 40

   player.move_location(next_location) # move
   print("")

# jailed_move_attempt(player : players) : void
def jailed_move_attempt(player): #new
   global die
   global turn 
   die = [int(0),int(0)]
   roll(die) # roll
   print("\t\tp",turn,"rolled = ",die[0],die[1])
   if player.rolled_doubles(die[0],die[1]) == True or player.time_jailed == 3:
      if player.time_jailed == 3 and player.rolled_doubles(die[0],die[1]) == False:
         player.time_jailed == 0
         global bail
         player.pay_money(bail)    
      print("\t\tp",turn,"escaped jail")
      next_location = player.current_location()
      next_location  += (die[0]+die[1])
      die[0]=0
      die[1] =1
      if next_location >= 40:
         player.recieve_amount(200)
         next_location = next_location % 40
      player.move_location(next_location) # move
      print("")  
      return False # in_jail = False
   else:
      print("\t\tplayer",player.player_number(),"remains in jail")
      print("")  
      return True
   
   
# player_event(player : players, event : string) : void
def player_event(player,event=""):
   ###standard player event
   if event == "roll":
      move(player)
   # if event == "build":
   # if event == "sell":
   # if event == "mortgage":
   # if event == "redeem":
   # if event == "menue":
   
# jailed_player_event(player : Players, event : string) : bool
def jailed_player_event(player,event=""): #new
   ###jailed palyer event
   if event == "roll doubles":
      #global player_events
      return True
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
      return False
   return True

# player_assets( target_player : player ) : void
def player_assets(player): #new
   ###List Player Assets (static stats)
   print("\t\tmoney = $",player.current_money())
   print("\t\tlocation = ",player.current_location())
   print("\t\tdoubles rolled = ",player.doubles_rolled )
   # if player.in_jail == True:
   print("\t\tin jail = ",player.in_jail)
   print("\t\ttime jailed =",player.time_jailed)
   # if player.jail_free_card > 0:
   print("\t\tjail free cards = ",player.jail_free_card)
   # print("\t\t")
   print("\t\t----------------------------------") 

# player_actions( target_player : player ) : void

# is_bankrupt(bankrupt : bool) : void

# event(player : Player) : void

# obj_interaction(id_1 : object, EVENT : string, id_2 : object) : void

# obj_interaction(id_1 : object, EVENT : string, id_2 : list <object>) : void

# take_turn(player : players, turn : int) : void
def take_turn(player): ### ! make player players
   global turn #like pass by refrence, access global
   global round 
   
   print("\tPlayer",turn, ":") #players turn
   
   if player[turn-1].in_debt() == True: # if player is in dept
      print("\t\tplayer",turn,"is in dept at $",player[turn-1].current_money())
      give_up = "y"
      # give_up = input("\tWould the player like to continue y/n? ")
      if give_up == "y":
         player[turn-1].declare_bankruptcy()
         return 
      # while player[turn-1].in_dept() == True: 
   if player[turn-1].in_jail == True:
      player[turn-1].time_jailed += 1
   ###List Player Assets 
   player_assets(player[turn-1]) #new

   ###List Player Actions (dynamic actions) 
   has_rolled = False
   end_turn = False
   while end_turn == False:
      ###new
      ###jailed player events
      attempt_escape = False
      if player[turn-1].in_jail == True and has_rolled == False: 
         global bail
         print("\t\tSelect Jailed Player action:")
         if has_rolled == False: 
            print("\t\t   0)",jailed_player_events[0])
         print("\t\t   1)",jailed_player_events[1],"$",bail) # needs if statment for being broke
         if player[turn-1].jail_free_card > 0: 
            print("\t\t   2)", jailed_player_events[2])
         target_event = input("\t\tchoice -> ")
         while (has_rolled == True and int(target_event) == 0) or (player[turn-1].jail_free_card == 0 and int(target_event) == 2):
            print("invalid choice, try again")
            print("\t\tSelect Jailed Player action:")
            if has_rolled == False: 
               print("\t\t   0)",jailed_player_events[0])
            print("\t\t   1)",jailed_player_events[1],"$",bail) # needs if statment for being broke
            if player[turn-1].jail_free_card > 0: 
               print("\t\t   2)", jailed_player_events[2])
            target_event = input("\t\tchoice -> ")
         print("")
         ###jailed_player_event returns True if player stays in jail
         if int(target_event) == 0:
            attempt_escape =  jailed_player_event(player[turn-1],jailed_player_events[int(target_event)])
         else:
            player[turn-1].in_jail= jailed_player_event(player[turn-1],jailed_player_events[int(target_event)])
      ###end new
      ###player event    
      print("\t\tSelect Player action:")  
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
         #new if statment   
            player_event(player[turn-1],player_events[int(target_event)])
         ##new below
         if attempt_escape == True and int(target_event) == 0:
            print("\t\tattempt jail escape")
            player[turn-1].in_jail = jailed_move_attempt(player[turn-1])
            has_rolled = True
         ###new below
         elif player[turn-1].rolled_doubles(die[0],die[1]) == True and player[turn-1].doubles_rolled == 2 and player_events[int(target_event)] == "roll":
               # doubles_rolled = 0
            print("\t\tPlayer",turn,"\"doubles rolled\" = ",player[turn-1].doubles_rolled+1)
               # send_to_jail(player)
            player[turn-1].go_to_jail()
            print("")
               # player[turn-1].in_jail = True
               #player[turn-1].doubles_rolled = 0
            player[turn-1].doubles_rolled += 1
            ###start new
            turn += 1
            if turn > len(player): # reset turns, start next round
               turn = turn % len(player) 
               round += 1
               print("")
               print("Round ",round)
               for i in range(0,len(player)): #new ,clears
                  player[i].doubles_rolled = 0
            return
            ###end new   
         
   if(player[turn-1].rolled_doubles(die[0],die[1]) == False):
      turn += 1
        
   else:
      player[turn-1].doubles_rolled += 1
      print("\n\t\tPlayer",turn,"goes again, \"doubles rolled\" = ",player[turn-1].doubles_rolled)
      
   player_count = len(player)
   
   if turn > player_count: # reset turns, start next round
      ###(not part of actual code)
      payment = player[turn-2].pay_money(300)
      player[0].recieve_money(payment)
      payment = 0
      ###(end not part of actual code)
      turn = turn % player_count
      for i in range(0,len(all_players)): #new ,clears 
         player[i].doubles_rolled = 0      
      round += 1
      print("")
      print("Round ",round)
      
   print("")
   
#--Main Executable--
###Menue
while starting_player_count < 2 or starting_player_count > 6: # initial starting players
   initialPlayers = input("Enter number of players(2-6): ")
   starting_player_count = int(initialPlayers) 

for i in range(0,starting_player_count): # initialize dynamic players list
   all_players.append(players(starting_total, i+1))
   
###Start Game
end_game = bool(False)
print("")
print("Round ",round)
print("")

while end_game == False: # Taking turn
   take_turn(all_players)
   if all_players[turn-1].is_bankrupt() == True:
      print("\t\tplayer",turn,"is bankrupt and is now out of the game.")
      all_players.pop(turn-1)
      print("\n\tcurrently",len(all_players),"player(s) remaining")
      turn += 1
      if turn > len(all_players): # reset turns, start next round
         turn = turn % len(all_players) + 1
         round += 1
         print("")
         print("Round ",round)
         for i in range(0,len(all_players)): #new ,clears
            all_players[i].doubles_rolled = 0
      if len(all_players) == 1:
         end_game = True
         print("\tPlayer", all_players[0].player_number(),"wins!\n")
###End Game        
print("Game Over\n")


