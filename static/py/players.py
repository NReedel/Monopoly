#players.py
###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Define monopoly player traits and actions
###

class players:
   # --Global Data--
   # nickname : string //represents username of player in monopoly
   # character : string //represents the figure a player uses in game
   _player_number = int(0) # -_player_number : int
   _location = 0 # -_location : int
   _money = int(0) # -_money : int
   doubles_rolled = int(0) # doublesrolled : int
   deeds = [] # +deeds : list <int>
   mortgages = [] # +mortgages : list <int>
   # +buildings : list <int>
   in_jail = False # +in_Jail : bool #new
   _bankrupt = False # -bankrupt : bool
   time_jailed = 0 # +time_jailded : int #new
   jail_free_card = 1 # +jail_free_card : int
   
   #--Contstructor--
   def __init__(self,startingTotal=5000, id_number=0):
      self._money = startingTotal
      self._player_number = id_number
      
   #--Method Implementation--
   # player_number(self) : int
   def player_number(self):
      return int(self._player_number)
   
   # move_location(location : int) : void
   def move_location(self,next_location):
      # print("move to location number",next_location)
      self._location = next_location
      print("\t\tplayer",self._player_number,"location now = ",self._location)
      
   # current_location(self) : int
   def current_location(self):
      return self._location
   
   # current_money(self) : void
   def current_money(self):
      return  self._money   
   
   # receive_money(self, amount : int) : void
   def receive_money(self,amount):
      self._money += amount
      print("\t\tplayer",self._player_number, "recieved $", amount)
      
   # pay_money(self, amount : int ) :  int
   def pay_money(self,amount):
      self._money -= amount
      print("\t\tplayer",self._player_number, "payed $", amount)
      return amount

   # change_balance(self, new_total : int) : void
   def change_balance(self, new_total):
       """ Sets the total amount of money held by the player equal to the new total parameter """
       self._money = new_total
   
   # def inDebt(self) : bool
   def in_debt(self) :
      if self._money < 0:
         return True
      return False
   
   # rolled_doubles(die1 : int, die2 : int) : bool
   def rolled_doubles(self,die1 = 0, die2 = 0):
      if die1 == die2:
         self.doubles_rolled == self.doubles_rolled + 1
         return True
      return False
      

   # get_property(contributor : string , property_value : int) : void
   # sell_property(property : int, reciever : string ) : int
   # mortgage_property() : void 
   # develop_building(property : int) : void
   # deconstruct_building(property : int) : void
   # bid() : void 
   
   # go_to_Jail() : void
   def go_to_jail(self): #new
      self._location = 9
      print("\t\tplayer", self._player_number,"location = ", self._location) 
      self.in_jail = True
      print("\t\tplayer",self._player_number,"is now in jail")
      jail_counter = 0
   # self.doubles_rolled = 0
   # get_out_of_Jail() : void
   
   # declare_bankruptcy() : void
   def declare_bankruptcy(self):
      self._bankrupt = True
      
   # is_bankrupt() : bool
   def is_bankrupt(self):
      return bool(self._bankrupt)   
