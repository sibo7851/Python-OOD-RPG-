class Stats(object):
	attack=0.0
	defense=0.0
	speed=0.0
	maxHealth=0.0
	currentHealth=0.0
	maxMagic=0.0
	currentMagic=0.0
	accuracy=0.0
	evasion=0.0
	statusEffect=[]
	money=0.0
	credits=0.0
	def __mul__(self, other): 
		self.attack=self.attack*other
		self.defense=self.defense*other
		self.speed=self.speed*other
		self.maxHealth=self.maxHealth*other
		self.currentHealth=self.currentHealth*other
		self.maxMagic=self.maxMagic*other
		self.currentMagic=self.currentMagic*other
		self.accuracy=self.accuracy*other
		self.evasion=self.evasion*other
		self.money=self.money*other
		return self

	def __add__(self, other):
		self.attack=self.attack+other.attack
		self.defense=self.defense+other.defense
		self.speed=self.speed+other.speed
		self.maxHealth=self.maxHealth+other.maxHealth
		self.currentHealth=self.currentHealth+other.currentHealth
		self.maxMagic=self.maxMagic+other.maxMagic
		self.currentMagic=self.currentMagic+other.currentMagic
		self.accuracy=self.accuracy+other.accuracy
		self.evasion=self.evasion+other.evasion
		self.money=self.money+other.money
		return self

	def initPlayerStats(self):
		self.attack=1.0
		self.defense=1.0
		self.speed=1.0
		self.maxHealth=1.0
		self.currentHealth=1.0
		self.maxMagic=1.0
		self.currentMagic=1.0
		self.accuracy=1.0
		self.evasion=1.0
		self.money=0.0
