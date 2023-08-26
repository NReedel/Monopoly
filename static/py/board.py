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
   
	def tile_check(self,all_players): # new
			# tiles[i].tile_class
			#t_g_o = [brown,sky-blue,dark-orchid,orange,red,yellow,green,cobalt-blue]
			# owner_id = []
			# for i in range(0,len(all_players)):
			#    owner_id.append(all_players[i].id)
			has_mononopoly = [False,False,False,False,False,False,False,False]
			total_groups_owned = [[], [], [], [], [], [], [], []] # needs better name, ownnable_monopoly
			max_groups_value =  (2, 3, 3, 3, 3, 3, 3, 2) # max_monopoly_value
			railroad_owners = []		
			utility_owners = []

			# for i in range (len(all_players)):
			# 	utilities_owned.append(0
    
			# 2d array for indexes  # ?
			monopoly_property_index = [[1,3],[6,8,9],[11,13,14],[16,18,19],[21,23,24],[26,27,29],[31,32,34],[37,39]]
			# buildable_property = [] # tiles
			for i in range(0,len(self.tile)): # needs if(tile[i].hotels < 1)
				if self.tile[i].tile_type == "street" and self.tile[i].tile_class == "property prop-brown":
					total_groups_owned[0].append(self.tile[i].owned_by)
					# for j in range(0,len(total_groups_owned[0])):
					# 	print(total_groups_owned[0][j])
				if self.tile[i].tile_type == "street" and self.tile[i].tile_class == "property prop-sky-blue":
					total_groups_owned[1].append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "street" and self.tile[i].tile_class == "property prop-dark-orchid":
					total_groups_owned[2].append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "street" and self.tile[i].tile_class == "property prop-orange":
					total_groups_owned[3].append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "street" and self.tile[i].tile_class == "property prop-red":
					total_groups_owned[4].append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "street" and self.tile[i].tile_class == "property prop-yellow":
					total_groups_owned[5].append(self.tile[i].owned_by)  
				if self.tile[i].tile_type == "street" and self.tile[i].tile_class == "property prop-green":
					total_groups_owned[6].append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "street" and self.tile[i].tile_class == "property prop-cobalt-blue":
					total_groups_owned[7].append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "railroad":
					railroad_owners.append(self.tile[i].owned_by)
				if self.tile[i].tile_type == "utility":
					utility_owners.append(self.tile[i].owned_by)
			# railroad_index = [[],[],[],[]]
			multiplier = 0
			for i in range(0, len(all_players)):
				# railroad count
				for j in range(len(railroad_owners)):
					if all_players[i].id == railroad_owners[j]:
						multiplier += 1
				for j in range(len(railroad_owners)):
					if all_players[i].id == railroad_owners[j]:
						self.tile[(j*10)+5].multiplier = multiplier
				multiplier = 0
				# utility count
				for j in range(len(utility_owners)):
					if all_players[i].id == utility_owners[j]:
						multiplier += 1
				if all_players[i].id == utility_owners[0]:
					self.tile[12].multiplier = multiplier
				if all_players[i].id == utility_owners[1]:
					self.tile[28].multiplier = multiplier		
				multiplier = 0

			for i in range(0,len(total_groups_owned)):
				if len(total_groups_owned[i]) == 2 and (total_groups_owned[i][0] == total_groups_owned[i][1]):
					# has_monopoly[i] = True
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = True
						# print("\t"+str(monopoly_property_index[i][j]),"= true")
				elif len(total_groups_owned[i]) == 3 and (total_groups_owned[i][0] == total_groups_owned[i][1] and total_groups_owned[i][1] == total_groups_owned[i][2]):
					# has_monopoly[i] = True
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = True
						# print("\t"+str(monopoly_property_index[i][j]),"= true")
				else:
					# has_monopoly[i] = False
					for j in range(0,len(monopoly_property_index[i])):
						self.tile[monopoly_property_index[i][j]].has_monopoly = False
						# print("\t"+str(monopoly_property_index[i][j]),"= false")
	
	   # for i in range(0,len(total_groups_owned)):
		# 	if has_monopoly[i] == True:
		# 		for j in range(0,len(monopoly_property_index[i])):
		# 			self.tiles[monopoly_property_index[i][j]].has_monopoly
				

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
    
   
   
   
