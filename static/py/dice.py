###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   Define monopoly dice
###

#--import--
import random
class Dice:
   
   #--Constructor--
   def __init__(self, starting_quantity = 2, starting_sides = 6): 
      self.quantity = starting_quantity
      self.sides = starting_sides
      self.all_dice = []
      for i in range(0,self.quantity):
         self.all_dice.append(int(0))
         
   #--Method Implementations--
   # roll(self) : void
   def roll(self): 
      for i in range(0,len(self.all_dice)):
         self.all_dice[i] = random.randint(1,self.sides)

   # print_roll(self) : void
   def print_roll(self):
      values = "" 
      for i in range(0,len(self.all_dice)):
         values += str(self.all_dice[i])
         values += " "
      return values
   
   # total_rolled(self) : int
   def total_rolled(self):
      total_rolled = 0
      
      for i in range(0,self.quantity):
         total_rolled += self.all_dice[i]
      
      return total_rolled
   
   # rolled_same_values(self) : bool
   def rolled_same_values(self):
      value = self.all_dice[0]
      for i in range(1,len(self.all_dice)):
         if value != self.all_dice[i]:
            return False
      return True

   # target_die_value(self, target : int) : return int
   def target_die_value(self, target = int(0) ):
      if int(target) < len(self.all_dice) and int(target) >= 0:
         return int(self.all_dice[target])
      return 0

   

         
            