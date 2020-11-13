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
