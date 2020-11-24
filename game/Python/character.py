from inventory import *
from controller import *
from StatStruct import *
from ledger import *

#implement strategy pattern for character types

class RPGCharacter(object):
	
	def __init__(self): 
		self.inventory=inventory()
		self.stats=Stats()
		self.name=""
		self.gender=""
		self.ledger=ledger()
		self.stats.money=0.0

class Athletic(RPGCharacter):
	def __init__(self): 
		super(Athletic,self).__init__()
		self.characterType="Athletic Major"
		self.stats.attack=self.stats.attack+3

class Engineer(RPGCharacter):
	def __init__(self): 
		super(Engineer,self).__init__()
		self.characterType="Engineering Major"
		self.stats.maxMagic=self.stats.maxMagic+3

class Art(RPGCharacter):
	def __init__(self): 
		super(Art,self).__init__()
		self.characterType="Art Major"
		self.stats.defense=self.stats.defense+3

class History(RPGCharacter):
	def __init__(self): 
		super(History,self).__init__()
		self.characterType="History Major"
		self.stats.maxHealth=self.stats.maxHealth+3

