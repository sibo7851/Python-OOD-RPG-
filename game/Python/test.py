from item import *


def jeffBridges():
	return "The Big Lebowski"


class WeaponFactory: 
  
    """ initialize weapons """
  
    def __init__(self): 
  
        self.Item = Item()
  
    def objectify(self, param): 
        self.Item.itemStats=param[1]
        self.Item.itemName="Sword of "+param[0]
        self.Item.classType=ItemEnum(1)
        """change the message using translations"""
        return self.Item
  
class ConsumableFactory: 
  
    """ initialize consumable """
  
    def __init__(self): 
  
        self.Item = Item()
  
    def objectify(self, param): 
        self.Item.itemStats=param[1]*10
        self.Item.itemName="Potion of "+param[0]
        self.Item.classType=ItemEnum(2)
        """change the message using translations"""
        return self.Item

class ResourceFactory: 
  
    """ initialize consumable """
  
    def __init__(self): 
  
        self.Item = Item()
  
    def objectify(self, param): 
        self.Item.itemStats=param[1]
        self.Item.itemName=param[0]
        self.Item.classType=ItemEnum(3)
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

#below is for testing, delete when working
if __name__ == "__main__": 
  
    f = Factory("Consumable") 
    X=Stats()
    X.attack=10
    i =("curing",X)
    O=f.objectify(i)
    print(O.itemStats.attack) 