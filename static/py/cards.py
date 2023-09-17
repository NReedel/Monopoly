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
from . import card_events

###############################################################

# (personal note) all cards have virtually identical attributes, so a hierarchy would be unnecessary. Hence, enums
# But then why do we need enums here? What purpose do they serve?
# Maybe these will be used for display purposes?
# Personal Reminder: event_name is used for most ctor arguments for card events, not just for storing the string. LEAVE IT IN.
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
			self.event_name = "payStaticAmount"
			self.card_event = card_events.PayStaticAmount(self.event_name, card[self.event_name])

		# card event: receive a flat amount of money from the bank
		elif (card.get('receiveStaticAmount') != None):
			self.event_name = "receiveStaticAmount"
			self.card_event = card_events.ReceiveStaticAmount(self.event_name, card[self.event_name])

		# card event: pay money to each player
		elif (card.get('payPlayerRateAmount') != None):
			self.event_name = "payPlayerRateAmount"
			self.card_event = card_events.PayPlayerRateAmount(self.event_name, card[self.event_name])

		# card event: receive money from each player
		elif (card.get('receivePlayerRateAmount') != None):
			self.event_name = "receivePlayerRateAmount"
			self.card_event = card_events.ReceivePlayerRateAmount(self.event_name, card[self.event_name])

		# card event: pay money per owned house and hotel to the bank
		elif (card.get('payHouseRateAmount') != None and
			  card.get('payHotelRateAmount') != None):
			self.event_name = "payBuildingRateAmount"
			self.card_event = card_events.PayBuildingRateAmount(self.event_name, card['payHouseRateAmount'], card['payHotelRateAmount'])
			
		# card event: move to the specified tile
		elif (card.get('moveToIndex') != None):
			self.event_name = "moveToIndex"
			self.card_event = card_events.MoveToIndex(self.event_name, card[self.event_name])

		# card event: move to the nearest specified tile and pay a specified rent rate
		elif (card.get('moveToNearest') != None and
			  card.get('cardRentMultiplier') != None):
			self.event_name = "moveToNearest"
			if (card['moveToNearest'] == "Utility"):
				self.isMoveToUtility = True
				self.card_event = card_events.MoveToNearestUtility(self.event_name, card[self.event_name], card['cardRentMultiplier'])
			elif (card['moveToNearest'] == "Railroad"):
				self.isMoveToRailroad = True
				self.card_event = card_events.MoveToNearestRailroad(self.event_name, card[self.event_name], card['cardRentMultiplier'])
			else:
				self.isMoveToUtility = False
				self.isMoveToRailroad = False
				print("Invalid moveToNearest card type in json; neither Railroad nor Utility")

		# card event: move the specified number of tiles (forward or backward)
		elif (card.get('moveSpaces') != None):
			self.event_name = "moveSpaces"
			self.card_event = card_events.MoveSpaces(self.event_name, card[self.event_name])
			
		# card event: receive a Get Out of Jail Free (GOJF) card
		elif (card.get('isGOJF') != None):
			self.event_name = "isGOJF"
			self.card_event = card_events.GetOutOfJailFree(self.event_name, card[self.event_name])


	def render_html():
		pass
		

###############################################################
