from itemFactory import *
from random import randint

class inventory(object):
	itemArray=[]
	def __init__(self): 
		self.itemArray=[]

	def getItems(self):
		return self.itemArray

	def countItem(self,item):
		return self.itemArray.count(item)

	def addItem(self,item):
		self.itemArray.append(item)

	def removeItem(self,item):
		self.itemArray.remove(item)


def createTestInventory():
	I=inventory()
	f = Factory("Consumable") 
	X=Stats()
	X.attack=10
	i =("curing",X)
	O=RareDecorator(f.objectify(i))
	I.addItem(O)
	I.addItem(O)
	return I

def findRandomItem():
	f = Factory("Consumable") 
	X=Stats()
	X.maxHealth=5
	X.currentHealth=5
	i =("Adderall",X)
	rando=randint(0,100)
	if rando>90:
		O=LegendaryDecorator(f.objectify(i))
	elif rando>50:
		O=UltraRareDecorator(f.objectify(i))
	else:
		O=RareDecorator(f.objectify(i))
	return O
