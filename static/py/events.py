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
├── BankruptPlayerEvents
├── AvaliablePropertyEvents
├── AuctionPropertyEvents
├── CardEvents 
├── MainMenuEvents
├── BuildBuildingEvents 
├── SellBuildingEvents        
├── MortgagePropertyEvents
├── RedeemPropertyEvents         
├── TradeEvents

'''
###############################################################
# current_player = self.arg[0].all_players[self.arg[0].turn-1] # alt
 
#--Imports--
from players import *
import copy

class Events:
   #--Global Data--
   argc = int(0)
   arg = []
   events = []
   # player = Players() 
   
   #--Constuctor--
   def __init__(self,*args):
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

   
class PlayerEvents(Events): # partial completion #add boundry while loop
   #--Argumets--
   # arg[0] = self from game 
   # arg[1] = bool(has_rolled) from game 
   
   #--Global Data--
   events = ["roll","build","sell","mortgage","redeem","trade","menu"]
    
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self):
      if self.arg[0].all_players[self.arg[0].turn-1].bankrupt == False: # new
         print("\t\tSelect players action:")  
         if self.arg[1] == True: 
            print("\t\t   0) pass turn")
         else: 
            print("\t\t   0)",self.events[0])
         for i in range(1,len(self.events)):
            num = str(i)
            num = num + ")"
            print("\t\t  ",num,self.events[i])
         target_event = input("\n\t\tchoice -> ")      
         return target_event
      else: # new
         return 0
   
   # event(self player : Players, event : string) : void
   def event(self,player,event = ""):
      if event == "roll":
         self.arg[0].game_dice.roll()
         print("\t\tplayer",player.player_number(),"roll =",self.arg[0].game_dice.print_roll()) # add roll total
         # needs if condition for alt moves
         self.arg[0].move(player, self.arg[0].game_dice.total_rolled()) 
      if event == "build":
         build = BuildBuildingEvents()
         choice = build.display_event_options(player)
         if choice != -1 :
            sell.event(player,choice)   
         else: 
            print()
            return
      if event == "sell":
         sell = SellBuildingEvents()
         choice = sell.display_event_options(player)
         if choice != -1 :
            sell.event(player,choice)   
         else: 
            print()
            return
            
      '''      
      if event == "mortgage":
      if event == "redeem":
      if event == "trade":
      
      '''   
      if event == "menu": # new
         menu = MenuPlayerEvents()
         choice = menu.display_event_options()
         menu.event(player,menu.events[int(choice)])
         
class JailedPlayerEvents(Events): # partial completion
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
         print("\t\tPlayer",player.player_number(),"is now out of jail\n")
         return False #player.in_jail == False
      
      if event == "jail free card":
         player.jail_free_card -= 1
         player.time_jailed = 0
         print("\t\tPlayer",player.player_number(),"is now out of jail\n")
         return False #player.in_jail == False
      
      return True

class MenuPlayerEvents(Events):
   #--Global Data--
   events = ["leave game","return to game","rules"]
    
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self): # new
      print("\t\tSelect players action:")
      for i in range(0,len(self.events)):
         num = str(i)+")"
         print("\t\t  ",num,self.events[i])
      target_event = input("\n\t\tchoice -> ")       
      return target_event
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""): # new
      if event == "leave game":
         player.bankrupt = True
         print()
         return
      if event == "return to game":
         print()
         return
      if event == "rules":
         rules_file_path = '/mnt/c/Users/Nreed/Code/All_Code/Monopoly/references/rules.txt' #vary by user
         with open(rules_file_path, 'r') as file:
            # Read the contents of the file
            file_contents = file.read()
         # Print the contents of the file
         print(file_contents)
         blank = input("\npress enter to exit\n")
         return
            
class BankruptPlayerEvents(Events):
   #--Global Data--
   events = ["give up","sell","mortgage","trade","menu"]
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self):
      print("\t\tSelect in dept players action:")  
      for i in range(0,len(self.events)):
         num = str(i)
         num = num + ")"
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
class AvaliablePropertyEvents(Events):
   #--Global Data--
   events = ["purchase","auction"]
    
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self):
      return
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""):
      return

class AuctionPropertyEvents(Events):
   #--Global Data--
   events = ["bid","forfeit"]
    
   #--Method Implementations--
   # display_event_options(self) : string 
   def display_event_options(self):
      return

   # event(self, all_players : Players, event : string, target_property : deeds) : void
   def event(self,all_players,event = "",):
      return
   
class CardEvents(Events):
   #--Global Data--
   events = ["take a chance"]
    
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self):
      return
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""):
      return

class MainMenuEvents(Events):
   #--Global Data--
   events = ["start game","number of players","rules","settings"] 
   
   #--Method Implementations--
   # display_event_options(self) : string
   def display_event_options(self): 
      return
   
   # event(self, event : string) : void
   def event(self, event = " "): 
      return
   
class BuildBuildingEvents(Events):
   
   # display_event_options(self,player : players) : string
   def display_event_options(self,player): 
      print("\t\tSelect property to build on:")
      '''
      for i in range(0,len(player.owned_deeds)):
         if player.owned_deeds[i].monopoly == True: #not actual code   
            self.events.append(player.owned_deeds[i]) #change to player.owned_deeds.name
            num = str(i) + ")"
            print("\t\t  ",num,self.events[i])
      '''
      print("\t\t  ",str(-1)+")","cancel build")
      target_event = input("\n\t\tchoice -> ")     
      return int(target_event)
   
   # event(self,player : Player, event : int) : void
   # def event(self, player, event = 0):

   
class SellBuildingEvents(Events): #almost complete

   # display_event_options(self,player : players) : string
   def display_event_options(self,player): 
      print("\t\tSelect building to sell:")
      '''
      for i in range(0,len(player.owned_deeds)):
         if player.owned_deeds[i].has_building == True: #not actual code
            self.events.append(player.owned_deeds[i]) #change to player.owned_deeds.name
            num = str(i) + ")"   
            print("\t\t  ",num,self.events[i])
      ''' 
      print("\t\t  ",str(-1)+")","cancel sale")
      target_event = input("\n\t\tchoice -> ")     
      return int(target_event)
   
   # event(self,player : Players, event : int) : void
   def event(self,player, event): #error
      return

       
class MortgagePropertyEvents(Events):
   # display_event_options(self,player : players) : string
   def display_event_options(self,player): 
      print("\t\tSelect property to mortgage:")
      '''   
      for i in range(0,len(player.owned_deeds)):  
         self.events.append(player.owned_deeds[i]) #change to player.owned_deeds.name
         num = str(i)
         num = num + ")"   
         print("\t\t  ",num,self.events[i])
      '''
      target_event = input("\n\t\tchoice -> ")     
      return int(target_event)
   
   # event(self,player : Player, event : int) : void
   # def event(self, player, event = 0):   

class RedeemPropertyEvents(Events):    
   # display_event_options(self,player : players) : string
   def display_event_options(self,player): 
      print("\t\tSelect property to redeem:")   
      for i in range(0,len(player.owned_deeds)):  
         self.events.append(player.owned_deeds[i]) #change to player.owned_deeds.name
         num = str(i)
         num = num + ")"   
         print("\t\t  ",num,self.events[i])
      target_event = input("\n\t\tchoice -> ")     
      return int(target_event)
   
   # event(self,player : Player, event : int) : void
   # def event(self, player, event = 0):   
  
class TradeEvents(Events):
   # display_event_options(self,player : players) : list 
   def display_event_options(self,player): #?
      print("\t\tSelect property to trade:")   
      for i in range(0,len(player.owned_deeds)):  
         self.events.append(player.owned_deeds[i]) #change to player.owned_deeds.name
         num = str(i) + ")"
         print("\t\t  ",num,self.events[i])
      target_event = input("\n\t\tchoice -> ")
      print("\t\tSelect money to trade(",player.current_money(),")")
      target_money = input("\n\t\tchoice -> ")
      list_pairing = [target_event,target_money]
      return list_pairing
   
   # event(self,player : Player, event : int) : void
   # def event(self, player, event = 0):   
