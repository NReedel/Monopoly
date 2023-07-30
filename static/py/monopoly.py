# monopoly.py

###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   main executable for monopoly.Contains menue events, starts and 
#             ends game after removing all but one player.
###

# Imports
from game import *
from players import *
from events import MainMenuEvents

class Monopoly:

   #--Method Implementation--
   # run() : bool
   def run():
      ###Data
      start_game = bool(False) # new
      end_game = bool(False)
      exit_menu = bool(False)
      initial_players = int(2)
      monopoly_game = Game()
      
      main_menu = MainMenuEvents()  # new
      #Main Menu Events
      while start_game == False:
         choice = main_menu.display_event_options(initial_players)
         # main_event.event() uses unpacking to modify data
         start_game, initial_players, exit_menu = main_menu.event(main_menu.events[int(choice)], start_game, initial_players, exit_menu)
         if exit_menu == True:
            return False
      ###End Main Menu Events
      print("\nStarting Game... ")
      monopoly_game.all_players.clear()   
   
      for i in range(1,initial_players+1): # initialize dynamic players list
         monopoly_game.all_players.append(Players(monopoly_game.starting_total, i))
         # print("\tInitialize Player",i)
      
      ###Start Game
      print("\nRound ",monopoly_game.round,"\n")
      
      while end_game == False: # Taking turn
         monopoly_game.take_turn(monopoly_game.all_players)
         if monopoly_game.all_players[monopoly_game.turn-1].bankrupt == True: 
            ###Remove Player
            if monopoly_game.all_players[monopoly_game.turn-1].in_debt():
               print("\n\t\tplayer",monopoly_game.all_players[monopoly_game.turn-1].player_number(),"is bankrupt.")
            print("\t\tplayer",monopoly_game.all_players[monopoly_game.turn-1].player_number()," is now out of the game.")
            monopoly_game.all_players.pop(monopoly_game.turn-1)
            print("\n\tCurrently",len(monopoly_game.all_players),"player(s) remaining\n")
            # monopoly_game.turn += 1
            monopoly_game.end_round_check(monopoly_game.all_players)
            if len(monopoly_game.all_players) == 1:
               ###End Game    
               end_game = True
               print("\tPlayer", monopoly_game.all_players[0].player_number(),"wins!\n")
               print("Game Over\n") 
               
      return True 

   #--Main Executable--
   running = True
   while running == True:
      running = run()
      if running == True:  
         input("\tpress enter to continue")
      else:
         print("\nExiting...\n")


   
   


