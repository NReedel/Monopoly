# events.py

###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Handle specialised user event and display event options.
#             Covers all user based input
###

###############################################################
# Events Hierarchy 🔳
###############################################################
'''
Events
├── InitialPlayerEvents # incomplete
├── PlayerEvents
├── JailedPlayerEvents
├── MenuPlayerEvents   
├── BankruptPlayerEvents  # incomplete
├── AvailablePropertyEvents  
├── AuctionPropertyEvents 
├── CardEvents # incomplete
├── MainMenuEvents
├── BuildBuildingEvents 
├── SellBuildingEvents  
├── MortgagePropertyEvents
├── RedeemPropertyEvents         
├── TradeEvents 

'''
###############################################################
# current_player = self.arg[0].all_players[self.arg[0].turn-1] # alt

# Imports
import copy

class Events:
   #--Global Data--
   argc = int(0)
   arg = []
   events = []
   
   #--Constuctor--
   def __init__(self,*args):

      self.argc = len(args)
      # self.arg = 0 # argument count, check for built in one
      self.argc = len(args) 
      
      if len(args) > 0:
         for i in range(len(args)):
            self.arg.append(args[i]) 
                 
   #--Method Implementation--
   def display_event_options(self): 
      return 
   def event(self): # event() : void
      return
   def display_event_options(self): 
      return 
   def event(self): # event() : void
      return
   def update(self,*argument):
      self.arg = argument
      
class PlayerEvents(Events): # partial completion 
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)
   
   #--Argumets--
   # arg[0] = self from game 

   #--Global Data--
   events = ["roll","build","sell","mortgage","redeem","trade","menu","status"]
    
   #--Method Implementations--
   # display_event_options(self, has_rolled) : string
   def display_event_options(self, has_rolled):
      
      if self.arg[0].all_players[self.arg[0].turn-1].bankrupt == False: 
         print("\t\tSelect players action:")  
      
         if has_rolled == True: 
            print("\t\t   0) pass turn")
         else: 
            print("\t\t   0)",self.events[0])
            
         for i in range(1,len(self.events)):
            num = str(i) + ")"
            print("\t\t  ",num,self.events[i])
         target_event = input("\n\t\tchoice -> ")      
         return target_event
      
      else: 
         return 0
   
   # event(self player : Players, event : string) : void
   def event(self,player,event = ""):
      current_player = self.arg[0].all_players[self.arg[0].turn-1]
      
      if event == "roll":
         self.arg[0].game_dice.roll()
         print("\t\tplayer",player.id,"roll =",self.arg[0].game_dice.print_roll()) # add roll total
         # needs if condition for alt moves
         self.arg[0].move(player, self.arg[0].game_dice.total_rolled()) 
         
      if event == "build":
         choice = 0
         while choice != -1:
            build = BuildBuildingEvents(self.arg[0])
            choice = build.display_event_options(player)
            
            if choice != -1 :
               build.event(player, choice)
               build.update(self.arg[0])
         
      if event == "sell":
         choice = 0
         while choice != -1:
            sell = SellBuildingEvents(self.arg[0])
            choice = sell.display_event_options(player)
            
            if choice != -1 :
               sell.event(player, choice)
               sell.update(self.arg[0])        
      
      if event == "mortgage": 
         choice = 0
         while choice != -1:
            mortgage = MortgagePropertyEvents(self.arg[0])
            choice = mortgage.display_event_options(player)
            print()
            
            if choice != -1 :
               mortgage.event(choice)
               mortgage.update(self.arg[0])
               
         # mortgage.update(self.arg[0])

      if event == "redeem":
         choice = 0
         while choice != -1:
            redeem = RedeemPropertyEvents(self.arg[0])
            choice = redeem.display_event_options(player) 
            print()

            if choice != -1 :
               redeem.event(choice)
               redeem.update(self.arg[0])
               
      if event == "trade":
         finished = 0
         trade = TradeEvents(self.arg[0])
         trade.display_event_options() 
         print()    

      if event == "menu":
         menu = MenuPlayerEvents()
         choice = menu.display_event_options()
         
         while int(choice) < 0 or int(choice) >= len(menu.events):
            print("\t\tInvalid choice, try again\n")
            choice = menu.display_event_options()
            
         menu.event(player,menu.events[int(choice)])
         if player.bankrupt == True:
            return
         
      if event == "status":
         print("\t\t-----------------------------")    
         player.player_status(self.arg[0].board.tile)
         
