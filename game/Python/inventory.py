from itemFactory import *

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
