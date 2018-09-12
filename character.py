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
    def equip_item(self, item):
        if (item.type == 'Helmet'):
            if(self.equipment['Helmet'] == None):
                self.max_health += item.bonus_health
                self.equipment['Helmet'] = item
            else:
                print('Unequip old Helmet and equip',item.item_id ,'?(yes/no):')
                result = input()
                if(result=='yes'):
                    self.unequip_item('Helmet')
                    self.equip_item(item)
                else:
                    return
                
    def unequip_item(self, type):
        if (self.equipment[type] != None):
            self.max_health -= int(self.equipment[type].bonus_health)
            self.equipment[type] = None
 

    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.name, 'lost', damage, 'hp')

    def healing(self, heal):
        self.health = self.health + heal
        print(self.name,'healed',heal, 'hp')

    def print_stats(self):
        print('HERO',self.name,'STATS')
        print('Heath Points:', self.health, '/',self.max_health)
        if (self.equipment['Helmet'] != None):
            print('Helmet:', self.equipment['Helmet'].item_id)
        if (self.equipment['Body'] != None):
            print('Body Armour:', self.equipment['Body'].item_id)
        if (self.equipment['Boots'] != None):
            print('Boots:', self.equipment['Boots'].item_id)
        if (self.equipment['Gloves'] != None):
            print('Gloves:', self.equipment['Gloves'].item_id)
        if (self.equipment['Weapon'] != None):
            print('Weapon', self.equipment['Weapon'].item_id)
class Item:
    def __init__(self, name, size):
        self.item_id = name
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
        print('Using item', item.item_id)
        self.storage.remove(item)