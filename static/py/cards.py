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
			
		self.subtype = card['subtype']
			
		self.title = card['title']
		self.image = card['image']
		self.description = card['description']
		
		self.event_name = card['eventName']
		
		match self.event_name:
			case card_events.Name.PAY_STATIC:	# card event: pay a flat amount of money to the bank
				self.card_event = card_events.PayStaticAmount(self.event_name, card[self.event_name])
				
			case card_events.Name.RECEIVE_STATIC:	# card event: receive a flat amount of money from the bank
				self.card_event = card_events.ReceiveStaticAmount(self.event_name, card[self.event_name])
				
			case card_events.Name.PAY_PLAYERS:	# card event: pay money to each player
				self.card_event = card_events.PayPlayerRateAmount(self.event_name, card[self.event_name])
				
			case card_events.Name.PAY_BUILDINGS:	# card event: pay money per owned house and hotel to the bank
				self.card_event = card_events.PayBuildingRateAmount(self.event_name, card['payHouseRateAmount'], card['payHotelRateAmount'])
				
			case card_events.Name.RECEIVE_PLAYERS:	# card event: receive money from each player
				self.card_event = card_events.ReceivePlayerRateAmount(self.event_name, card[self.event_name])
				
			case card_events.Name.MOVE_INDEX:	# card event: move to the specified tile
				self.card_event = card_events.MoveToIndex(self.event_name, card[self.event_name])
				
			case card_events.Name.MOVE_NEAREST:	# card event: move to the nearest specified tile and pay a specified rent rate
				if (card[card_events.Name.MOVE_NEAREST] == "Utility"):
					self.isMoveToUtility = True
					self.card_event = card_events.MoveToNearestUtility(self.event_name, card[self.event_name], card['cardRentMultiplier'])
				elif (card[card_events.Name.MOVE_NEAREST] == "Railroad"):
					self.isMoveToUtility = False
					self.card_event = card_events.MoveToNearestRailroad(self.event_name, card[self.event_name], card['cardRentMultiplier'])
				else:
					self.isMoveToUtility = False
					print("Invalid moveToNearest card type in json; neither Railroad nor Utility")
				
			case card_events.Name.MOVE_SPACES:	# card event: move the specified number of tiles (forward or backward)
				self.card_event = card_events.MoveSpaces(self.event_name, card[self.event_name])
				
			case card_events.Name.GOJF:	# card event: receive a Get Out of Jail Free (GOJF) card
				self.card_event = card_events.GetOutOfJailFree(self.event_name, card[self.event_name])
				
			case _:
				print(f"No corresponding event with the event name {self.event_name}.")


	def render_html():
		pass
		

###############################################################