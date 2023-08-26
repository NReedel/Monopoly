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
   total_hotels = int(0) # +total_hotels : int
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
            tile_status += "(m) "
         if(owned_tile.tile_type == "street" and owned_tile.has_monopoly == True): # new
            tile_status += "(M) "  
         if(owned_tile.tile_type == "railroad"):# new # needs update 
            tile_status += "(*"+str(owned_tile.multiplier)+")" 
         if(owned_tile.tile_type == "utility"): # new # needs update    
            tile_status += "(*"+str(owned_tile.multiplier)+")" 
         if(owned_tile.tile_type == "street" and owned_tile.houses > 0 and owned_tile.hotels < 1) :
            tile_status += "h = " + str(owned_tile.houses) + " "
         if(owned_tile.tile_type == "street" and owned_tile.hotels > 0) :
            tile_status += "H = " + str(owned_tile.hotels) + " "               
         print("\t\t   -",self.deeds[i].name,tile_status)
         tile_status = ""
         
      # print("\t\tmortgages :",len(self.owned_mortgages)) #maybe
      # for i in range(0,len(self.owned_mortgages)):
      #    print("\t\t   -",self.owned_mortgages[i])  #needs modification
      print("\t\ttotal houses =",self.total_houses)
      print("\t\ttotal hotels =",self.total_hotels)
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
   
   # might simplify and by using monopoly check to board class 
   # buildable_property_list(self,board_tiles: list <tiles>) : list <deeds> 
   def buildable_property_list(self, tiles): # new
      # tiles[i].tile_class
      #t_g_o = [brown,sky-blue,dark-orchid,orange,red,yellow,green,cobalt-blue]
      total_groups_owned = [0, 0, 0, 0, 0, 0, 0, 0]
      max_groups_value =  (2, 3, 3, 3, 3, 3, 3, 2)
      # 2d array for indexes  # ?
      buildable_property_index = [[1,3],[6,8,9],[11,13,14],[16,18,19],[21,23,24],[26,27,29],[31,32,34],[37,39]]
      buildable_property = [] # tiles
      for i in range(0,len(tiles)): 
         if(tiles[i].owned_by == self.id and tiles[i].tile_class == "property prop-brown"):
            total_groups_owned[0] += 1
            if total_groups_owned[0] == max_groups_value[0]:
               for j in range(0,len(buildable_property_index[0])):
                  if tiles[buildable_property_index[0][j]].hotels == 0:
                     buildable_property.append(self.target_deed(buildable_property_index[0][j]))
         if(tiles[i].owned_by == self.id and tiles[i].tile_class == "property prop-sky-blue"):
            total_groups_owned[1] += 1
            if total_groups_owned[1] == max_groups_value[1]:
               for j in range(0,len(buildable_property_index[1])):
                  if tiles[buildable_property_index[1][j]].hotels == 0:
                     # print(buildable_property_index[1][j],"h =",tiles[buildable_property_index[1][j]].houses)
                     buildable_property.append(self.target_deed(buildable_property_index[1][j]))       
         if(tiles[i].owned_by == self.id and tiles[i].tile_class == "property prop-dark-orchid"):
            total_groups_owned[2] += 1
            if total_groups_owned[2] == max_groups_value[2]:
               for j in range(0,len(buildable_property_index[2])):
                  if tiles[buildable_property_index[2][j]].hotels == 0:
                     buildable_property.append(self.target_deed(buildable_property_index[2][j]))  
         if(tiles[i].owned_by == self.id and tiles[i].tile_class == "property prop-orange"):
            total_groups_owned[3] += 1
            if total_groups_owned[3] == max_groups_value[3]:
               for j in range(0,len(buildable_property_index[3])):
                  if tiles[buildable_property_index[3][j]].hotels == 0:
                     buildable_property.append(self.target_deed(buildable_property_index[3][j]))  
         if(tiles[i].owned_by == self.id and tiles[i].tile_class == "property prop-red"):
            total_groups_owned[4] += 1
            if total_groups_owned[4] == max_groups_value[4]:
               for j in range(0,len(buildable_property_index[4])):
                  if tiles[buildable_property_index[4][j]].hotels == 0:
                     buildable_property.append(self.target_deed(buildable_property_index[4][j]))  
         if(tiles[i].owned_by == self.id and tiles[i].tile_class == "property prop-yellow"):
            total_groups_owned[5] += 1 
            if total_groups_owned[5] == max_groups_value[5]:
               for j in range(0,len(buildable_property_index[5])):
                  if tiles[buildable_property_index[5][j]].hotels == 0:
                     buildable_property.append(self.target_deed(buildable_property_index[5][j]))  
         if(tiles[i].owned_by == self.id and tiles[i].tile_class == "property prop-green"):
            total_groups_owned[6] += 1
            if total_groups_owned[6] == max_groups_value[6]:
               for j in range(0,len(buildable_property_index[6])):
                  if tiles[buildable_property_index[6][j]].hotels == 0:
                     buildable_property.append(self.target_deed(buildable_property_index[6][j]))  
         if(tiles[i].owned_by == self.id and tiles[i].tile_class == "property prop-cobalt-blue"):
            # print(i,tiles[i].tile_class)
            total_groups_owned[7] += 1  
            if total_groups_owned[7] == max_groups_value[7]:
               for j in range(0,len(buildable_property_index[7])):
                  if tiles[buildable_property_index[7][j]].hotels == 0:
                     buildable_property.append(self.target_deed(buildable_property_index[7][j]))  
      return buildable_property      
        
   # sellable_property_list(self,board_tiles: list <tiles>) : list <deeds> 
   def sellable_property_list(self,tiles):
      # tiles[i].tile_class
      sellable_property = [] # deeds
      for i in range(0,len(self.deeds)):
         if tiles[self.deeds[i].index].tile_type == "street":
            if tiles[self.deeds[i].index].hotels > 0 or tiles[self.deeds[i].index].houses > 0:
               sellable_property.append(self.deeds[i])
      return sellable_property
   
   ## target_deed(self, index : int) : Deed
   def target_deed(self, index): # new
      for i in range(len(self.deeds)):
         if self.deeds[i].index == index:
            return self.deeds[i]
      return 
   


   
