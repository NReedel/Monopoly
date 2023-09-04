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
├── InitialPlayerEvents
├── PlayerEvents
├── JailedPlayerEvents
├── MenuPlayerEvents   
├── BankruptPlayerEvents  # incomplete
├── AvaliablePropertyEvents  
├── AuctionPropertyEvents # incomplete
├── CardEvents # incomplete
├── MainMenuEvents
├── BuildBuildingEvents # incomplete
├── SellBuildingEvents  # incomplete  
├── MortgagePropertyEvents
├── RedeemPropertyEvents         
├── TradeEvents # incomplete

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
      if len(args) > 0:
         for i in range(len(args)):
            self.arg.append(args[i]) 
                 
   #--Method Implementation--
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
      self.argc = len(args)
      if len(args) > 0:
         for i in range(len(args)):
            self.arg.append(args[i]) 
   
   #--Argumets--
   # arg[0] = self from game 

   #--Global Data--
   events = ["roll","build","sell","mortgage","redeem","trade","menu"]
    
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

         
            # error doesn't update proper     
                 
      '''     
      if event == "trade":
      
      '''   
      if event == "menu":
         menu = MenuPlayerEvents() # ADD UPDATE!
         choice = menu.display_event_options()
         while int(choice) < 0 or int(choice) >= len(menu.events):
            print("\t\tInvalid choice, try again\n")
            choice = menu.display_event_options()
         menu.event(player,menu.events[int(choice)])
         if player.bankrupt == True:
            return
         
class JailedPlayerEvents(Events):
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)
      
   #--Argumets--
   # arg[0] = self from game, used for bail and player
   
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
         rules_file_path = 'rules.txt' 
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
class AvaliablePropertyEvents(Events): # near complete
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)   
      self.argc = len(args)
      if len(args) > 0:
         for i in range(len(args)):
            self.arg.append(args[i]) 
            
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
   def event(self, event ):
      bank = self.arg[0].bank
      current_tile = self.arg[0].board.tile
      all_players = self.arg[0].all_players
      current_player = (all_players[self.arg[0].turn-1])
      current_tile = self.arg[0].board.tile[current_player.current_location()]
      # player_deeds.deep_copy(current_player.deeds)
      # bank_deeds = bank.deeds 
      if event == "purchase":
         ### buy deed from bank
         self.arg[0].transfer_payment(current_player, self.arg[0].bank, current_tile.property_cost)
         self.arg[0].transfer_deed(bank, current_player, current_player.current_location())
        
         
      if event == "auction": #needs testing
         auction = AuctionPropertyEvents(self.arg[0])
         auction_deed = self.arg[0].bank.deeds[current_player.current_location()] # copys current locations deed
         self.arg[0].bank.deeds.pop(current_player.current_location()) #remove deed
         auction.display_event_options(auction_deed,self.arg[0].all_players, self.arg[0].turn)
         del auction
         
class AuctionPropertyEvents(Events): #incomplete
   #--Constructor--
   def __init__(self, *args):
      super().__init__(*args)  
         
   #--Global Data--
   events = ["bid","forfeit"]
    
   #--Method Implementations--
   # display_event_options(self,auctioned_deed : Deed, all_players : Players, starting_bidder : int) : string 
   def display_event_options(self,auctioned_deed, all_players, starting_bidder): #incomplete
      current_bid = 0
      current_bidder = starting_bidder
      biding_players = all_players 
      while len(biding_players) > 1:
         print("\t\tcurrent bid: ",current_bid)
         for i in range(len(self.events)):
            num = str(i) + ")"
            print("\t\t  ",num,self.events[i]) 
            target_event = input("\n\t\tchoice -> ") 
         self.event(biding_players[current_bidder-1],target_event) 

   # event(self, players : Players, event : int) : void
   def event(self, player, event):
      return

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
   def __init__(self, ):
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
         rules_file_path = 'rules.txt' #vary by user
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
         print("\t\tSelect property to build:")
         print("\t\t ",str(-1)+")","cancel building")
         for i in range(0,len(self.events)):
            h = "h ="
            development = board.tile[self.events[i].index].houses 
            if(board.tile[self.events[i].index].hotels > 0):
               h = "H ="
               development = board.tile[self.events[i].index].hotels
            # self.events.append(self.events[i].name) #change to player.owned_deeds.name
            num = str(i) + ") " # + str(self.events[i].index)
            print("\t\t  ",num,self.events[i].name,h,development)          

         target_event = input("\n\t\tchoice -> ")
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
            print("\t\tcan't afford the selection, try again\n")

      bank = self.arg[0].bank
      # print("\n\t\t"+self.events[int(target_event)].name,"building =",self.events[int(target_event)].name)      
      self.arg[0].transfer_payment(player,bank,payment) 
      return self.events[int(target_event)].index
   
   # event(self,event : int) : void
   def event(self,player,event):
      board = self.arg[0].board
      if board.tile[event].houses < 4:
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
      print()
      if int(target_event) == -1:
         return -1
      target_deed = self.events[int(target_event)]
      if board.tile[self.events[int(target_event)].index].hotels == 1:
         payment = int(target_deed.hotel_cost / 2)
      else:
         payment = int(target_deed.house_cost / 2)        
      bank = self.arg[0].bank
      # print("\n\t\t"+self.events[int(target_event)].name,"building =",self.events[int(target_event)].name)      
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
         
   # display_event_options(self,player : players) : list 
   def display_event_options(self,player): #incomplete
      print("\t\tSelect property to trade:")
      ''' 
      for i in range(0,len(player.owned_deeds)):  
         self.events.append(player.owned_deeds[i]) #change to player.owned_deeds.name
         num = str(i) + ")"
         print("\t\t  ",num,self.events[i])
      ''' 
      print("\t\t  ",str(-1)+")","cancel trade offer") # maybe
      target_event = input("\n\t\tchoice -> ")
      print("\t\tSelect money to trade(",player.current_money(),")")
      target_money = input("\n\t\tchoice -> ")
      list_pairing = [target_event,target_money]
      return list_pairing
   
   # event(self,player : Player, event : int) : void
   # def event(self, player, event = 0):   