class JailedPlayerEvents(Events): 
  
   #--Global Data--
   events = ["roll doubles","pay jail fee","jail free card"]
   
   #--Method Implementations--
   # display_event_options(self, player : Players) : string
   def display_event_options(self,player):
      print("\t\tSelect Jailed player action:")
      for i in range(0,len(self.events)):
         num = str(i)+")"
         if i == 0:
            print("\t\t  ",num,self.events[i])
         elif i == 1:
            print("\t\t  ",num,self.events[i],"$",self.arg[0].bail)
         elif i == 2 and player.jail_free_card > 0: 
            print("\t\t  ",num,self.events[i])
      target_event = input("\n\t\tchoice -> ")      
      return target_event
   
   # event(player : Players, event : string) : bool
   def event(self,player,event=""): 
      # player = self.arg[0].all_players[self.arg[0].turn-1]
      if event == "roll doubles":
         return True # attempt_escape == True
      
      if event == "pay jail fee":   
         player.pay_money(self.arg[0].bail)
         player.time_jailed = 0
         print("\t\tPlayer",player.id,"is now out of jail\n")
         return False #player.in_jail == False
      
      if event == "jail free card":
         player.jail_free_card -= 1
         player.time_jailed = 0
         print("\t\tPlayer",player.id,"is now out of jail\n")
         return False #player.in_jail == False
      
      return True

class MenuPlayerEvents(Events):
   
   
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)   

   #--Global Data--
   events = ["leave game","return to game","rules"]
    
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self): 
      print("\t\tSelect players action:")
      for i in range(0,len(self.events)):
         num = str(i)+")"
         print("\t\t  ",num,self.events[i])
      target_event = input("\n\t\tchoice -> ")       
      return target_event
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""): 
      if event == "leave game":
         #Note: doesn't consider AI players
         player.bankrupt = True
         print()
         return
      if event == "return to game":
         print()
         return
      if event == "rules":
         print() 
         # Load file here, use your own link 💬
         rules_file_path = '../txt/monopoly_rules.txt' 
         with open(rules_file_path, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()
         # Print the contents of the file
         print(file_contents)
         blank = input("\npress enter to exit\n")
         return
            
class BankruptPlayerEvents(Events): #incomplete
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)     
   
   #--Global Data--
   events = ["give up","sell","mortgage","trade","menu"]
   
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self):
      print("\t\tSelect in dept players action:")  
      for i in range(0,len(self.events)):
         num = str(i) + ")"
         print("\t\t  ",num,self.events[i])      
      target_event = input("\n\t\tchoice -> ")      
      return target_event
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""):
      if event == "give up":
         player.bankrupt = True
      '''      
      if event == "sell":
      if event == "mortgage":
      if event == "trade"
      if event == "menu"
      ''' 
    
