from inventory import *
from controller import *
from StatStruct import *

class RPGCharacter(object):
	
	def __init__(self): 
		self.inventory=inventory()
		self.stats=Stats()

