from inventory import *
from controller import *
from StatStruct import *
from ledger import *
from command import *
from random import randint

#implement strategy pattern for character types

class RPGCharacter(Receiver):
	
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
		self.stats.initPlayerStats()
		self.stats.attack=self.stats.attack+3

	def do_something(self):
		return "You explained that you're only in school because you got a sports scholarship"

class Engineer(RPGCharacter):
	def __init__(self): 
		super(Engineer,self).__init__()
		self.characterType="Engineering Major"
		self.stats.initPlayerStats()
		self.stats.maxMagic=self.stats.maxMagic+3

	def do_something(self):
		return "You overanalyzed the question"

class Art(RPGCharacter):
	def __init__(self): 
		super(Art,self).__init__()
		self.characterType="Art Major"
		self.stats.initPlayerStats()
		self.stats.defense=self.stats.defense+3
	def do_something(self):
		return "You doodled on your work"

class History(RPGCharacter):
	def __init__(self): 
		super(History,self).__init__()
		self.characterType="History Major"
		self.stats.initPlayerStats()
		self.stats.maxHealth=self.stats.maxHealth+3
	def do_something(self):
		return "You remembered."

class Professor(RPGCharacter):
	def __init__(self): 
		super(Professor,self).__init__()
		self.characterType="Professor"
		self.stats.initPlayerStats()
		self.stats=self.stats*3

	def do_something(self):
		rando=randint(0,100)
		if (rando>83):
			return "The Professor gave a pop quiz"
		elif (rando>50):
			return "The Professor gave an exam"
		else:
			return "The Professor gave a homework assignment"


