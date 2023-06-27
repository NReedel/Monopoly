###############################################################
# cards.py
###############################################################

from enum import Enum

###############################################################

class CardType(Enum):
    CHANCE       = 1
    COMMUNITY	 = 2
    NONE		 = 3

###############################################################

class Card():

	# Will need to add a dictionary parameter for JSON initialization ⚠
	def __init__(self, index):

		self.card_id = index
		self.type = CardType.NONE
		self.card_text = ""

		self.event = None  			# ⚠
		self.is_ownable = False		# Get out of jail free card


	def render_html():
		pass
		

###############################################################
