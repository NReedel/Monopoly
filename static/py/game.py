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
# monopoly_characters = ("cannon", "thimble", "top hat", "iron", "battleship", "boot", "race car","purse")
player_events = ("roll","build","sell","mortgage","redeem","menue")
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
def roll(pair):
   pair[0] = random.randint(1,6)
   pair[1] = random.randint(1,6)
   
# move(player : Player) : void
def move(player): 
   global die 
   die = [0,0]
   roll(die) # roll
   print("\t\tp",turn,"rolled = ",die[0],die[1])
   next_location = player[turn-1].current_location()
   next_location  += (die[0]+die[1])
   
   if next_location >= 40:
      next_location = next_location % 40
      
   player[turn-1].move_location(next_location) # move
   print("\t\tplayer",turn,"location now = ",player[turn-1].current_location())
   print("")
   
# player_event(player : Player, event : string) : void
def player_event(player,event=""):
   if event == "roll":
      move(player)
   # if event ==  "roll":
   # if event == "build":
   # if event == "sell":
   # if event == "mortgage":
   # if event == "redeem":
   # if event == "menue":
   
      
# set_starting_players() : int

# is_in_jail(in_jail : bool) : void

# is_bankrupt(bankrupt : bool) : void

# event(player : Player) : void

# obj_interaction(id_1 : object, EVENT : string, id_2 : object) : void

# obj_interaction(id_1 : object, EVENT : string, id_2 : list <object>) : void

# take_turn(player : Player, turn : int
def take_turn(player):
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
   
   ###List Player Assets (static stats)
   print("\t\tmoney = $",player[turn-1].current_money())
   print("\t\tlocation = ",player[turn-1].current_location())
   print("\t\tin jail = ",player[turn-1].in_jail)
   print("\t\t----------------------------------")
   ###List Player Actions (dynamic actions)
   has_rolled = False
   end_turn = False
   
   while end_turn == False:
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
         player_event(player,player_events[int(target_event)])
   
   if(player[turn-1].rolled_doubles(die[0],die[1]) == False):
      turn = turn + 1
   elif player[turn-1].rolled_doubles(die[0],die[1]) == True and player[turn-1].doubles_rolled == 3:
      doubles_rolled = 0
      print("\t\tPlayer",turn,"goes to jail, since \"doubles rolled\" = ",player[turn-1].doubles_rolled)
      # send_to_jail(player)
      player[turn-1].in_jail = True
      player[turn-1].doubles_rolled = 0
      turn = turn + 1
   else:
      player[turn-1].doubles_rolled += 1
      print("\t\tPlayer",turn,"goes again, \"doubles rolled\" = ",player[turn-1].doubles_rolled)
      
   player_count = len(player)
   
   if turn > player_count: # reset turns, start next round
      ###(not part of actual code)
      payment = player[turn-2].pay_money(300)
      player[0].recieve_money(payment)
      payment = 0
      ###(end not part of actual code)
      turn = turn % player_count
      round += 1
      print("")
      print("Round ",round)
      
   print("")
   
#--Main Executable--

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
      if len(all_players) == 1:
         end_game = True
         print("\tplayer", all_players[0].player_number(),"wins!\n")
print("Game Over\n")


