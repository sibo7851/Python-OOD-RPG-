
class bill(object):
	def __init__(self,detail,cost):
		self.detail=detail
		self.cost=cost

class ledger(object):
	def __init__(self):
		self.debtArray=[]

	def addBill(self,bill):
		self.debtArray.append(bill)