class AvailablePropertyEvents(Events): # near complete
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)
            
   #--Argumets--
   # arg[0] = self from game, used for bank and all_players
   
   #--Global Data--
   events = ["purchase","auction"]
    
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self,property_cost, player_money):
      print("\t\tSelect players action:")
      for i in range(0,len(self.events)):
         num = str(i)+")"
         if i == 0 and player_money >= property_cost:
            print("\t\t  ",num,self.events[i],"for",str("$")+str(property_cost))
         elif i == 1: 
            print("\t\t  ",num,self.events[i])
      target_event = input("\n\t\tchoice -> ")
      print()       
      return str(target_event)
      
   # event(self, event : string) : void
   def event(self, event):
      bank = self.arg[0].bank
      current_tile = self.arg[0].board.tile
      all_players = self.arg[0].all_players
      current_player = (all_players[self.arg[0].turn-1])
      current_tile = self.arg[0].board.tile[current_player.current_location()]
      # player_deeds.deep_copy(current_player.deeds)
      # bank_deeds = bank.deeds 
      if event == "purchase":
         ### buy deed from bank
         self.arg[0].transfer_payment(current_player, bank, current_tile.property_cost)
         self.arg[0].transfer_deed(bank, current_player, current_player.current_location())
      if event == "auction": 
         auction = AuctionPropertyEvents(self.arg[0])
         auction_deed = self.arg[0].bank.deeds[current_player.current_location()] # copys current locations deed
         self.arg[0].bank.deeds.pop(current_player.current_location()) #remove deed
         deed_reciever, highest_bid = auction.display_event_options(auction_deed,self.arg[0].all_players, self.arg[0].turn)
         self.arg[0].transfer_payment(all_players[deed_reciever], bank, highest_bid)
         self.arg[0].transfer_deed(bank,all_players[deed_reciever], current_player.current_location())
         print("\tPlayer",self.arg[0].turn,":")
         del auction
   
class AuctionPropertyEvents(Events): 
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)  
         
   #--Global Data--
   events = ["bid","forfeit"]
    
   #--Method Implementations--
   # display_event_options(self,auctioned_deed : Deed, all_players : Players, starting_bidder : int) : string 
   def display_event_options(self,auctioned_deed, all_players, starting_bidder): #incomplete
      current_bid = 0
      highest_bidder = 0
      current_bidder = starting_bidder-1
      biding_players = copy.deepcopy(all_players) 
      
      while len(biding_players) > 1:
         print("\t\tbidder: player"+biding_players[current_bidder].id+"["+str(biding_players[current_bidder].current_money())+"]")
         print("\t\tcurrent bid: ",current_bid)
         for i in range(len(self.events)):
            num = str(i) + ")"
            if i == 0 and current_bid >= biding_players[current_bidder].current_money():
               print("\n\t\tPlayer",biding_players[current_bidder].id)
               pass 
            else:
               print("\t\t  ",num,self.events[i])
         ### player doesn't have enough money and forfeits
         if current_bid >= biding_players[current_bidder].current_money():
            target_event = 1
         ### player chooses option
         else:
            valid = False
            ### input, validate player input
            while(valid != True):
               target_event = int(input("\n\t\tchoice -> "))
               valid = self.is_valid_number(target_event, len(self.events))
               if valid == False:
                  print("\t\tInvalid choice, try again")
         choice = self.event(biding_players[current_bidder],self.events[target_event], current_bid) 
         
         if choice == 0: # remove player from bid list
            print("\t\tplayer "+biding_players[current_bidder].id+" has forfeited")
            biding_players.pop(current_bidder)
            # current_bidder =  int(biding_players.id)-1
            if len(biding_players) == 1: # highest bidder wins
               print("\n\t\tplayer",biding_players[0].id,"wins!")
               return (int(biding_players[0].id)-1), current_bid
            
               
         elif choice > 0: # place bid, set highest bidder
            current_bid = choice
            highest_bidder = int(biding_players[current_bidder].id)-1
            current_bidder = (current_bidder + 1) % len(biding_players) # next bidder
            
         elif choice == -1:
            print("\t\tthe value you entered is too low")
         
   # event(self, players : Players, event : int) : void
   def event(self, player, event, highest_bid):
      if event == "forfeit":
         return 0
      elif event == "bid":
         bid = int(input("\n\t\tenter bid > "+str(highest_bid)+" -> "))
         if bid > highest_bid:
            print("\n\t\tplayer",player.id,"has bidded at",str(bid),"\n")
            return bid
         else:
            # invalid
            return -1
         
   # is_valid_number(self, str : input_str, event_size : int)
   def is_valid_number(self,input_str,events_size):
      try:
         number = int(input_str)
         return 0 <= number < events_size
      except ValueError:
         return False

