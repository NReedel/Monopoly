###############################################################
# board.py
###############################################################

from tiles import Tile

# from deeds import Deed ⚠
# from bank import Bank ⚠

###############################################################

class Board:
	
	def __init__(self):
		
		self.tiles = []

		# Load JSON here 💬

		for t in range(40):
			self.tiles.append(Tile(t))
			# Bank.deeds.append(Deed(t)) ⚠
			'''
				Will need Tile and Deed 
				to accept a dictionary as an argument
				to initialize their members
			'''

	# Quick test function
	def print_board(self):
		for t in self.tiles:
			print("\tTile.tile_id: ", t.tile_id)


	# May need later when rendering front-end elements
	def render_board():
		pass

###############################################################
