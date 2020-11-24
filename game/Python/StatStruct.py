class Stats(object):
	attack=0
	defense=0
	speed=0
	maxHealth=0
	currentHealth=0
	maxMagic=0
	currentMagic=0
	statusEffect=[]
	money=0
	credits=0
	def __mul__(self, other): 
		self.attack=self.attack*other
		self.defense=self.defense*other
		self.speed=self.speed*other
		self.maxHealth=self.maxHealth*other
		self.currentHealth=self.currentHealth*other
		self.maxMagic=self.maxMagic*other
		self.currentMagic=self.currentMagic*other
		self.money=self.money*other
		return self

	def initPlayerStats(self):
		self.attack=1
		self.defense=1
		self.speed=1
		self.maxHealth=1
		self.currentHealth=1
		self.maxMagic=1
		self.currentMagic=1
		self.money=0.0
