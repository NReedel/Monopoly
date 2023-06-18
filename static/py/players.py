# players.py
###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Define monopoly player traits and actions
###

class players:
   
   # --Global Data--
   # nickname : string # represents username of player in monopoly
   # character : string # represents the figure a player uses in game
   __player_number = int(0) # -__player_number : int
   __money = int(0) # -__money : int
   __location = 0 # -__location : int
   has_rolled = False
   doubles_rolled = int(0) # doublesrolled : int
   in_jail = False # +in_Jail : bool 
   time_jailed = int(0) # +time_jailded : int 
   jail_free_card = int(0) # +jail_free_card : int
   owned_deeds = [] # +owned_deeds : list <Deeds>
   # owned_deeds = ["Baltic Ave.","Boardwalk"] #example version
   # owned_mortgages = [] # +owned_mortgages : list <Deeds> #maybe?
   total_houses = int(0) # +total_houses : int
   total_buildings = int(0) # +total_buildings : int
   bankrupt = False # +bankrupt : bool
   
   #--Contstructor--
   def __init__(self,startingTotal = 0, id_number = 0):
      self.__money = startingTotal
      self.__player_number = id_number
      
   #--Method Implementations--
   # player_assets( target_player : player ) : void
   def player_status(self): 
      ###List Player Assets (static stats)
      # print("player number = "self.__player_number)
      # print("player character = "self.character)
      print("\t\tmoney = $",self.current_money())
      print("\t\tin debt =",self.in_debt())
      print("\t\tlocation =",self.current_location())
      print("\t\tdoubles rolled =",self.doubles_rolled )
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
   
   # move_location(location : int) : void
   def move_location(self,next_location):
      # print("move to location number",next_location)
      self.__location = next_location
      print("\t\tplayer",self.__player_number,"location now =",self.__location)
      
   # current_location(self) : int
   def current_location(self):
      return self.__location
   
   # current_money(self) : void
   def current_money(self):
      return  self.__money   
   
   # recieve_money(self, amount : int) : void
   def recieve_money(self,amount):
      self.__money += amount
      print("\t\tplayer",self.__player_number, "recieved $", amount)
      
   # pay_money(self, amount : int ) :  int
   def pay_money(self,amount):
      self.__money -= amount
      print("\t\tplayer",self.__player_number, "payed $", amount)
      return amount
   
   # def inDebt(self) : bool
   def in_debt(self) :
      if self.__money < 0:
         return True
      return False
   
   # rolled_doubles(die1 : int, die2 : int) : bool
   def rolled_doubles(self,die1 = 0, die2 = 0):
      if die1 == die2:
         self.doubles_rolled == self.doubles_rolled + 1
         return True
      return False
   
   # go_to_Jail() : void
   def go_to_jail(self): 
      self.__location = 9
      print("\t\tplayer", self.__player_number,"location = ", self.__location) 
      self.in_jail = True
      print("\t\tplayer",self.__player_number,"is now in jail")
      self.jail_counter = 0

   # get_property(contributor : string , property_value : int) : void
   # sell_property(property : int, reciever : string ) : int
   # mortgage_property() : void 
   # unmortgage_propety() : void
   # develop_building(property : int) : void
   # deconstruct_building(property : int) : void
   


   


   
