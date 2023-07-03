# events.py

###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Handle specialised user event and display event options
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
├── CardEvents #new   
├── MainMenuEvents
├── SellPropertyEvents
├── BuildPropertyEvents         
├── MortgagePropertyEvents
├── RedeemPropertyEvents         
├── TradeEvents
'''
###############################################################
from players import *
from deeds import *
# from game import *
from asyncio import events


class Events:
   #--Global Data--
   argc = 0
   events = []
   #--Constuctor--
   def __init__(self,*args):
      self.argc = 0 # argument count
      if len(args) > 0:
         for i in args:
            self.argc += i
            
   #--Method Implementation--
   def display_event_options(self): 
      return 
   def event(self): # event() : void
      return

   
class PlayerEvents(Events): # partial completion
   #--Global Data--
   events = ["roll","build","sell","mortgage","redeem","trade","menu"]
   '''    
   #--Method Implementations--
   # display_event_options(self) : void
   def display_event_options(self):
      return
   # event(self player : Players, event : string) : void
   def event(self,player,event = ""):
      if event == "roll":
         self.move(player)
      if event == "build":
      if event == "sell":
      if event == "mortgage":
      if event == "redeem":
      if event == "trade"
      if event == "menu":
   '''   
      
class Jailed_Player_Events(Events): # partial completion
   #--Global Data--
   event = ["roll doubles","pay jail fee","jail free card"]
   
   #--Method Implementations--
   '''
   # display_event_options(self) : void
   def display_event_options(self):
      return  
   # event(player : Players, event : string) : bool
   def event(self,player,event=""): 
      
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
   '''
class MenuPlayerEvents(Events):
   #--Global Data--
   events = ["leave game","return to game","rules"]
    
   #--Method Implementations--
   # display_event_options(self) : void
   def display_event_options(self):
      return
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""):
      return
   
class BankruptPlayerEvents(Events):
   #--Global Data--
   events = ["give up","sell","mortgage","trade","menu"]
   #--Method Implementations--
   # display_event_options(self) : void
   def display_event_options(self):
      return
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""):
      return
      
class AvaliablePropertyEvents(Events):
   #--Global Data--
   events = ["purchase","auction"]
    
   #--Method Implementations--
   # display_event_options(self) : void
   def display_event_options(self):
      return
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""):
      return

class AuctionPropertyEvents(Events):
   #--Global Data--
   events = ["bid","forfeit"]
    
   #--Method Implementations--
   # display_event_options(self) : void
   def display_event_options(self):
      return

   # event(self, all_players : Players, event : string, target_property : deeds) : void
   def event(self,all_players,event = "",):
      return
   
class CardEvents(Events):
   #--Global Data--
   events = ["take a chance"]
    
   #--Method Implementations--
   # display_event_options(self) : void
   def display_event_options(self):
      return
      
   # event(self, player : Players, event : string) : void
   def event(self,player,event = ""):
      return

class MainMenuEvents(Events):
   #--Global Data--
   events = ["start game","number of players","rules","settings"] 
   
   #--Method Implementations--
   # display_event_options(self) : void
   def display_event_options(self): 
      return
   
   # event(self, event : string) : void
   def event(self, event = " "): 
      return
   
# class SellPropertyEvents(Events):

# class BuildPropertyEvents(Events):  
       
# class MortgagePropertyEvents(Events):

# class RedeemPropertyEvents(Events):       
  
# class TradeEvents(Events):

