###############################################################
# cards.py
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
│   └── MoveSpaces	# Also used for reverse movement by a number of tiles
└── OwnableCardEvents
    └── GOJF

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
    def __init__(self, event_name, event_attribute):
        super().__init__(event_name)
        self.static_money_amount = event_attribute
        

class PayStaticAmount(StaticMoneyEvents):
    def __init__(self, event_name, event_attribute):
        super().__init__(event_name, event_attribute)
        self.action_text = "Paid $"

    # pay_money(self, current_balance : int) : int
    def pay_money(self, current_balance):
        self.print_event_action(self.action, self.static_money_amount)
        return current_balance - self.static_money_amount


class ReceiveStaticAmount(StaticMoneyEvents):
    def __init__(self, event_name, event_attribute):
        super().__init__(event_name, event_attribute)
        self.action_text = "Received $"

    # receive_money(self, current_balance : int) : int
    def receive_money(self, current_balance):
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
    def __init__(self, event_name, event_attribute):
        super().__init__(event_name)
        self.rate_money_amount = event_attribute


class PayRateAmount(RateMoneyEvents):
    def __init__(self, event_name, event_attribute):
        super().__init__(event_name, event_attribute)
        self.action_text = "Paid $"


class PayPlayerRateAmount(PayRateAmount):
    def __init__(self, event_name, event_attribute, player_count):
        super().__init__(event_name, event_attribute)
        self.total_money_paid = self.rate_money_amount * (player_count - 1)  # excludes current player

    # pay_money(self, current_balance : int, player_count : int) : int
    def pay_money(self, current_balance):
        self.print_event_action(self.action_text, self.total_money_paid)
        return current_balance - self.total_money_paid

    # receive_owed_amount(self) : int
    def receive_owed_amount(self, owed_player_balance):
        ''' Used for paying all other players their owed rate '''
        return owed_player_balance + self.rate_money_amount


class PayBuildingRateAmount(PayRateAmount):
    def __init__(self, event_name, event_attribute, second_event_attribute, house_count, hotel_count):
        super().__init__(event_name, event_attribute)
        self.second_rate_money_amount = second_event_attribute  # hotels; houses are listed first in json
        self.total_money_paid = (self.rate_money_amount * house_count) + (self.second_rate_money_amount * hotel_count)

    # pay_money(self, current_balance : int, player_count : int) : int
    def pay_money(self, current_balance):
        self.print_event_action(self.action_text, self.total_money_paid)
        return current_balance - self.total_money_paid


class ReceiveRateAmount(RateMoneyEvents):
    pass


class ReceivePlayerRateAmount(ReceiveRateAmount):
    pass


'''
├── MovePlayerEvents
│   ├── MoveToIndex
│   ├── MoveToNearest
│   └── MoveSpaces	# Also used for reverse movement by a number of tiles
'''
class MovePlayerEvents(CardEvents):
    pass


class MoveToIndex(MovePlayerEvents):
    pass


class MoveToNearest(MovePlayerEvents):
    pass


class MoveSpaces(MovePlayerEvents):
    pass


'''
└── OwnableCardEvents
    └── GOJF
'''
class OwnableCardEvents(CardEvents):
    pass


class GOJF(OwnableCardEvents):
    pass
