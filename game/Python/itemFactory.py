from item import *

#this is kind of an easter egg I guess
def jeffBridges():
	return "The Big Lebowski"


class WeaponFactory: 
  
    """ initialize weapons """
  
    def __init__(self): 
  
        self.Item = Weapon()
  
    def objectify(self, param): 
        self.Item.itemStats=param[1]
        self.Item.itemName="Sword of "+param[0]
        self.Item.classType="Weapon"
        """change the message using translations"""
        return self.Item
  
class ConsumableFactory: 
  
    """ initialize consumable """
  
    def __init__(self): 
  
        self.Item = Consumable()
  
    def objectify(self, param): 
        self.Item.itemStats=param[1]*10
        self.Item.itemName="Bottle of "+param[0]
        self.Item.classType="Consumable"
        """change the message using translations"""
        return self.Item

class ResourceFactory: 
  
    """ initialize consumable """
  
    def __init__(self): 
  
        self.Item = Resource()
  
    def objectify(self, param): 
        self.Item.itemStats=param[1]
        self.Item.itemName="Stone of "+param[0]
        self.Item.classType="Resource"
        """change the message using translations"""
        return self.Item

  
def Factory(weaponType ="Consumable"): 
  
    """Factory Method"""
    objectFactory = { 
        "Consumable": ConsumableFactory, 
        "Weapon": WeaponFactory,
        "Resource": ResourceFactory
    } 
  
    return objectFactory[weaponType]() 



  
