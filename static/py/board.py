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
		# Load JSON here, use your own link if outside working directory 💬
		with open('tiles.json', 'r') as rf:
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

		with open('community_chest.json', 'r') as rf:
			for cards in json.load(rf):
				self.community_chest.deck.append(Cards(cards))

		with open('chance.json', 'r') as rf:
			for cards in json.load(rf):
				self.chance.deck.append(Cards(cards))

		self.chance.shuffle()
		self.community_chest.shuffle()
    
	# location(tile_index : int) : str
	def location(self,tile_index):
		return str(self.tile[tile_index].name)
				
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
    
