###############################################################
# board.py
###############################################################
from tiles import *
from board_tiles import *
from cards import *
import json
# from deeds import Deed ⚠
# from bank import Bank ⚠

###############################################################
class Board:
   
      # --Data--
	tile = []
	community_chest = []
	chance = []
 
	# --Constructor--
	def __init__(self):
		# Load JSON here, use your own link if outside working directory 💬
		with open('tiles.json', 'r') as rf:
			for tiles in json.load(rf):
				if tiles['type'] == "street":
					self.tile.append(StreetBoardTiles(tiles))
				elif tiles['type'] == "railroad":
					self.tile.append(RailRoadBoardTiles(tiles))
				elif tiles['type'] == "utility":
					self.tile.append(UtilityBoardTiles(tiles))
				else: #tiles['type'] == "special":
					self.tile.append(SpecialBoardTiles(tiles))

		with open('community_chest.json', 'r') as rf:
			for cards in json.load(rf):
				self.community_chest.append(Cards(cards))

		with open('chance.json', 'r') as rf:
			for cards in json.load(rf):
				self.chance.append(Cards(cards))
    
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
    
