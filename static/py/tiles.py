###############################################################
# tiles.py
# Monopoly board tile class and derived classes
###############################################################

from enum import Enum

###############################################################
# Enumerated Monopoly Class 🔎
###############################################################

class Monopoly(Enum):
    BROWN       = 1
    CYAN        = 2
    MAGENTA     = 3
    ORANGE      = 4
    RED         = 5
    YELLOW      = 6
    GREEN       = 7
    BLUE        = 8
    RAIL        = 9
    UTILITY     = 10
    NONE        = 11


###############################################################
# Tile Hierarchy 🔳
###############################################################
'''
Tile
├── Tile_Property
│   ├── Property_Street
│   └── Property_Special
│       ├── Property_Railroad
│       └── Property_Utility
└── Tile_Special
    ├── Tile_Card
    ├── Tile_Tax
    └── Tile_Corner
'''
###############################################################

class Tile:
	
    def __init__ (self, index):
		
        self.tile_id = index
        self.tile_name = ""
        
        self.event_on_land = None   # ⚠⚠⚠
        self.occupants = []         # list of player ids
        
        self.fname_bg = ""      # option for later dynamic rendering
        self.css_class = ""     # used later for web app
	
    def Render_HTML():
        pass


###############################################################
# Purchasable Tiles 🏠
###############################################################

class Tile_Property(Tile):

    def __init__ (self):
  
        self.property_cost = 0
        self.mortgage_value = 0
        self.is_mortgaged = False
        self.rent_base = 0

        self.owned_by = None    # player id
        self.set_num_owned = 0
        self.set_num_total = 0
        self.monopoly_type = Monopoly.NONE


class Property_Street(Tile_Property):

    def __init__ (self):
    
        self.tile_color = ""    # need to standardize color format, ie. hex

        self.cost_house = 0
        self.num_houses = 0
        self.num_hotels = 0

    def Can_Buy_Hotel():
        return self.num_houses == 4


class Property_Special(Tile):
    def __init__ (self):
        self.fname_icon = ""


class Property_Railroad(Property_Special):
    def Get_Rent_Owed():
        return self.set_num_owned * 25


class Property_Utility(Property_Special):
    def Get_Rent_Owed(roll):
        if self.set_num_owned == 0:
            return 0
        elif self.set_num_owned == 1:
            return roll * 4
        else:
            return roll * 10


###############################################################
# Special Tiles 🎲
###############################################################

class Tile_Special(Tile):
    def __init__ (self):
        self.fname_icon = ""


# Chance and Community Chest
class Tile_Card(Tile_Special):
    pass


# Income and Luxury Tax
class Tile_Tax(Tile_Special):
    def __init__ (self):
        self.tax_amount = 0


# Will need updating later ⚠⚠⚠
class Tile_Corner(Tile_Special):
    pass


###############################################################