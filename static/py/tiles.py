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
├── TileProperty
│   ├── PropertyStreet
│   └── PropertySpecial
│       ├── PropertyRailroad
│       └── PropertyUtility
└── TileSpecial
    ├── TileCard
    ├── TileTax
    └── TileCorner
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
	
    def render_html():
        pass


###############################################################
# Purchasable Tiles 🏠
###############################################################

class TileProperty(Tile):

    def __init__ (self):

        super(TileProperty, self).__init__(index)

        self.property_cost = 0
        self.mortgage_value = 0
        self.is_mortgaged = False
        self.rent_base = 0

        self.owned_by = None    # player id
        self.set_num_owned = 0
        self.set_num_total = 0
        self.monopoly_type = Monopoly.NONE


class PropertyStreet(TileProperty):

    def __init__ (self):
    
        super(PropertyStreet, self).__init__(index)
        
        self.tile_color = ""    # need to standardize color format, ie. hex

        self.cost_house = 0
        self.num_houses = 0
        self.num_hotels = 0

    def can_buy_hotel():
        return self.num_houses == 4


class PropertySpecial(Tile):

    def __init__ (self):
        super(PropertySpecial, self).__init__(index)
        self.fname_icon = ""


class PropertyRailroad(PropertySpecial):

    def __init__ (self):
        super(PropertyRailroad, self).__init__(index)

    def get_rent_owed():
        return self.set_num_owned * 25


class PropertyUtility(PropertySpecial):

    def __init__ (self):
        super(PropertyUtility, self).__init__(index)

    def get_rent_owed(roll):
        if self.set_num_owned == 2:
            return roll * 10
        elif self.set_num_owned == 1:
            return roll * 4
        else:
            return 0


###############################################################
# Special Tiles 🎲
###############################################################

class TileSpecial(Tile):
    def __init__ (self):
        super(TileSpecial, self).__init__(index)
        self.fname_icon = ""


# Chance and Community Chest
class TileCard(TileSpecial):
    def __init__ (self):
        super(TileCard, self).__init__(index)


# Income and Luxury Tax
class TileTax(TileSpecial):
    def __init__ (self):
        super(TileTax, self).__init__(index)
        self.tax_amount = 0


# Will need updating later ⚠⚠⚠
class TileCorner(TileSpecial):
    def __init__ (self):
        super(TileCorner, self).__init__(index)


###############################################################