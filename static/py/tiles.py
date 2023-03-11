# tiles.py
# Monopoly board tiles

'''
tiles [40]
├── property [22]
│   ├── purple
│   ├── light blue
│   ├── magenta
│   ├── orange
│   ├── red
│   ├── yellow
│   ├── green
│   └── dark
│       ├── color
│       ├── name
│       └── price
└── special [18]
    ├── corner [4]
    │   ├── go
    │   ├── jail
    │   ├── free parking
    │   └── go to jail
    ├── card [6]
    │   ├── community chest [3]
    │   └── chance [3]
    │       ├── name
    │       ├── img
    │       └── [bottom]
    ├── tax [2]
    │   ├── income
    │   └── luxury
    │       ├── name
    │       ├── img
    │       └── bottom
    ├── railroad [4]
    │   ├── reading
    │   ├── pennsylvania
    │   ├── b & o
    │   └── short line
    │       ├── name
    │       ├── img
    │       └── price
    └── utility [2]
        ├── electric company
        └── water works
            ├── name
            ├── img
            └── price
'''

class Tile:
	def __init__ (self, index)
		self.name = name
		self.index = index
	
	def Render_HTML():
		pass

'''
tiles {
    color,
    name,
    price,
    deed,
    events {
        buy,
        payRent,
        upgrade,
        sellUpgrade,
        mortgage,
        trade,
        declareBankruptcy
    },
    streets[22],
    upgrades {
        house,
        hotel
    },
    state {
        canPurchase,
        owned,
        occupiedBy,
        rentValue
    }
'''