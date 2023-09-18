###############################################################
# board.py
###############################################################

from . import tiles
from . import cards
from . import deck
import json
import os

###############################################################
class Board:
   
	tile = []
	community_chest = deck.Deck()
	chance = deck.Deck()
 
	# --Constructor--
	def __init__(self):
		with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'json', 'tiles.json'), 'r') as rf:
			for t in json.load(rf):
				if t['type'] == "street":
					self.tile.append(tiles.PropertyStreet(t))
				elif t['type'] == "railroad":
					self.tile.append(tiles.PropertyRailroad(t))
				elif t['type'] == "utility":
					self.tile.append(tiles.PropertyUtility(t))
				else: #tiles['type'] == "special":
					if(t['special'] == "card"):
						self.tile.append(tiles.TileCard(t))      
					if(t['special'] == "tax"):
						self.tile.append(tiles.TileTax(t))
					if(t['special'] == "corner"):
						self.tile.append(tiles.TileCorner(t))
      
		with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'json', 'community_chest.json'), 'r') as rf:
			for c in json.load(rf):
				self.community_chest.deck.append(cards.Cards(c))  
    
		with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'json', 'chance.json'), 'r') as rf:
			for c in json.load(rf):
				self.chance.deck.append(cards.Cards(c))
    
		self.chance.shuffle()
		self.community_chest.shuffle()
    
	# location(tile_index : int) : str
	def location(self,tile_index):
			return str(self.tile[tile_index].tile_name)
   
	def tile_check(self,all_players): 
			monopoly_group_total=  (2, 3, 3, 3, 3, 3, 3, 2)   
			monopoly_owner_groupings = [[], [], [], [], [], [], [], []] # needs better name, ownnable_monopoly
			railroad_owners = []		
			utility_owners = []
			monopoly_property_index = [[1,3],[6,8,9],[11,13,14],[16,18,19],[21,23,24],[26,27,29],[31,32,34],[37,39]]
   		### append tile group owners to their respective lists
			for i in range(0,len(self.tile)): 
				
				if self.tile[i].tile_type == "street":
					if self.tile[i].monopoly_type.value == 1: # "Monopoly.BROWN"
						monopoly_owner_groupings[0].append(self.tile[i].owned_by)
					if self.tile[i].monopoly_type.value == 2: # "Monopoly.CYAN"
						monopoly_owner_groupings[1].append(self.tile[i].owned_by)
					if self.tile[i].monopoly_type.value == 3: # "Monopoly.MAGENTA"
						monopoly_owner_groupings[2].append(self.tile[i].owned_by)
					if self.tile[i].monopoly_type.value == 4: # "Monopoly.ORANGE"
						monopoly_owner_groupings[3].append(self.tile[i].owned_by)
					if self.tile[i].monopoly_type.value == 5: # "Monopoly.RED"
						monopoly_owner_groupings[4].append(self.tile[i].owned_by)  
					if self.tile[i].monopoly_type.value == 6: # "Monopoly.YELLOW"
						monopoly_owner_groupings[5].append(self.tile[i].owned_by)
					if self.tile[i].monopoly_type.value == 7: # "Monopoly.GREEN"
						monopoly_owner_groupings[6].append(self.tile[i].owned_by)
					if self.tile[i].monopoly_type.value == 8: # "Monopoly.BLUE"
						monopoly_owner_groupings[7].append(self.tile[i].owned_by)
						
				if self.tile[i].tile_type == "railroad":
					railroad_owners.append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "utility":
					utility_owners.append(self.tile[i].owned_by)	
     
			### apply has_monopoly T/F status to all street tile
			for i in range(0,len(monopoly_owner_groupings)):
				
				if len(monopoly_owner_groupings[i]) == 2 and (monopoly_owner_groupings[i][0] == monopoly_owner_groupings[i][1]):
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = True
				elif len(monopoly_owner_groupings[i]) == 3 and (monopoly_owner_groupings[i][0] == monopoly_owner_groupings[i][1] and monopoly_owner_groupings[i][1] == monopoly_owner_groupings[i][2]):
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = True
				else:
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = False

   		#### apply multipliers to railroad and utilities
			multiplier = 0
			for i in range(0, len(all_players)): 
				### railroad count
				for j in range(len(railroad_owners)): # finds the multiplier for player who owns a railroad
					if all_players[i].id == railroad_owners[j]:
						multiplier += 1
				for j in range(len(railroad_owners)): # apply multiplier to each tile
					if all_players[i].id == railroad_owners[j]:
						self.tile[(j*10)+5].multiplier = multiplier
				multiplier = 0
				
				### utility count
				for j in range(len(utility_owners)): # finds the multiplier for player who owns a utility
					if all_players[i].id == utility_owners[j]:
						multiplier += 1
				if all_players[i].id == utility_owners[0]: # apply multiplier to electric company
					self.tile[12].multiplier = multiplier
				if all_players[i].id == utility_owners[1]: # apply mutiplier to water works
					self.tile[28].multiplier = multiplier		
				multiplier = 0      

###############################################################
