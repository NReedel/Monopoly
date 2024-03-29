###############################################################
# card_events.py
###############################################################

###
# *Name:    Alicyn Knapp
# *Credit:  PennWest Projects! (discord server)
# *Purpose: Define Monopoly card events attributes and actions
###

from enum import *

###############################################################
'''
CardEvents
├── StaticMoneyEvents
│   ├── PayStaticAmount
│   └── ReceiveStaticAmount
├── RateMoneyEvents
│   ├── PayRateAmount
│   │   ├── PayPlayerRateAmount
│   │   └── PayBuildingRateAmount
│   └── ReceiveRateAmount
│       └── ReceivePlayerRateAmount
├── MovePlayerEvents
│   ├── MoveToIndex
│   ├── MoveToNearest
│   │   ├── MoveToNearestUtility
│   │   └── MoveToNearestRailroad
│   └── MoveSpaces	# Also used for reverse movement by a number of tiles
└── OwnableCardEvents
    └── GetOutOfJailFree

'''
###############################################################

class Name(str, Enum):
    PAY_STATIC = "payStaticAmount"
    RECEIVE_STATIC = "receiveStaticAmount"
    PAY_PLAYERS = "payPlayerRateAmount"
    PAY_BUILDINGS = "payBuildingRateAmount"
    RECEIVE_PLAYERS = "receivePlayerRateAmount"
    MOVE_INDEX = "moveToIndex"
    MOVE_NEAREST = "moveToNearest"
    MOVE_SPACES = "moveSpaces"
    GOJF = "isGOJF"
    NONE = "none"

###############################################################

class CardEvents:
    def __init__(self, event_name):
        self.event_name = event_name
        self.action_text = ""
        self.action_attribute = ""
        self.optional_verbage = ""
        
    # print_event_action(self, action : string, action_attribute : T, optional_verbage : string) : void
    def print_event_action(self, action_text, action_attribute, optional_verbage = ""):
        print(f"\t\t{action_text}{action_attribute}{optional_verbage}.")
        print("")

'''
├── StaticMoneyEvents
│   ├── PayStaticAmount
│   └── ReceiveStaticAmount
'''
class StaticMoneyEvents(CardEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name)
        self.static_money_amount = event_value