# !!! Cards have no user-based input, 
#       but there may be some house rules otherwise 
#       so this will be left here for now
# !!!   
# class CardEvents(Events): #incomplete
#    #--Constructor--
#    def __init__(self, *args):
#       super().__init__(*args)  
#        
#    #--Global Data--
#    events = ["take a chance"]
#   
#    #--Method Implementations--
#    # display_event_options(self) : string
#    def display_event_options(self):
#       return
#     
#    # event(self, player : Players, event : string) : void
#    def event(self,player,event = ""):
#       return

class MainMenuEvents(Events): # near complete
   #--Constructor--
   def __init__(self):
      super().__init__()  
      
   #--Global Data--
   events = ["start game","players","rules","settings","exit"] 
   
   #--Method Implementations--
   # display_event_options(self, initial_players : int) : string
   def display_event_options(self,initial_players): 
      print("\nMonopoly Menu :")
      for i in range(len(self.events)):
         num = str(i)+")"
         if i != 1:
            print("  ",num,self.events[i])
         else:
            print("  ",num,self.events[i],"=", "[" + str(initial_players) + "]") 
      target_event = input("\nchoice -> ")
      return target_event
   
   # event(self, event : string, start_game : bool, initial_players : int, exit_menu : bool)) : tuple<T>
   def event(self, event, start_game, initial_players, exit_menu):
      if event == "start game": # "start_game"
         #start_game = main_menu.event(main_menu.events[int(choice)])
         start_game = True
      if event == "players": # "number of players"
         #initial_players = main_menu.event(main_menu.events[int(choice)])
         initial_players = 0     
            
         while initial_players < 2 or initial_players > 6:
            initial_players = int(input("\nEnter number of players(2-6): "))
            if initial_players < 2 or initial_players > 6:
               print("Invalid quantiy, try again")
               
      if event == "rules": # "rules"
         # Load file here, use your own link 💬
         print() 
         rules_file_path = '../txt/monopoly_rules.txt' 
         with open(rules_file_path, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()
            # Print the contents of the file
            print(file_contents)
         blank = input("\npress enter to exit\n")
         
      if event == "settings": # "settings" # for house rules, might be front-end 
         pass
      
      if event == "exit": # "exit"
         exit_menu = True

      return start_game, initial_players, exit_menu # unpack tuple
   ''' 
      if event == "start game":
      if event == "number of players"
      if event == "rules": 
      if event == "settings":
      if event == "exit":
   '''
      
class BuildBuildingEvents(Events): 
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)  
   
   # display_event_options(self,player : players) : int
   def display_event_options(self,player): 
      board = self.arg[0].board
      # buildable_properties
      self.events = copy.deepcopy(player.buildable_property_list(board.tile))
      can_afford = False
      while can_afford == False:
         target_event = "-2" 
         while int(target_event) >= len(self.events) or int(target_event) < (-1):
            print("\t\tSelect property to build:")
            print("\t\t ",str(-1)+")","cancel building")
            for i in range(0,len(self.events)):
               h = "h ="
               development = board.tile[self.events[i].index].houses 
               if(board.tile[self.events[i].index].hotels > 0):
                  h = "H ="
                  development = board.tile[self.events[i].index].hotels
               num = str(i) + ") " # + str(self.events[i].index)
               print("\t\t  ",num,self.events[i].name,h,development)          
            target_event = input("\n\t\tchoice -> ")
            if int(target_event) >= len(self.events) or int(target_event) < (-1):
               print("\t\tinvalid choice, try again\n") 
         print()
         if int(target_event) == -1:
            return -1
         target_deed = self.events[int(target_event)]
         if board.tile[self.events[int(target_event)].index].houses < 4 and player.current_money() >= target_deed.house_cost:
            payment = target_deed.house_cost
            can_afford = True
         elif board.tile[self.events[int(target_event)].index].houses == 4  and player.current_money() >= target_deed.hotel_cost:
            payment = target_deed.hotel_cost
            can_afford = True
         else:
            print("\t\tcan't afford the selection\n") 

      bank = self.arg[0].bank
      # print("\n\t\t"+self.events[int(target_event)].name,"building =",self.events[int(target_event)].name)      
      self.arg[0].transfer_payment(player,bank,payment) 
      return self.events[int(target_event)].index
   
   # event(self,event : int) : void
   def event(self,player,event):
      board = self.arg[0].board
      if board.tile[event].houses < 4 and board.tile[event].hotels != 1: 
         board.tile[event].houses += 1
         player.total_houses += 1
         print("\t\t"+board.tile[event].tile_name,"h =",board.tile[event].houses,"\n")  
      else:
         board.tile[event].houses = 0
         board.tile[event].hotels += 1
         player.total_hotels += 1
         print("\t\t"+board.tile[event].tile_name,"H =",board.tile[event].hotels,"\n")  

