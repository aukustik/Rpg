class MainChar:
    def __init__(self, nameChar):
        self.health = 100
        self.name = nameChar
        self.exp = 0
        self.backpack = Storage(20)

    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.name, 'lost', damage, 'hp')

    def healing(self, heal):
        self.health = self.health + heal
        print(self.name,'healed',heal, 'hp')


class Item:
    def __init__(self, name, size):
        self.itemId = name
        self.itemSize = size
        self.quantity = 1

class HealingPotion(Item):
    def using(self, char):
        char.healing(20)

class Storage:
    def __init__(self, maxSize):
        self.size = maxSize
        self.storage = []
    
    def add_item(self, item):
        if(len(self.storage) + item.itemSize > self.size):
            print('not enough space')
        else:
            self.storage.append(item)
        
    def remove_item(self, item):
        self.storage.remove(item)

    def use_item(self, item):
        print('Using item', item.itemId)
        self.storage.remove(item)