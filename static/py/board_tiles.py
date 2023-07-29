# board_tiles.py

###
# *Name:      Nate Reedel
# *Credit:    PennWest Projects! (discord server)
# *Purpose:   generate tiles on the board, used for owned and unowned properties
#             defined by the tiles json file. 
###

###############################################################
# BoardsTiles Hierarchy 🔳
###############################################################
'''
BoardTiles
├── SpecialBoardTiles
├── StreetBoardTiles
├── RailRoadBoardTiles
└── UtilityBoardTiles
    ├──CornerBoardTiles
    ├──TaxBoardTiles
    └── CardBoardTiles
'''
###############################################################
class BoardTiles():

   # -- Constructor --
   def __init__(self, tile):
        self.type = "none"  # "special","street", "railroad", "utility", "none"
        self.owner = "none" # "player 2-6", "bank", "none"
         # note: bank class needs identifier for owner to work 
        self.houses = int(0)
        self.hotels = int(0)
        self.index = tile['index']
        self.name = tile['name']
        
class SpecialBoardTiles(BoardTiles):
   # -- Constructor --
   def __init__(self, tile):   
      super().__init__(tile)
      self.type = tile['type'] # "special" 
      self.owner = "none"
      self.special = tile['special'] # "corner" or "card" or"tax"

class StreetBoardTiles(BoardTiles):
   # -- Constructor --
   def __init__(self, tile):
       super().__init__(tile)
       self.type = tile['type'] # "street" 
       self.owner = "bank"

class RailRoadBoardTiles(BoardTiles):
   # -- Constructor - 
   def __init__(self, tile):
      super().__init__(tile)
      self.type = tile['type'] # "railroad"
      self.owner = "bank"
                      
class UtilityBoardTiles(BoardTiles):
   # -- Constructor --
   def __init__(self, tile):
       super().__init__(tile)
       self.type = tile['type'] # "utility" 
       self.owner = "bank"
       
       
# class CornerBoardTiles(UtilityBoardTiles):

# class TaxBoardTiles(UtilityBoardTiles):

# class CardBoardTiles(UtilityBoardTiles):



      
