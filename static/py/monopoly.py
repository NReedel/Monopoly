###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   main executable for monopoly.Contains menue events, starts and 
#             ends game after removing all but one player.
###

# Imports
from asyncio import run
from game import *
from players import *

class Monopoly:
   
   #--Method Implementation--
   def run():
      ###Data
      monopoly_game = Game()
      end_game = bool(False)
      ###Menue
      while monopoly_game.starting_player_count < 2 or monopoly_game.starting_player_count > 6: # initial starting players
         initialPlayers = input("Enter number of players(2-6): ")
         monopoly_game.starting_player_count = int(initialPlayers) 
         
      for i in range(0,monopoly_game.starting_player_count): # initialize dynamic players list
         monopoly_game.all_players.append(Players(monopoly_game.starting_total, i+1))
      ###Start Game
      print("\nRound ",monopoly_game.round,"\n")
      while end_game == False: # Taking turn
         monopoly_game.take_turn(monopoly_game.all_players)
         if monopoly_game.all_players[monopoly_game.turn-1].bankrupt == True: 
            ###Remove Player
            print("\t\tplayer",monopoly_game.turn,"is bankrupt and is now out of the game.")
            monopoly_game.all_players.pop(monopoly_game.turn-1)
            print("\n\tcurrently",len(monopoly_game.all_players),"player(s) remaining")
            monopoly_game.turn += 1
            monopoly_game.end_round_check(monopoly_game.all_players)
            if len(monopoly_game.all_players) == 1:
               ###End Game    
               end_game = True
               print("\tPlayer", monopoly_game.all_players[0].player_number(),"wins!\n")
               print("Game Over\n")   
   
   # --Constructor--
   # def __init__(self):
   #    self.run()
   
   #--Main Executable--
   run()


