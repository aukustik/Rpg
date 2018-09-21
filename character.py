import time

class MainChar:
    def __init__(self, nameChar):
        self.health = 100
        self.stamina = 15
        self.max_health = 100
        self.max_stamina = 15
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
            if(self.equipment[item.type] == None):
                self.equipment[item.type] = item
                if (item.type == 'Helmet'):
                    self.max_health += item.bonus_health
                    self.health += item.bonus_health
                if (item.type == 'Body'):
                    self.max_stamina += item.bonus_stamina
            else:
                print('Unequip old', item.type,'and equip',item.item_id ,'?(yes/no):')
                result = input()
                if(result=='yes'):
                    self.unequip_item(item.type)
                    self.equip_item(item)
                else:
                    return
    def unequip_item(self, type):
        if (self.equipment[type] != None):
            if (type == 'Helmet'):
                self.max_health -= int(self.equipment[type].bonus_health)
                self.health -= int(self.equipment[type].bonus_health)
            if (type == 'Body'):
                self.max_stamina -= int(self.equipment[type].bonus_stamina)
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
        print('Stamina:', self.stamina, '/', self.max_stamina)
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
    
    def health_checking(self):
        return self.max_health + sum([item.bonus_health for item in self.equipment])
        
    def say_any(self, text):
        message = text
        print(self.name, 'says: ', end='')
        for i in message:
            print(i, end='')
            time.sleep(0.03)
        time.sleep(0.5)
        print('\n')
    
    def show_backpack(self):
        print('Backpack:')
        for i in self.backpack.storage:
            print(i.info())
        
        while(True):
            print('equip item/exit')
            chose = input()
            if (chose == 'equip item'):
                print('what?')
                chose_2 = input()
                for i in self.backpack.storage:
                    if (chose_2 == i.item_id):
                        self.equip_item(i)
                        self.backpack.remove_item(i)
                
            if (chose == 'exit'):
                return False




class Item:
    def __init__(self, name, size):
        self.item_id = name
        self.itemSize = size
        self.quantity = 1
    
    def __str__(self):
        return self.item_id

class HealingPotion(Item):
    type = 'Potion'
    def using(self, char):
        char.healing(20)

class Helmets(Item):
    type = 'Helmet'
    bonus_health = 0
    
    def set_health(self, value):
        self.bonus_health = value

    def get_health(self):
        return self.bonus_health

    def info(self):
        self.message = self.type + ': ' + self.item_id + ' (' + 'Bonus HP:' + str(self.bonus_health) + ')'
        return self.message

class Keys(Item):
    type = 'Key'

    def info(self):
        self.message = 'Item:' + self.type
        return self.message

class BodyArmour(Item):
    type = 'Body'
    bonus_stamina = 0
    
    def set_stamina(self, value):
        self.bonus_stamina = value
    
    def get_stamina(self):
        return self.bonus_stamina
    
    def info(self):
        self.message = self.type + ': ' + self.item_id + ' (' + 'Bonus Stamina:' + str(self.bonus_stamina) + ')'
        return self.message

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