from inventory import *
from controller import *
from StatStruct import *

class Character(object):
	
	def __init__(self): 
		self.inventory=inventory.inventory()
		self.stats=StatStruct.Stats()

