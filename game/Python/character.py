from inventory import *
from controller import *
from StatStruct import *

#implement strategy pattern for character types

class RPGCharacter(object):
	
	def __init__(self): 
		self.inventory=inventory()
		self.stats=Stats()
		self.name=""
		self.gender=""

class Biker(RPGCharacter):
	def __init__(self): 
		super(Biker,self).__init__()
		self.characterType="Biker"
		self.stats.attack=self.stats.attack+3

class Scientist(RPGCharacter):
	def __init__(self): 
		super(Scientist,self).__init__()
		self.characterType="Scientist"
		self.stats.maxMagic=self.stats.maxMagic+3

class Yuppie(RPGCharacter):
	def __init__(self): 
		super(Yuppie,self).__init__()
		self.characterType="Yuppie"
		self.stats.defense=self.stats.defense+3

class Priest(RPGCharacter):
	def __init__(self): 
		super(Priest,self).__init__()
		self.characterType="Priest"
		self.stats.maxHealth=self.stats.maxHealth+3