class SellBuildingEvents(Events): 
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)  

   # display_event_options(self,player : players) : int
   def display_event_options(self,player): 
      board = self.arg[0].board
      # buildable_properties
      self.events = copy.deepcopy(player.sellable_property_list(board.tile))
      target_event = "-2" 
      while int(target_event) >= len(self.events) or int(target_event) < (-1):            
         print("\t\tSelect property to sell:")
         print("\t\t ",str(-1)+")","cancel selling")
         for i in range(0,len(self.events)):
            h = "h ="
            development = board.tile[self.events[i].index].houses 
            
            if(board.tile[self.events[i].index].hotels > 0):
               h = "H ="
               development = board.tile[self.events[i].index].hotels
               
            num = str(i) + ") " # + str(self.events[i].index)
            print("\t\t  ",num,self.events[i].name,h,development)          
         target_event = input("\n\t\tchoice -> ")
         if int(target_event) >= len(self.events) or int(target_event) < (-1):
            print("\t\tinvalid choice, try again\n")
      print()
      if int(target_event) == -1:
         return -1
      target_deed = self.events[int(target_event)]
      if board.tile[self.events[int(target_event)].index].hotels == 1:
         payment = int(target_deed.hotel_cost / 2)
      else:
         payment = int(target_deed.house_cost / 2)        
      bank = self.arg[0].bank  
      self.arg[0].transfer_payment(bank,player,payment) 
      return self.events[int(target_event)].index
   
   # event(self, event : int) : void
   def event(self,player, event): 
      board = self.arg[0].board
      if board.tile[event].hotels == 1:
         board.tile[event].hotels = 0
         player.total_hotels -= 1 
         board.tile[event].houses = 4
         player.total_houses += 4 
      else:
         board.tile[event].houses -= 1
         player.total_houses -= 1 
         #print("\t\t"+board.tile[event].tile_name,"H =",board.tile[event].hotels,"\n") 
      print("\t\t"+board.tile[event].tile_name,"h =",board.tile[event].houses,"\n") 
       
class MortgagePropertyEvents(Events): 
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)  
      
   # display_event_options(self,player : players) : int
   def display_event_options(self,player): 
   
      board = self.arg[0].board
      # mortgageable_properties
      self.events = copy.deepcopy(player.mortgageable_property_list(board.tile))
      print("\t\tSelect property to mortgage:")
      
      print("\t\t ",str(-1)+")","cancel mortgage")
      for i in range(0,len(self.events)):
          # self.events.append(self.events[i].name) #change to player.owned_deeds.name
          num = str(i) + ")" 
          print("\t\t  ",num,self.events[i].name)          

      target_event = input("\n\t\tchoice -> ")
      if int(target_event) == -1:
         return -1
      target_deed = self.events[int(target_event)]
      payment = target_deed.mortgage_value # mortgage_value
      bank = self.arg[0].bank
      print("\n\t\t"+self.events[int(target_event)].name,"is mortgaged")      
      self.arg[0].transfer_payment(bank,player,payment)      
      return self.events[int(target_event)].index
   
   # event(self, event : int) : void
   def event(self,event): 
      board = self.arg[0].board
      board.tile[event].is_mortgaged = True

