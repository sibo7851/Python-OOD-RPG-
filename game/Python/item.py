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