# players.py

###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Define monopoly player traits and actions
###


from deeds import *
import copy

class Players:
   
   # --Global Data--
   # nickname : string # represents username of player in monopoly
   # character : string # represents the figure a player uses in game
   id = str(0) # -id : str
   __money = int(0) # -__money : int
   __location = int(0) # -__location : int
   location_name = "go" # location_name : str
   has_rolled = False
   same_values_rolled = int(0) # doublesrolled : int

   in_jail = False  # +in_Jail : bool 
   time_jailed = int(0) # +time_jailded : int 
   jail_free_card = int(0) # +jail_free_card : int
   deeds = [] # +deeds : list <Deeds>
   total_houses = int(0) # +total_houses : int
   total_buildings = int(0) # +total_buildings : int
   bankrupt = False # +bankrupt : bool
   
   #--Contstructor--
   def __init__(self,startingTotal = 0, id_number = 0): 
      self.__money = startingTotal
      self.id = id_number
      
   #--Method Implementations--
   # player_assets(self, tiles) : void
   def player_status(self,tiles): 
      ###List Player Assets (static stats)
      # print("player number = "self.id)
      # print("player character = "self.character)
      print("\t\tmoney =","$"+str(self.current_money()))
      print("\t\tin debt =",self.in_debt())
      print("\t\tlocation",str("["+str(self.current_location()))+"] =",self.location_name)
      print("\t\tsame values rolled =",self.same_values_rolled )
      # if self.in_jail == True:
      print("\t\tin jail =",self.in_jail)
      if self.in_jail == True:
         print("\t\ttime jailed =",self.time_jailed)
      # if self.jail_free_card > 0:
      print("\t\tjail free cards =",self.jail_free_card)
      print("\t\tproperties:",len(self.deeds))
      tile_status = "" # (m),houses[n],hotel[n]
      for i in range(0,len(self.deeds)):

         owned_tile = tiles[self.deeds[i].index]
         if(owned_tile.is_mortgaged == True):
            tile_status = tile_status + "(m) "
         if(owned_tile.houses > 1) and (owned_tile.hotels < 1) :
            tile_status = tile_status + " h = " + str(owned_tile.houses) + " "
         if(owned_tile.hotels > 0) :
            tile_status = tile_status + " H = " + str(owned_tile.hotels) + " "               
         print("\t\t   -",self.deeds[i].name,tile_status)
         tile_status = ""
         
      # print("\t\tmortgages :",len(self.owned_mortgages)) #maybe
      # for i in range(0,len(self.owned_mortgages)):
      #    print("\t\t   -",self.owned_mortgages[i])  #needs modification
      print("\t\ttotal houses =",self.total_houses)
      print("\t\ttotal hotels =",self.total_buildings)
      # print("\t\tbankrupt =",self.bankrupt)
      # print("\t\t")
      print("\t\t-----------------------------")    
   
   # move_location(next_location : int, location_text) : void
   def move_location(self,next_location, location_text): 
      # print("move to location number",next_location)
      self.__location = next_location
      self.location_name = location_text
      print("\n\t\tplayer",self.id,"location is ","\n\t\t["+str(self.__location)+"]",self.location_name)
      
   # current_location(self) : int
   def current_location(self):
      return self.__location
   
   # current_money(self) : void
   def current_money(self):
      return  self.__money   
   
   # recieve_money(self, amount : int) : void
   def receive_money(self,amount):
      self.__money += amount
      print("\t\tplayer",self.id, "recieved $" + str(amount))
   
   # pay_money(self, amount : int ) :  int
   def pay_money(self,amount):
      self.__money -= amount
      print("\t\tplayer",self.id, "payed $" + str(amount))
   
   # change_balance(self, new_total : int) : void
   def set_balance(self, new_total):
       """ Sets the total amount of money held by the player equal to the new total parameter """
       self.__money = new_total
   
   # def inDebt(self) : bool
   def in_debt(self) :
      if self.__money < 0:
         return True
      return False
   
   # go_to_Jail() : void
   def go_to_jail(self): 
      self.__location = 10
      print("\t\tplayer", self.id,"location =", self.__location) 
      self.in_jail = True
      print("\t\tplayer",self.id,"is now in jail")
      self.jail_counter = 0

   # buy_property(deed : deeds) : void
   def add_property(self,deed):
      copy_list = []
      copy_list = copy.deepcopy(self.deeds)
      self.deeds.clear()
      copy_list.append(deed)
      print("copy_list")
      for i in range(len(copy_list)):
         print("\t",i,copy_list[i].name)   
      self.deeds = copy.deepcopy(copy_list)
      print("\ncurrent_deeds")
      for i in range(len(self.deeds)):
         print("\t",i,self.deeds[i].name) 
      del copy_list
      
   # remove_property(property : int, reciever : string ) : void
   def remove_property(self,index):
      for i in range(len(self.deeds)):
         if index == self.deeds[i].index:
            target_deed = self.deeds[i]
            self.deeds.pop(i)
            return target_deed

   #property_cost (index : int) : int
   def property_cost(self,index): # needs adjustment for houses and property collection
      for i in range(len(self.deeds)):
         if index == self.deeds[i].index:
            target_deed = self.deeds[i]
            return int(target_deed.rent)     
   
   # mortgageable_property_list(self, tiles : list<tiles>) : list <deeds> # must refrence deed tile
   def mortgageable_property_list(self, tiles): 
      mortgageable_property = []
      for i in range(len(self.deeds)):
         owned_tile = tiles[self.deeds[i].index]
         if owned_tile.is_mortgaged == False and owned_tile.houses == 0 and owned_tile.hotels == 0:
            mortgageable_property.append(self.deeds[i])
            
      return mortgageable_property
   
   # unmortgageable_property_list(self, tiles : list<tiles>) : list <deeds>
   def unmortgageable_property_list(self, tiles): 
      unmortgageable_property = []
      for i in range(len(self.deeds)):
         if tiles[self.deeds[i].index].is_mortgaged == True:
            unmortgageable_property.append(self.deeds[i])
            
      return unmortgageable_property
   
   
   # build(target_tile : tiles) : void
      # add building to target_tile
      
   # sell(target_tile : tiles) : void
      # remove building from target_tile
   
   # buildable_property_list(self,board_tiles: list <tiles>) : dict <deeds> 
      # return dict of buildable properties with current houses and hotels
      
   # sellable_property_list(self,board_tiles: list <tiles>) : dict <deeds> 
      # return dict of buildable properties with current houses and hotels
   
   ## target_deed(self, index : int) : Deed
   # def target_deed(self, index): # maybe
   #    for i in range(len(self.deeds)):
   #       if self.deeds[i].index == index:
   #          return self.deeds[i]
   #    return 
   


   