class RedeemPropertyEvents(Events): #incomplete
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)  
      
   # display_event_options(self,player : players) : int
   def display_event_options(self,player): 
      board = self.arg[0].board
      self.events = copy.deepcopy(player.unmortgageable_property_list(board.tile))
      print("\t\tSelect property to redeem:")
      print("\t\t ",str(-1)+")","cancel redemption")
      
      for i in range(0,len(self.events)):
          # self.events.append(self.events[i].name) #change to player.owned_deeds.name
          num = str(i) + ")"  
          print("\t\t  ",num,self.events[i].name)      
          
      target_event = input("\n\t\tchoice -> ")
      if int(target_event) == -1:
         return -1      
      target_deed = self.events[int(target_event)]
      payment = target_deed.unmortgage_value # unmortgage_value
      bank = self.arg[0].bank
      print("\n\t\t"+self.events[int(target_event)].name,"is unmortgaged")
      self.arg[0].transfer_payment(player,bank,payment)     
      return self.events[int(target_event)].index
   
   # event(self,event : int) : void
   def event(self,event): 
      board = self.arg[0].board
      board.tile[event].is_mortgaged = False
  
class TradeEvents(Events): #incomplete
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)  
         
 # display_event_options(self) : void
   def display_event_options(self):
      selectable_players = []
      game = self.arg[0]
      player = game.all_players[game.turn-1]
      # list_pairing = []
      # generate tradable player list  
      for i in range(0,len(game.all_players)):
         if game.all_players[i].id != player.id:
            selectable_players.append(game.all_players[i])
      # num = str(i) + ")"
      target_player = -1
      ### pick player to trade with
      while target_player < 0 or target_player >= len(selectable_players):
         print("\t\tChoose a player to trade with:")
         print("\t\t ",str(-1)+")","cancel trade offer")
         for i in range(0,len(selectable_players)):
            num = str(i) + ")"
            print("\t\t  ",num,"player",selectable_players[i].id)
         target_player = int(input("\n\t\tchoice -> "))
         if target_player == -1:
            return
      selected_player = selectable_players[target_player]
      next_step = False 
      ### offer asset properties
      offered_properties = []
      deed_choice = -1
      player_properties = copy.deepcopy(player.deeds)
      current_offer = ""
      if len(player_properties) == 0:
         next_step = True
      while next_step == False: ### select properties
         # for i in range(0, len(offered_properties)):
         if current_offer != "":
            print("\n\t\tproperties offered:", current_offer)
         print("\n\t\tSelect property:")
         print("\t\t ",str(-1)+")","finish property offer")
         for i in range(0,len(player_properties)):
            num = str(i) + ")"
            print("\t\t  ", num, player_properties[i].name)
         deed_choice = int(input("\n\t\tchoice -> "))
         ### respond to offered choice
         if deed_choice >= 0 and deed_choice < len(player_properties):
            removed_property = player_properties.pop(deed_choice)
            offered_properties.append(removed_property)
            current_offer += "\n\t\t   -"+removed_property.name
         elif int(deed_choice) == -1:
            next_step = True
            deed_choice = -1
         else: 
            print("\t\tinvalid choice, try again\n") 
      ### reset
      next_step = False
      offered_money = -1
      ### offer asset money
      while offered_money < 0 or offered_money > player.current_money():
         print("\n\t\tcurrent money:",player.current_money())
         offered_money = int(input("\t\tenter offer: $"))
         if offered_money < 0 or offered_money > player.current_money():   
            print("\t\tinvalid choice, try again\n")
      confirm_offer = -1
      ### confirm property, money offer
      while confirm_offer < 0 or confirm_offer > 1:
         print("\n\t\tyour money offer is $"+str(offered_money))
         if current_offer != "":
            print("\t\tyour property offer is", current_offer+"\n") # current_offer is not the requested list
         print("\t\tConfirm offer")
         print("\t\t  ","0) yes, continue")
         print("\t\t  ","1) no, exit trade")
         confirm_offer = int(input("\n\t\tchoice -> "))
      if confirm_offer == 1:
         return
      ### requested asset properties
      print("\n\t\trequest assets from player "+str(selected_player.id))
      desired_properties = []
      deed_choice = -1
      other_player_properties = copy.deepcopy(selected_player.deeds)
      current_request = ""
      if len(other_player_properties) == 0:
         next_step = True
      while next_step == False: ### select properties
         if current_request != "":
            print("\n\t\trequested properties:", current_request)
         print("\n\t\tSelect property:")
         print("\t\t ",str(-1)+")","finish property request")
         for i in range(0,len(other_player_properties)):
            num = str(i) + ")"
            print("\t\t  ", num, other_player_properties[i].name)
         deed_choice = int(input("\n\t\tchoice -> "))
         ### respond to offered choice
         if deed_choice >= 0 and deed_choice < len(player_properties):
            removed_property = other_player_properties.pop(deed_choice)
            desired_properties.append(removed_property)
            current_request += removed_property.name
         elif int(deed_choice) == -1:
            next_step = True
            deed_choice = -1
         else: 
            print("\t\tinvalid choice, try again\n")
      ### reset
      next_step = False
      desired_money = -1
      ### desired asset money
      while desired_money < 0 or desired_money > selected_player.current_money():
         print("\n\t\tcurrent money:",selected_player.current_money())
         desired_money = int(input("\t\tenter request: $"))
         if desired_money < 0 or desired_money > selected_player.current_money():   
            print("\t\tinvalid choice, try again\n")
      confirm_offer = -1
      ### confirm property, money request0
      while confirm_offer < 0 or confirm_offer > 1:
         print("\n\t\tyour money request is $"+str(desired_money))
         if current_request != "":
            print("\t\tyour property request is", current_request+"\n")
         print("\n\t\tConfirm request")
         print("\t\t  ","0) yes, continue")
         print("\t\t  ","1) no, exit trade")
         confirm_offer = int(input("\n\t\tchoice -> "))
      if confirm_offer == 1:
         return      
      ### selected_player accept/deny request
      print("\n\t\tPlayer "+selected_player.id+" is offered by Player "+str(player.id))
      print("\t\t   $"+str(offered_money))
      for i in range(0,len(offered_properties)):
            print("\t\t   -"+offered_properties[i].name)
      print("\t\tIn exchange for")
      print("\t\t   $"+str(desired_money))
      for i in range(0,len(desired_properties)):
         print("\t\t   -"+desired_properties[i].name)
      print("\n\t\tConfirm trade?")
      confirm_request= -1
      while confirm_request < 0 or confirm_request > 1:
         print("\t\t  ","0) accept")
         print("\t\t  ","1) reject")
         confirm_request = int(input("\n\t\tchoice -> "))
         print()
      if confirm_request == 1:
         print("\t\toffer rejected")
      elif confirm_request == 0:
         print("\t\toffer accepted")
         ### perform trade
         # trader
         for i in range(0,len(offered_properties)):
            if(i == 0):
               print("\n\tfor player "+selected_player.id,"...")
            game.transfer_deed(player,selected_player, offered_properties[i].index)
         if offered_money != 0:   
            game.transfer_payment(player, selected_player, offered_money)        
         print()
         # recipient    
         for i in range(0,len(desired_properties)):
            if(i == 0):
               print("\n\tfor player "+player.id,"...")            
            game.transfer_deed(selected_player, player, desired_properties[i].index)

         if desired_money != 0:            
            game.transfer_payment(selected_player, player, desired_money)
         print()
         player.player_status(game.board.tile)
      return  
   
   # event(self,player : Player, event : int) : void
   # def event(self, player, event = 0):   