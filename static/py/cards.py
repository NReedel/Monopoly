###############################################################
# cards.py
###############################################################

###
# *Name:    Alicyn Knapp, Chris Schneider
# *Credit:  PennWest Projects! (discord server)
# *Purpose: Define Monopoly card attributes and actions
###

# from asyncio.windows_events import NULL
from enum import Enum
from card_events import *

###############################################################

class CardType(Enum):
    CHANCE = 1
    CHEST = 2
    NONE = 3
	
###############################################################

class Cards:
	def __init__(self, card):
		''' All cards are initialized with json in board.py constructor '''

		self.index = card['index']

		# initialize with enum based on type
		if card['type'] == "Chance":
			self.type = CardType.CHANCE
		elif card['type'] == "Community Chest":
			self.type = CardType.CHEST
		else:
			self.type = CardType.NONE
			
		self.title = card['title']
		self.image = card['image']
		self.description = card['description']

		# card event: pay a flat amount of money to the bank
		if (card.get('payStaticAmount') != None):
			self.event = "payStaticAmount"
			self.card_event = PayStaticAmount(self.event, card[self.event])

		# card event: receive a flat amount of money from the bank
		elif (card.get('receiveStaticAmount') != None):
			self.event = "receiveStaticAmount"
			self.card_event = ReceiveStaticAmount(self.event, card[self.event])

		# card event: pay money to each player
		elif (card.get('payPlayerRateAmount') != None):
			self.event = "payPlayerRateAmount"
			self.pay_player_rate = card[self.event]

		# card event: receive money from each player
		elif (card.get('receivePlayerRateAmount') != None):
			self.event = "receivePlayerRateAmount"
			self.receive_player_rate = card[self.event]

		# card event: pay money per owned house and hotel to the bank
		elif (card.get('payHouseRateAmount') != None and
			  card.get('payHotelRateAmount') != None):
			self.event = "payBuildingRateAmount"
			self.payHouseRate = card['payHouseRateAmount']
			self.payHotelRate = card['payHotelRateAmount']

		# card event: move to the specified tile OR move backwards three spaces
		elif (card.get('moveTo') != None):
			if (card.get('moveTo') >= 0):
				self.event = "move"
				self.move_to = card['moveTo']
			else:
				self.event = "reverseMove"
				self.reverse_move = card['moveTo']

		# card event: move to the nearest specified tile and pay a specified rent rate
		elif (card.get('cardRentMultiplier') != None and
			  card.get('moveToNearest') != None):
			self.event = "moveToNearest"
			self.tile_type = card['moveToNearest']
			self.card_rent_multiplier = card['cardRentMultiplier']

		# card event: receive a GOJF card
		elif (card.get('isGOJF') != None):
			self.is_ownable = card['isGOJF']


	def render_html():
		pass
		

###############################################################
