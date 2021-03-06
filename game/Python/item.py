from StatStruct import *

class Item(object):
	def __init__(self): 
		self.classType="None"
		self.itemStats=Stats()
		self.itemName=""
		self.classType=""
		self.itemUsage=""

	def use(self):
		pass

class Weapon(Item):
	def __init__(self): 
		itemUsage="Equip"
	def use(self):
		return self.itemStats

class Consumable(Item):
	def __init__(self): 
		itemUsage="Use"
	def use(self):
		return self.itemStats

class Resource(Item):
	def __init__(self): 
		itemUsage="Craft"
	def use(self):
		return self.itemStats


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