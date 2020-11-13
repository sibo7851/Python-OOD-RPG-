from enum import Enum
from StatStruct import *

class ItemEnum(Enum):
	weapon=1
	consumable=2
	resource=3

class Item(object):
	itemStats=Stats()
	itemName=""
	classType=ItemEnum(1)
	def __init__(self): 
		self.classType=ItemEnum(1)

class ItemDecorator(Item):
	def __init__(self, arg):
		self._arg = arg

class RareDecorator(ItemDecorator):
	def __init__(self,arg):
		self.itemStats=arg.itemStats*2
		self.itemName="Rare "+arg.itemName

class UltraRareDecorator(ItemDecorator):
	def __init__(self,arg):
		self.itemStats=arg.itemStats*3
		self.itemName="Ultra Rare "+arg.itemName

class LegendaryDecorator(ItemDecorator):
	def __init__(self,arg):
		self.itemStats=arg.itemStats*4
		self.itemName="Legendary "+arg.itemName