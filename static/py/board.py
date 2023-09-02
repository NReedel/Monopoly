###############################################################
# board.py
###############################################################
from tiles import *
from cards import *
from deck import *
import json

###############################################################

class Board:
   
   # --Data--
	tile = []
	community_chest = Deck()
	chance = Deck()
 
	# --Constructor--
	def __init__(self):
		# Load JSON here, use your own link 💬
		with open('/mnt/c/Users/Nreed/Code/All_Code/Monopoly/static/Json/tiles.json', 'r') as rf:
			# with open('tiles.json', 'r') as rf:
			for tiles in json.load(rf):
				if tiles['type'] == "street":
					self.tile.append(PropertyStreet(tiles))
				elif tiles['type'] == "railroad":
					self.tile.append(PropertyRailroad(tiles))
				elif tiles['type'] == "utility":
					self.tile.append(PropertyUtility(tiles))
				else: #tiles['type'] == "special":
					if(tiles['special'] == "card"):
						self.tile.append(TileCard(tiles))      
					if(tiles['special'] == "tax"):
						self.tile.append(TileTax(tiles))
					if(tiles['special'] == "corner"):
						self.tile.append(TileCorner(tiles))
      
		with open('/mnt/c/Users/Nreed/Code/All_Code/Monopoly/static/Json/community_chest.json', 'r') as rf:
			for cards in json.load(rf):
				self.community_chest.deck.append(Cards(cards))  
    
		with open('/mnt/c/Users/Nreed/Code/All_Code/Monopoly/static/Json/chance.json', 'r') as rf:
			for cards in json.load(rf):
				self.chance.deck.append(Cards(cards))
    
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
					if str(self.tile[i].monopoly_type) == "Monopoly.BROWN":
						monopoly_owner_groupings[0].append(self.tile[i].owned_by)
					if str(self.tile[i].monopoly_type) == "Monopoly.CYAN":
						monopoly_owner_groupings[1].append(self.tile[i].owned_by)
					if str(self.tile[i].monopoly_type) == "Monopoly.MAGENTA":
						monopoly_owner_groupings[2].append(self.tile[i].owned_by)
					if str(self.tile[i].monopoly_type) == "Monopoly.ORANGE":
						monopoly_owner_groupings[3].append(self.tile[i].owned_by)
					if str(self.tile[i].monopoly_type) == "Monopoly.RED":
						monopoly_owner_groupings[4].append(self.tile[i].owned_by)  
					if str(self.tile[i].monopoly_type) == "Monopoly.YELLOW":
						monopoly_owner_groupings[5].append(self.tile[i].owned_by)
					if str(self.tile[i].monopoly_type) == "Monopoly.GREEN":
						monopoly_owner_groupings[6].append(self.tile[i].owned_by)
					if str(self.tile[i].monopoly_type) == "Monopoly.BLUE":
						monopoly_owner_groupings[7].append(self.tile[i].owned_by)
						
				if self.tile[i].tile_type == "railroad":
					railroad_owners.append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "utility":
					utility_owners.append(self.tile[i].owned_by)	
     
			### apply has_monopoly T/F status to all street tile
			for i in range(0,len(monopoly_owner_groupings)):
				
				if len(monopoly_owner_groupings[i]) == 2 and (monopoly_owner_groupings[i][0] == monopoly_owner_groupings[i][1]):
					# has_monopoly[i] = True
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = True
						# print("\t"+str(monopoly_property_index[i][j]),"= true")
				elif len(monopoly_owner_groupings[i]) == 3 and (monopoly_owner_groupings[i][0] == monopoly_owner_groupings[i][1] and monopoly_owner_groupings[i][1] == monopoly_owner_groupings[i][2]):
					# has_monopoly[i] = True
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = True
						# print("\t"+str(monopoly_property_index[i][j]),"= true")
				else:
					# has_monopoly[i] = False
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = False
						# print("\t"+str(monopoly_property_index[i][j]),"= false")
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

		# # Quick test function
		# def print_board(self):
		# 	for t in self.tiles:
		# 		print("\tTile.tile_id: ", t.tile_id)


		# # May need later when rendering front-end elements
		# def render_board():
		# 	pass

###############################################################


# owner(current_players : Player) : str  
# def owner(current_players)  
    
   
   
   