class PayStaticAmount(StaticMoneyEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.action_text = "Paid $"
        
    # pay_money(self, current_balance : int) : int
    def pay_money(self, current_balance):
        ''' Takes player's current balance and returns the subtraction of the money paid '''
        self.print_event_action(self.action_text, self.static_money_amount)
        return current_balance - self.static_money_amount


class ReceiveStaticAmount(StaticMoneyEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.action_text = "Received $"
        
    # receive_money(self, current_balance : int) : int
    def receive_money(self, current_balance):
        ''' Takes player's current balance and returns the addition of the money received '''
        self.print_event_action(self.action_text, self.static_money_amount)
        return current_balance + self.static_money_amount


'''
├── RateMoneyEvents
│   ├── PayRateAmount
│   │   ├── PayPlayerRateAmount
│   │   └── PayBuildingRateAmount
│   └── ReceiveRateAmount
│       └── ReceivePlayerRateAmount
'''
class RateMoneyEvents(CardEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name)
        self.rate_money_amount = event_value


class PayRateAmount(RateMoneyEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.action_text = "Paid $"


class PayPlayerRateAmount(PayRateAmount):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        
    # pay_money(self, current_balance : int, player_count : int) : int
    def pay_money(self, current_balance, player_count):
        ''' Takes player's current balance and number of players and returns the subtraction of their total amount paid '''
        self.total_money_paid = self.rate_money_amount * (player_count - 1)  # excludes current player
        self.print_event_action(self.action_text, self.total_money_paid)
        return current_balance - self.total_money_paid
    
    # receive_owed_amount(self, other_player_balance : int) : int
    def receive_owed_amount(self, other_player_balance):
        ''' Takes balance of players who are receiving money and returns the addition of their owed rate '''
        return other_player_balance + self.rate_money_amount


class PayBuildingRateAmount(PayRateAmount):
    def __init__(self, event_name, event_value, second_event_value):
        super().__init__(event_name, event_value)
        self.hotel_rate_money_amount = second_event_value  # houses are listed first in json and thus loaded into the original event_value
        
    # pay_money(self, current_balance : int, house_count : int, hotel_count : int) : int
    def pay_money(self, current_balance, house_count, hotel_count):
        ''' Takes player's current balance and number of players and returns the subtraction of their total amount paid '''
        self.total_money_paid = (self.rate_money_amount * house_count) + (self.hotel_rate_money_amount * hotel_count)
        self.print_event_action(self.action_text, self.total_money_paid)
        return current_balance - self.total_money_paid


class ReceiveRateAmount(RateMoneyEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.action_text = "Received $"


class ReceivePlayerRateAmount(ReceiveRateAmount):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        
    # receive_money(self, current_balance : int, player_count : int) : int
    def receive_money(self, current_balance, player_count):
        ''' Takes player's current balance and number of players and returns the addition of their total amount received '''
        self.total_money_received = self.rate_money_amount * (player_count - 1)  # excludes current player
        self.print_event_action(self.action_text, self.total_money_received)
        return current_balance + self.total_money_received
    
    # pay_owed_amount(self, other_player_balance : int) : int
    def pay_owed_amount(self, other_player_balance):
        ''' Takes balance of players who are paying money and returns the subtraction of their paid rate '''
        return other_player_balance - self.rate_money_amount

'''
├── MovePlayerEvents
│   ├── MoveToIndex
│   ├── MoveToNearest
│   │   ├── MoveToNearestUtility
│   │   └── MoveToNearestRailroad
│   └── MoveSpaces	# Also used for reverse movement by a number of tiles
'''
class MovePlayerEvents(CardEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name)
        self.move = event_value
        self.action_text = "Moved "
        

class MoveToIndex(MovePlayerEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.action_text = "Moved to tile at index "

    # move_to_index(self) : int
    def move_to_index(self):
        ''' Returns the index that the player must move to '''
        self.print_event_action(self.action_text, self.move)
        return self.move

    
class MoveToNearest(MovePlayerEvents):
    def __init__(self, event_name, event_value, second_event_value):
        super().__init__(event_name, event_value)
        self.action_text = "Moved to nearest "
        self.rent_multiplier = second_event_value
        self.nearest_tile_index = int(0)
        

class MoveToNearestUtility(MoveToNearest):
    def __init__(self, event_name, event_value, second_event_value):
        super().__init__(event_name, event_value, second_event_value)

    # move_to_index(self, current_location : int) : int
    def move_to_nearest_utility(self, current_location):
        ''' Returns the index of the nearest utility that the player must move to '''
        if (self.move == "Utility"):
            if (current_location >= 28 or current_location < 12):
                # if current_location >= 28, make sure all pass GO criteria are being fulfilled
                self.nearest_tile_index = 12
            elif (current_location >= 12 and current_location < 28):
                self.nearest_tile_index = 28
                
            self.print_event_action(self.action_text, self.move)
        else:
            print("\t\tInvalid move_to value in Utility. Cannot move player.")
        return self.nearest_tile_index

    # pay_card_rent(self, dice_roll : int) : int
    def get_adjusted_rent(self, dice_roll):
        ''' Calculates the new rent based on the rent multiplier and the dice roll '''
        return dice_roll * self.rent_multiplier


class MoveToNearestRailroad(MoveToNearest):
    def __init__(self, event_name, event_value, second_event_value):
        super().__init__(event_name, event_value, second_event_value)

    # move_to_index(self, current_location : int) : int
    def move_to_nearest_railroad(self, current_location):
        ''' Returns the index of the nearest railroad that the player must move to '''
        if (self.move == "Railroad"):
            if (current_location >= 35 or current_location < 5):
                # if current_location >= 35, make sure all pass GO criteria are being fulfilled
                self.nearest_tile_index = 5
            elif(current_location >= 5 and current_location < 15):
                self.nearest_tile_index = 15
            elif(current_location >= 15 and current_location < 25):
                self.nearest_tile_index = 25
            elif (current_location >= 25 and current_location < 35):
                self.nearest_tile_index = 35
                
            self.print_event_action(self.action_text, self.move)
        else:
            print("\t\tInvalid move_to value in Railroad. Cannot move player.")
        return self.nearest_tile_index

    # pay_card_rent(self, normal_rent_amount : int) : int
    def get_adjusted_rent(self, normal_rent_amount):
        ''' Calculates the new rent based on the rent multiplier and the normal rent owed '''
        return normal_rent_amount * self.rent_multiplier


class MoveSpaces(MovePlayerEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.isReverseMove = bool(self.move < 0)
        self.new_location = int(0)
        
        if (self.isReverseMove):
            self.optional_verbage = " spaces backward"
        else:
            self.optional_verbage = " spaces forward"

    # move_spaces(self, current_location : int) : int
    def move_spaces(self, current_location):
        ''' Takes player's current location and returns the addition of the number of spaces to move '''
        if (self.isReverseMove):
            self.print_event_action(self.action_text, self.move * -1, self.optional_verbage)
        elif (not self.isReverseMove):
            self.print_event_action(self.action_text, self.move, self.optional_verbage)
            
        self.new_location = current_location + self.move
        
        if self.new_location < 0:   # possible only for reverse movement/negative moveSpaces
            self.new_location = (current_location + 40) + self.move

        return self.new_location


'''
└── OwnableCardEvents
    └── GetOutOfJailFree
'''
class OwnableCardEvents(CardEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name)
        self.action_text = "Player now owns "    #... "total number of owned cards of that type"
        self.isOwnable = event_value    # not used by class, but may be used for implementation
        self.new_total_owned = int(0)   # changed when new card and total number of owned cards of a specific category are both given


class GetOutOfJailFree(OwnableCardEvents):  # AKA: GOJF
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.optional_verbage = " Get Out Of Jail Free Cards"
    
    # give_card(self, GOJF_owned_count : int) : int
    def give_card(self, GOJF_owned_count):
        ''' Takes the amount of GOJF cards currently owned and returns the addition of one more card '''
        self.new_total_owned = GOJF_owned_count + 1
        self.print_event_action(self.action_text, self.new_total_owned, self.optional_verbage)
        return self.new_total_owned
