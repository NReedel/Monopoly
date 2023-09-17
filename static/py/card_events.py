###############################################################
# card_events.py
###############################################################

###
# *Name:    Alicyn Knapp
# *Credit:  PennWest Projects! (discord server)
# *Purpose: Define Monopoly card events attributes and actions
###

###############################################################
# Here's what a card hierarchy might looks like
# Although the below all look like they could be methods in the Card class,
#	this problem arises: how do you enforce the use of only the methods
#	associated with the card event? You technically could define the methods
#	only in the "if this card event, define these variables" conditionals, but
#	that gets very very messy. Each of the classes below can and should have
#	their own data and methods associated with them.
# Here's how this will work: an instance of each derived Card Event will be
#	declared in their respective condiitonals below
# Should the CardEvents remain here or in their own file?
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


class CardEvents:
    def __init__(self, event_name):
        self.event_name = event_name
        self.action_text = ""
        
    # print_event_action(self, action : string, action_attribute : T) : void
    def print_event_action(self, action_text, action_attribute):
        print(action_text, action_attribute, ".")


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
        self.total_money_paid = (self.rate_money_amount * house_count) + (self.second_rate_money_amount * hotel_count)
        # second_rate_money_amount undefined ⚠⚠⚠
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
        self.move_to = event_value
        

class MoveToIndex(MovePlayerEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.action_text = "Moved to tile at index "

    # move_to_index(self) : int
    def move_to_index(self):
        ''' Returns the index that the player must move to '''
        self.print_event_action(self.action_text, self.move_to)
        return self.move_to

    
class MoveToNearest(MovePlayerEvents):
    def __init__(self, event_name, event_value, second_event_value):
        super().__init__(event_name, event_value)
        self.action_text = "Moved to nearest "
        self.rent_multiplier = second_event_value
        self.nearest_tile_index = int(0)
        

class MoveToNearestUtility(MoveToNearest):
    def __init__(self, event_name, event_value, second_event_value):
        super().__init__(event_name, event_value, second_event_value)

    # move_to_index(self, current_location : int)
    def move_to_nearest_utility(self, current_location):
        ''' Returns the index of the nearest utility that the player must move to '''
        if (self.move_to == "Utility"):
            if (current_location >= 28 or current_location < 12):
                # if current_location >= 28, make sure all pass GO criteria are being fulfilled
                self.nearest_tile_index = 12
            elif (current_location >= 12 or current_location < 28):
                self.nearest_tile_index = 28
            self.print_event_action(self.action_text, self.move_to)
        else:
            print("Invalid move_to value (Utility). Cannot move player.")
        return self.nearest_tile_index

    # pay_card_rent(self, current_balance : int, dice_roll : int) : int
    def pay_card_rent(self, current_balance, dice_roll):
        ''' Takes player's current balance and dice roll and returns the subtraction of the total amount paid from the current balance '''
        self.total_paid = dice_roll * self.rent_multiplier
        return current_balance - self.total_paid


class MoveToNearestRailroad(MoveToNearest):
    def __init__(self, event_name, event_value, second_event_value):
        super().__init__(event_name, event_value, second_event_value)

    # move_to_index(self, current_location : int)
    def move_to_nearest_railroad(self, current_location):
        ''' Returns the index of the nearest railroad that the player must move to '''
        if (self.move_to == "Railroad"):
            if (current_location >= 35 or current_location < 5):
                # if current_location >= 28, make sure all pass GO criteria are being fulfilled
                self.nearest_tile_index = 5
            elif(current_location >= 5 or current_location < 15):
                self.nearest_tile_index = 15
            elif(current_location >= 15 or current_location < 25):
                self.nearest_tile_index = 25
            elif (current_location >= 25 or current_location < 35):
                self.nearest_tile_index = 35
            self.print_event_action(self.action_text, self.move_to)
        else:
            print("Invalid move_to value (Railroad). Cannot move player.")
        return self.nearest_tile_index

    # pay_card_rent(self, current_balance : int, normal_rent_amount : int) : int
    def pay_card_rent(self, current_balance, normal_rent_amount):
        ''' Takes player's current balance and the amount of rent normally owed and returns the subtraction of the total amount paid from the current balance '''
        self.total_paid = normal_rent_amount * self.rent_multiplier
        return current_balance - self.total_paid


class MoveSpaces(MovePlayerEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        if (self.move_to > 0):
            self.action_text = f"Moved forward {self.move_to} spaces."
        elif (self.move_to < 0):
            self.action_text = f"Moved backward {self.move_to * -1} spaces."
        else:
            self.action_text = "No spaces moved. Number of spaces to move is 0."

    # move_spaces(self, current_location : int) : int
    def move_spaces(self, current_location):
        ''' Takes player's current location and returns the addition of the number of spaces to move '''
        print(self.action_text)
        return current_location + self.move_to


'''
└── OwnableCardEvents
    └── GetOutOfJailFree
'''
class OwnableCardEvents(CardEvents):
    def __init__(self, event_name, event_value):
        super().__init__(event_name)
        self.isOwnable = event_value
        self.owned_count = int(0)


class GetOutOfJailFree(OwnableCardEvents):  # AKA: GOJF
    def __init__(self, event_name, event_value):
        super().__init__(event_name, event_value)
        self.action_text = f"Player now has {self.owned_count} Get Out Of Jail Free cards."
    
    # give_card(self, GOJF_owned_count : int) : int
    def give_card(self, GOJF_owned_count):
        ''' Takes the amount of GOJF cards currently owned and returns the addition of one more card '''
        self.owned_count = GOJF_owned_count + 1
        print(self.action_text)
        return self.owned_count
