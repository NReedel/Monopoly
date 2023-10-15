###############################################################
# tiles.py
# Monopoly board tile class and derived classes
###############################################################

from enum import Enum

###############################################################
# Enumerated Monopoly Class 🔎
###############################################################

class Monopoly(Enum):
    # monopoly_type # new # move to seperate file
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
	
    def __init__ (self, tile):
        self.tile_id = tile['index']
        self.tile_name = tile['name']
        self.owned_by = "none"    # "player number", "bank", "none"
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

    def __init__ (self, tile):
        super().__init__(tile)
        self.property_cost = tile['price']
        self.mortgage_value = 0
        self.is_mortgaged = False
        self.rent_base = 0
        self.set_num_owned = 0
        self.set_num_total = 0
        self.houses = int(0)
        self.hotels = int(0)
        self.tile_class = tile['css']['class'] 
        self.tile_type = tile['type']  # "street", "railroad", "utility"
        self.monopoly_type = Monopoly.NONE
        
    # available_deed(self) : bool
    def available_deed(self): 
      if self.owned_by == "bank":
         return True
      return False


class PropertyStreet(TileProperty):

    def __init__ (self,tile):
    
        super(PropertyStreet, self).__init__(tile)
        self.has_monopoly  = False 
        self.tile_color = ""    # need to standardize color format, ie. hex
        self.cost_house = 0
        self.num_houses = 0
        self.num_hotels = 0
        # max_groups_value =  (2, 3, 3, 3, 3, 3, 3, 2) # maybe
        # new
        if(self.tile_class == "property prop-brown"):        
            self.monopoly_type = Monopoly.BROWN
        if(self.tile_class == "property prop-sky-blue"):
            self.monopoly_type = Monopoly.CYAN
        if(self.tile_class == "property prop-dark-orchid"):
            self.monopoly_type = Monopoly.MAGENTA
        if(self.tile_class == "property prop-orange"):
            self.monopoly_type = Monopoly.ORANGE     
        if(self.tile_class == "property prop-red"):
            self.monopoly_type = Monopoly.RED   
        if(self.tile_class == "property prop-yellow"):
            self.monopoly_type = Monopoly.YELLOW     
        if(self.tile_class == "property prop-green"):
            self.monopoly_type = Monopoly.GREEN      
        if(self.tile_class == "property prop-cobalt-blue"):
            self.monopoly_type = Monopoly.BLUE

class PropertySpecial(TileProperty):

    def __init__ (self,tile):
        super(PropertySpecial, self).__init__(tile)
        self.fname_icon = ""
        self.multiplier = 1
        
class PropertyRailroad(PropertySpecial):
    def __init__ (self,tile):
        super(PropertyRailroad, self).__init__(tile)
        self.monopoly_type = Monopoly.RAIL # new

class PropertyUtility(PropertySpecial):

    def __init__ (self,tile):
        super(PropertyUtility, self).__init__(tile)
        self.monopoly_type = Monopoly.UTILITY # new


    # def get_rent_owed(roll):
    #     if self.set_num_owned == 2:
    #         return roll * 10
    #     elif self.set_num_owned == 1:
    #         return roll * 4
    #     else:
    #         return 0


###############################################################
# Special Tiles 🎲
###############################################################

class TileSpecial(Tile):
    def __init__ (self,tile):
        super(TileSpecial, self).__init__(tile)
        self.fname_icon = ""
        self.tile_type = tile['type']  # "special"
        self.special_type = tile['special'] # "corner" or "card" or "tax"

# Chance and Community Chest
class TileCard(TileSpecial):
    def __init__ (self,tile):
        super(TileCard, self).__init__(tile)
        self.card_type = tile['card']  # "chest" or "chance"

# Income and Luxury Tax
class TileTax(TileSpecial):
    def __init__ (self,tile):
        super().__init__(tile)
        self.tax_amount = tile['price']

# Will need updating later ⚠⚠⚠
class TileCorner(TileSpecial):
    def __init__ (self,tile):
        super(TileCorner, self).__init__(tile)
        self.corner_type = tile['corner']  # "go" or "jail" or "parking" or "arrested" (go to jail)

###############################################################
