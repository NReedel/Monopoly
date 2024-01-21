# game.py

###
# *Name:      Alicyn Knapp, Chris Schneider, Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Connects all other classes other than monopoly. Deals with 
#             turns, the players, and their interactions with each other,
#             the board and bank. 
###

#--Imports--
from . import dice
from . import bank
from . import events
from . import board
from . import deeds
import json
import copy
import os

class Game:
   ###--Global Data--
   starting_total = int(2500)
   bail = int(50)
   monopoly_characters = ("cannon", "thimble", "top hat", "iron", "battleship", "boot", "race car","purse") 
   payment = int(0) # Note: used to store return value from pay_money() and used as arg in recieve_money()
   game_dice = dice.Dice(2,6)
   turn = int(1)
   round = int(1)
   all_players = []
   bank = bank.Bank()
   board = board.Board()
   last_deck_drawn = str("")
   player_events = events.PlayerEvents()
   jailed_player_events = events.JailedPlayerEvents()
   bankrupt_player_events = events.BankruptPlayerEvents()

   ###--Constructor--
   def __init__(self):
      with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'json', 'tiles.json'), 'r') as rf:
         for tiles in json.load(rf):
            match tiles['type']:
               case "street":
                  self.bank.deeds.append(deeds.DeedStreet(tiles))
               
               case "railroad":
                  self.bank.deeds.append(deeds.DeedRailroad(tiles))
               
               case "utility":
                  self.bank.deeds.append(deeds.DeedUtility(tiles))
                
            self.board.tile[tiles['index']].owned_by = "bank"
         
         self.board.tile_check(self.all_players) 

   ###--Method Implementations--
   # transfer(self) : void
   def transfer_all(self): 
      starting_deeds_size = len(self.bank.deeds)
      for i in range(0,starting_deeds_size):
         self.transfer_deed(self.bank,self.all_players[0],self.bank.deeds[i].index)
          
   # pass_GO(self, player : Player, next_location : int) : int
   def pass_GO_check(self, player, next_location):
      ''' If player has passed GO, pays the player and resets to 40 > next_location > 0 based on next_location mod 40 '''
      if next_location >= 40 or next_location == 0:
         player.receive_money(200)
         next_location = next_location % 40
      
      return next_location
   
   # calculate_spaces_moving(self, current_location : int, next_location : int) : int
   def calculate_spaces_moving(self, current_location, next_location):
      ''' For cases when spaces_moving is not determined by a dice roll (i.e., card events), takes the current location and next location, and returns spaces_moving '''
      if next_location < current_location:
          spaces_moving =  next_location + (40 - current_location)  # i.e. (next_location - GO (0)) + (NONE (40) - player.current_location())
      else:
          spaces_moving = next_location - current_location
          
      return spaces_moving
   
   # tile_landing_events(self, player : Player, next_location : int, isPersistentCardEvent : bool) : void
   def tile_landing_events(self, player, next_location, isPersistentCardEvent):
      ''' Determines the landed-on tile's type and conducts the actions associated with different tile types and states '''
      current_tile = self.board.tile[next_location]
      
      if current_tile.tile_type != "special": # tile with deed
         
         if current_tile.available_deed() == True : # purchasable
            print("\t\tthis property can be bought\n")
            available_property_events = events.AvailablePropertyEvents(self)
            cost = current_tile.property_cost
            can_buy = False
            if cost <= player.current_money():
               can_buy = True
            target_event = available_property_events.display_event_options(cost, player.current_money())
            
            while ((int(target_event) < 0 or len(available_property_events.events)) <= int(target_event) and can_buy == True) or (can_buy == False and (int(target_event) >= len(available_property_events.events) or int(target_event) < 1)):
               print("\t\tinvalid choce, try again\n")
               target_event = available_property_events.display_event_options(cost, player.current_money())
               
            available_property_events.event(available_property_events.events[int(target_event)])
            del available_property_events

         elif current_tile.is_mortgaged == True: #mortgaged property
            print("\t\tproperty is mortgaged\n")
            return

         elif current_tile.owned_by == player.id: # self owned
            print("\t\tyou own this property\n")

         elif current_tile.owned_by != player.id and current_tile.owned_by != "bank": # pay rent
            print("\t\tyou landed on another player's property\n")
            owner_number = int(current_tile.owned_by)
            rent_value = 0 # index for options
            
            current_deed = self.all_players[owner_number-1].target_deed(next_location)
            
            ### street
            match current_tile.tile_type:
               case "street":
                  # options = ["R", "M_R", "R_H_1", "R_H_2","R_H_3","R_H_4","R_H"]
                  if current_tile.has_monopoly == True:
                     rent_value = 1 # monopoly_rent
                  if current_tile.houses > 0:
                     rent_value =  current_tile.houses + 1 # rent_house_
                  if current_tile.hotels > 0:
                     rent_value = 6 # rent_hotel_
                  
                  payment = current_deed.current_rent(rent_value)
                  self.transfer_payment(player, self.all_players[owner_number-1], payment)
                  print("")
                  return

            ### railroad
               case "railroad":
                  #options = ["R", "R_2", "R_3", "R_4"]
                  if current_tile.multiplier == 2:
                     rent_value = 1
                  elif current_tile.multiplier == 3:
                     rent_value = 2
                  elif current_tile.multiplier == 4:
                     rent_value = 3
                     
                  normal_payment = current_deed.current_rent(rent_value)

                  if isPersistentCardEvent:
                     # gathering last_card_drawn for card_event attribute
                     if self.last_deck_drawn is self.board.chance.deck_name:  # chance
                        drawn_card = self.board.chance.last_card_drawn
                     elif self.last_deck_drawn is self.board.community_chest.deck_name:   # chest
                        drawn_card = self.board.community_chest.last_card_drawn
                        
                     
                     print(f"\t\tplayer {player.id} normally owes = {normal_payment}")

                     adjusted_payment = drawn_card.card_event.get_adjusted_rent(normal_payment)
                     
                     print(f"\t\tplayer {player.id} now owes = {adjusted_payment}")
                     
                     self.transfer_payment(player, self.all_players[owner_number-1], adjusted_payment)
                     print("")
                     return
                  
                  self.transfer_payment(player, self.all_players[owner_number-1], normal_payment)
                  print("")
                  return

            ### utilites
               case "utility":
                  utility_dice = dice.Dice(2, 6)
                  utility_dice.roll()
                  print(f"\t\tplayer {player.id} roll = {utility_dice.print_roll}")
                  
                  if isPersistentCardEvent:
                     # gathering last_card_drawn for card_event attribute
                     if self.last_deck_drawn is self.board.chance.deck_name:  # chance
                        drawn_card = self.board.chance.last_card_drawn
                     elif self.last_deck_drawn is self.board.community_chest.deck_name:   # chest
                        drawn_card = self.board.community_chest.last_card_drawn
                        
                     adjusted_payment = drawn_card.card_event.get_adjusted_rent(utility_dice.total_rolled())
                     self.transfer_payment(player, self.all_players[owner_number-1], adjusted_payment)
                     print("")
                     return
                  
                  # options = ["R_M_1", "R_M_2"]
                  if current_tile.multiplier == 2:
                     rent_value = 1

                  payment = current_deed.current_rent(rent_value) * utility_dice.total_rolled()
                  self.transfer_payment(player, self.all_players[owner_number-1], payment)
                  print("")
                  return

      else: # landing on special tile
         match current_tile.special_type:
            case "corner":
               match current_tile.corner_type:
                  case "arrested":   # Go To Jail
                     player.go_to_jail()
                     
                  case "jail":
                     pass
                  
                  case "parking":
                     pass
                  
                  case "go":
                     pass

            # tax tiles
            case "tax":
               player.pay_money(current_tile.tax_amount)
             
            # card tiles
            case "card":
               match current_tile.card_type:
                  case self.board.chance.deck_name:
                     chance_card = self.board.chance.draw_card()
                     self.last_deck_drawn = self.board.chance.deck_name

                     print("\t\tThe card reads:")
                     print(f"\t\t{chance_card.description}")
                     print("")
                     
                     self.card_event_match(chance_card, player)

                  case self.board.community_chest.deck_name:
                     chest_card = self.board.community_chest.draw_card()
                     self.last_deck_drawn = self.board.community_chest.deck_name

                     print("\t\tThe card reads:")
                     print(f"\t\t{chest_card.description}")
                     print("")
                     
                     self.card_event_match(chest_card, player)
         return


   # card_event_match(self, card : Card, player : Player) : void
   def card_event_match(self, card, player):
       ''' Finds a match for the card's event name and conducts the given event '''
       match card.event_name:
           case "payStaticAmount":
               new_player_balance = card.card_event.pay_money(player.current_money())
               player.set_balance(new_player_balance)

           case "receiveStaticAmount":
               new_player_balance = card.card_event.receive_money(player.current_money())
               player.set_balance(new_player_balance)

           case "payPlayerRateAmount":
               new_player_balance = card.card_event.pay_money(player.current_money(), len(self.all_players))
               player.set_balance(new_player_balance)

               # pay all other players using card_events.receive_owed_amount()
               for i in range(len(self.all_players)):
                   if (self.all_players[i].id != player.id):    # avoids the player drawing the card
                       new_other_player_balance = card.card_event.receive_owed_amount(player.current_money())
                       self.all_players[i].set_balance(new_other_player_balance)
                       
           case "payBuildingRateAmount":
               new_player_balance = card.card_event.pay_money(player.current_money(), player.total_houses, player.total_hotels)
               player.set_balance(new_player_balance)

           case "receivePlayerRateAmount":
               new_player_balance = card.card_event.receive_money(player.current_money(), len(self.all_players))
               player.set_balance(new_player_balance)

               # receive money from all other players using card_events.pay_owed_amount()
               for i in range(len(self.all_players)):
                   if (self.all_players[i].id != player.id):    # avoids the player drawing the card
                       new_other_player_balance = card.card_event.pay_owed_amount(player.current_money())
                       self.all_players[i].set_balance(new_other_player_balance)

           case "moveToIndex":
               if (card.subtype != "Jail"):     # Go To Jail card does not allow collection of GO payment
                   next_location = card.card_event.move_to_index()
                   
                   spaces_moving = self.calculate_spaces_moving(player.current_location(), next_location)
                   new_player_location = self.pass_GO_check(player, player.current_location() + spaces_moving)
                       
               else: # Go To Jail
                   new_player_location = card.card_event.move_to_index()
                   player.in_jail = True

               player.move_location(new_player_location, self.board.location(new_player_location))
               print("")
               self.tile_landing_events(player, new_player_location, False)   # isPersistentCardEvent = False

           case "moveToNearest": # isPersistentCardEvent
               if (not card.isMoveToUtility): # railroads
                   next_location = card.card_event.move_to_nearest_railroad(player.current_location())
                   
                   spaces_moving = self.calculate_spaces_moving(player.current_location(), next_location)
                   new_player_location = self.pass_GO_check(player, player.current_location() + spaces_moving)
                       
               elif (card.isMoveToUtility): # utilities
                   next_location = card.card_event.move_to_nearest_utility(player.current_location())
                   
                   spaces_moving = self.calculate_spaces_moving(player.current_location(), next_location)
                   new_player_location = self.pass_GO_check(player, player.current_location() + spaces_moving)
                   
               else:
                   print("\t\tInvalid moveToNearest card type in card class; neither Railroad nor Utility. Player will not be moved.")
                   new_player_location = player.current_location()
               
               player.move_location(new_player_location, self.board.location(new_player_location))
               print("")
               self.tile_landing_events(player, new_player_location, True)   # isPersistentCardEvent = True

           case "moveSpaces":
               if card.card_event.isReverseMove:   # player does not collect GO if moving counter-clockwise (i.e., reverse movement/negative moveSpaces)
                   new_player_location = card.card_event.move_spaces(player.current_location())
               else:
                  new_player_location = self.pass_GO_check(player, card.card_event.move_spaces(player.current_location()))

               player.move_location(new_player_location, self.board.location(new_player_location))
               print("")
               self.tile_landing_events(player, new_player_location, False)   # isPersistentCardEvent = False

           case "isGOJF":
               player.jail_free_card = card.card_event.give_card(player.jail_free_card)
           
           case _:
               print(f"\t\tNo event with the name {card.event_name} found.")
        

   # move(self, Player : Players, spaces_moving: int) : void
   def move(self,player,spaces_moving):
      # checks if the player passes GO on the next move
      #     and sets the new location to either next_location % 40 (passed GO) or current_location + spaces_moving
      next_location = self.pass_GO_check(player, player.current_location() + spaces_moving)
         
      player.move_location(next_location, self.board.location(next_location)) # new
      print("")
      self.tile_landing_events(player, next_location, False)   # isPersistentCardEvent = False
      
   # # transfer_payment(payer : T, recipient :  T, paymnet : int) : void
   def transfer_payment(self,payer, recipient, payment):
      payer.pay_money(payment)
      recipient.receive_money(payment)

   # transfer_deed(owner: T, recipient :  T, location : int) : void
   def transfer_deed(self,owner, recipient, location): 
      owner_deeds = copy.deepcopy(owner.deeds) # maybe
      recipient_deeds = copy.deepcopy(recipient.deeds)

      for i in range(0,len(owner_deeds)): 
         
         if location == owner_deeds[i].index:
            target_deed = owner_deeds[i]
            i = len(owner_deeds)
      ###Aleternative to performing a sort
      # if len(recipient_deeds) == 0:
      #    recipient_deeds.append(target_deed)
      # elif location < recipient_deeds[0].index:  
      #    print(location, recipient_deeds[0].index)
      #    recipient_deeds.insert(0,target_deed)
      # else:     
      #    for i in range(1,len(recipient_deeds)): 
            
      #       if location > recipient_deeds[i-1].index:
      #          recipient_deeds.insert(i,target_deed)
      #          i = len(recipient_deeds)
      recipient_deeds.append(target_deed)
      recipient.deeds = copy.deepcopy(recipient_deeds)
      print("\t\t\""+str(target_deed.name)+"\"","received\n")
      self.board.tile[location].owned_by = recipient.id
      self.board.tile_check(self.all_players)
      if recipient.id != "bank":   
         recipient.sort_deeds()
      
   # jailed_move_attempt(self, player : Players) : void
   def jailed_move_attempt(self,player): 
      self.game_dice.roll()
      print("\t\tplayer",player.id,"roll =",self.game_dice.print_roll())
      
      if self.game_dice.rolled_same_values() == True or player.time_jailed == 3:
         
         if player.time_jailed == 3 and self.game_dice.rolled_same_values() == False:
            player.time_jailed = 0
            player.pay_money(self.bail)    
            
         print("\t\tplayer",player.id(),"is now out of jail")
         next_location = self.pass_GO_check(player, player.current_location() + self.game_dice.total_rolled())
            
         player.move_location(next_location, self.board.location(next_location)) # move
         print("")  
         return False # in_jail = False
      
      else:
         print("\t\tplayer",player.id,"remains in jail")
         print("")  
         return True # in_jail = True

   # end_round_check(RemainingPlayers : list<Players>) : void
   def end_round_check(self,remainingPlayers = []):
      
      if self.turn > len(remainingPlayers): # reset turns, start next round
         self.turn = self.turn % len(remainingPlayers) 
         self.round += 1
         print("Round ",self.round)
         print("")
                  
         for i in range(0,len(remainingPlayers)):
            remainingPlayers[i].same_values_rolled = 0

   # take_self.turn(Target_players : list<Players>) : void
   def take_turn(self,target_players = []):
      print("\tPlayer",target_players[self.turn-1].id, ":") 
      
      ###List Target_players Status 
      target_players[self.turn-1].player_status(self.board.tile)  
      
      while target_players[self.turn-1].in_debt() == True: 
         ###Bakrupt Player Events 
         self.bankrupt_player_events.update(self)
         print("\t\tplayer",target_players[self.turn-1].id,"is in debt at","$"+str(target_players[self.turn-1].current_money()),"\n")
         target_event = self.bankrupt_player_events.display_event_options()
         
         while int(target_event) < 0 or len(self.bankrupt_player_events.events) <= int(target_event):
            print("\t\tInvalid choice, try again\n")
            target_event = self.bankrupt_player_events.display_event_options()
            
         self.bankrupt_player_events.event(target_players[self.turn-1],self.bankrupt_player_events.events[int(target_event)])
         if target_players[self.turn-1].bankrupt == True:
            return 
         
      if target_players[self.turn-1].in_jail == True:
         target_players[self.turn-1].time_jailed += 1
         
      self.player_events.update(self)
      self.jailed_player_events.update(self)
      has_rolled = False
      end_turn = False
      attempt_escape = False
      
      ###Start Turn
      while end_turn == False:
         
         ###Jailed Player Events
         if target_players[self.turn-1].in_jail == True and has_rolled == False: 
            target_event = self.jailed_player_events.display_event_options(target_players[self.turn-1]) 
            
            while int(target_event) < 0 or len(self.jailed_player_events.events) <= int(target_event) or int(target_event == 2) and target_players[self.turn-1].jail_free_card == 0:
               ###redisplay if given bad input
               print("\t\tInvalid choice, try again\n")
               target_event = self.jailed_player_events.display_event_options(target_players[self.turn-1])
               
            print("")
            
            if int(target_event) == 0:
               ###jailed_player_events.event returns True automatically
               attempt_escape = self.jailed_player_events.event(target_players[self.turn-1],self.jailed_player_events.events[int(target_event)])
            else:
               ###jailed_player_events.event returns True if player stays in jail
               target_players[self.turn-1].in_jail = self.jailed_player_events.event(target_players[self.turn-1],self.jailed_player_events.events[int(target_event)])
         
         ###Player Events
         if target_players[self.turn-1].bankrupt == False: 
            target_event = self.player_events.display_event_options(has_rolled) 
            
               
         ###Player Menu Quit 
         if target_players[self.turn-1].bankrupt == True:
            has_rolled = True
            end_turn = True
            return 
         ###end Player Menu Quit

         if int(target_event) == 0 and has_rolled == False:
            has_rolled = True
         elif int(target_event) == 0 and has_rolled == True:
            end_turn = True
         else:
            pass         
            
         if end_turn  == False:
            print("")
            if (attempt_escape == True and int(target_event) != 0) or attempt_escape == False:   
               self.player_events.event(target_players[self.turn-1],self.player_events.events[int(target_event)]) 
            if attempt_escape == True and int(target_event) == 0:
               print("\t\tattempt jail escape")
               target_players[self.turn-1].in_jail = self.jailed_move_attempt(target_players[self.turn-1])
               has_rolled = True
               
            elif self.game_dice.rolled_same_values() == True and target_players[self.turn-1].same_values_rolled == 2 and self.player_events.events[int(target_event)] == "roll":   
               print("\t\tsame values rolled =",target_players[self.turn-1].same_values_rolled+1)
               target_players[self.turn-1].go_to_jail()
               print("")
               target_players[self.turn-1].same_values_rolled += 1
               self.turn += 1
               self.end_round_check(target_players)
               return
           
      ###End Of Turn
      if(self.game_dice.rolled_same_values() == False or attempt_escape == True):   
         self.turn += 1
      else:
         target_players[self.turn-1].same_values_rolled += 1
         print("\n\t\tPlayer",target_players[self.turn-1].id,"goes again")
         
      print("")
      
      if self.turn > len(target_players): # reset self.turns, start next self.round
         self.end_round_check(target_players)
 
   # end take_turn
   
# end class
