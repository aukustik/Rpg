class MainChar:
    def __init__(self, nameChar):
        self.health = 100
        self.max_health = 100
        self.name = nameChar
        self.exp = 0
        self.backpack = Storage(20)
        self.equipment = {
            'Helmet':None,
            'Body':None,
            'Boots':None,
            'Gloves':None,
            'Weapon':None
        }
    def equip_item_helm(self, item):
        if (item.type == 'Helmet'):
            self.max_health += item.bonus_health
            self.equipment['Helmet'] = item.itemId

    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.name, 'lost', damage, 'hp')

    def healing(self, heal):
        self.health = self.health + heal
        print(self.name,'healed',heal, 'hp')

    def print_stats(self):
        print('HERO STATS')
        print('Heath Points:', self.health, '/',self.max_health)


class Item:
    def __init__(self, name, size):
        self.itemId = name
        self.itemSize = size
        self.quantity = 1

class HealingPotion(Item):
    type = 'Potion'
    def using(self, char):
        char.healing(20)

class Helmets(Item):
    type = 'Helmet'
    bonus_health = 20


class Storage:
    def __init__(self, maxSize):
        self.size = maxSize
        self.storage = []
    
    def add_item(self, item):
        if(len(self.storage) + item.itemSize > self.size):
            print('Not enough space')
        else:
            self.storage.append(item)
        
    def remove_item(self, item):
        self.storage.remove(item)

    def use_item(self, item):
        print('Using item', item.itemId)
        self.storage.remove(item)