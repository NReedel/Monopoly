# monopoly.py

###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   main executable for monopoly.Contains menue events, starts and 
#             ends game after removing all but one player. Execute via app.py
#             using flask.
###

# Imports
from . import game
from . import players
from . import events

class Monopoly:

   #--Method Implementation--
   # run() : bool
   def run(self):
      ###Data
      start_game = bool(False) 
      end_game = bool(False)
      exit_menu = bool(False)
      initial_players = int(2)
      monopoly_game = game.Game()
      main_menu = events.MainMenuEvents()  

      ####Main Menu Events
      while start_game == False:
         choice = main_menu.display_event_options(initial_players)
         start_game, initial_players, exit_menu = main_menu.event(main_menu.events[int(choice)], start_game, initial_players, exit_menu)
         if exit_menu == True:
            del monopoly_game 
            print("\nExiting...\n")
            return False

      ###End Main Menu Events
      print("\nStarting Game... ")
      monopoly_game.all_players.clear()   
      for i in range(1,initial_players+1): # initialize dynamic players list
         player = players.Players(monopoly_game.starting_total, str(i))
         # player.location_name = str(monopoly_game.board.tile[0].tile_name)
         monopoly_game.all_players.append(player)
         starting_pos = monopoly_game.all_players[i-1].current_location()
         # print("\tinitializing player",i)
         del player
      # monopoly_game.transfer_all()  

      ###Start Game
      print("\nRound ",monopoly_game.round,"\n")
      while end_game == False: # Taking turn
         monopoly_game.take_turn(monopoly_game.all_players)
         if monopoly_game.all_players[monopoly_game.turn-1].bankrupt == True: 
            ###Remove Player
            if monopoly_game.all_players[monopoly_game.turn-1].in_debt():
               print("\n\t\tplayer",monopoly_game.all_players[monopoly_game.turn-1].id,"is bankrupt.")
            print("\t\tplayer",monopoly_game.all_players[monopoly_game.turn-1].id," is now out of the game.")
            monopoly_game.all_players[monopoly_game.turn-1].deeds.clear()
            print("\t\tplayer",monopoly_game.turn,"is bankrupt.")
            print("\t\tplayer",monopoly_game.turn," is now out of the game.")
            monopoly_game.all_players.pop(monopoly_game.turn-1)
            print("\n\tCurrently",len(monopoly_game.all_players),"player(s) remaining\n")
            monopoly_game.end_round_check(monopoly_game.all_players)
            
            if len(monopoly_game.all_players) == 1:
               ###End Game    
               end_game = True
               print("\tPlayer", monopoly_game.all_players[0].id,"wins!\n")
               monopoly_game.all_players[0].deeds.clear()
               print("Game Over\n")
               
      del monopoly_game
      input("\tpress enter to continue")  
      return True 

   #--Main Executable--
   # running = True
   # while running == True:
   #    running = run()