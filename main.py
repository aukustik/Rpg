from character import *

mainCharacter = MainChar("Vitalik")
print(mainCharacter.name,'\'s hp = ',mainCharacter.health)
potion = HealingPotion('Healing Potion', 1)
mainCharacter.backpack.add_item(potion)
mainCharacter.backpack.add_item(potion)
royal = Item('Piano', 20)
mainCharacter.backpack.add_item(royal)
mainCharacter.take_damage(50)
potion.using(mainCharacter)
print(mainCharacter.name,'\'s hp =',mainCharacter.health)