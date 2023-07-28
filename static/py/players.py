# players.py

###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Define monopoly player traits and actions
###

class Players:
   
   # --Global Data--
   # nickname : string # represents username of player in monopoly
   # character : string # represents the figure a player uses in game
   __player_number = int(0) # -__player_number : int
   __money = int(0) # -__money : int
   __location = int(0) # -__location : int
   location_name = "Go" # location : str
   has_rolled = False
   same_values_rolled = int(0) # doublesrolled : int

   in_jail = False  # +in_Jail : bool 
   time_jailed = int(0) # +time_jailded : int 
   jail_free_card = int(0) # +jail_free_card : int
   # owned_deeds = ["Reading Railroad","Baltic Ave","Boardwalk"] # 
   owned_deeds = [] # +owned_deeds : list <Deeds>
   owned_mortgages = [] # +owned_mortgages : list <Deeds> #maybe?
   total_houses = int(0) # +total_houses : int
   total_buildings = int(0) # +total_buildings : int
   bankrupt = False # +bankrupt : bool
   
   #--Contstructor--
   def __init__(self,startingTotal = 0, id_number = 0):
      self.__money = startingTotal
      self.__player_number = id_number
      
   #--Method Implementations--
   # player_assets(self) : void
   def player_status(self): 
      ###List Player Assets (static stats)
      # print("player number = "self.__player_number)
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
      print("\t\tproperties:",len(self.owned_deeds))
      for i in range(0,len(self.owned_deeds)):
         print("\t\t   -",self.owned_deeds[i]) #needs modification
      # print("\t\tmortgages :",len(self.owned_mortgages)) #maybe
      # for i in range(0,len(self.owned_mortgages)):
      #    print("\t\t   -",self.owned_mortgages[i])  #needs modification
      print("\t\ttotal houses =",self.total_houses)
      print("\t\ttotal hotels =",self.total_buildings)
      # print("\t\tbankrupt =",self.bankrupt)
      # print("\t\t")
      print("\t\t-----------------------------") 
      
   # player_number(self) : int
   def player_number(self):
      return int(self.__player_number)
   
   # move_location(next_location : int, location_text) : void
   def move_location(self,next_location, location_text): # new
      # print("move to location number",next_location)
      self.__location = next_location
      self.location_name = location_text
      print("\n\t\tplayer",self.__player_number,"location is ","\n\t\t["+str(self.__location)+"]",self.location_name)
      
   # current_location(self) : int
   def current_location(self):
      return self.__location
   
   # current_money(self) : void
   def current_money(self):
      return  self.__money   
   
   # recieve_money(self, amount : int) : void
   def receive_money(self,amount):
      self.__money += amount
      print("\t\tplayer",self.__player_number, "recieved $", amount)
   
   # pay_money(self, amount : int ) :  int
   def pay_money(self,amount):
      self.__money -= amount
      print("\t\tplayer",self.__player_number, "payed $", amount)
   
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
      print("\t\tplayer", self.__player_number,"location =", self.__location) 
      self.in_jail = True
      print("\t\tplayer",self.__player_number,"is now in jail")
      self.jail_counter = 0

   # get_property(contributor : string , property_value : int) : void
   # sell_property(property : int, reciever : string ) : int
   # mortgage_property() : void 
   # unmortgage_propety() : void
   # develop_building(property : int) : void
   # deconstruct_building(property : int) : void
   


   
