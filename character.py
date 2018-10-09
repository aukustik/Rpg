import time
from achievments import *
from equipment import CharacterEquip
from characterstats import Stats
class Observable:
    def __init__(self):
        self.observers = list()
    
    def notify_obs(self):
        for i in self.observers:
            i.notify()
    
    def add_observer(self, observer):
        self.observers.append(observer)
        
    def remove_obs(self, observer):
        self.observers.remove(observer)


class Character(Observable):
    def __init__(self, nameChar):
        super().__init__()
        self.name = nameChar
    
    def say_any(self, text):
        message = text
        print(self.name, 'says: ', end='')
        for i in message:
            print(i, end='')
            time.sleep(0.03)
        time.sleep(0.5)
        print('\n')
    
class MainChar(Character):
    def __init__(self, nameChar):
        super().__init__(nameChar)
        self.stunned = {
            'state': False,
            'duration': 0
        }
        self.name = nameChar
        self.backpack = Storage(20)
        self.equipment = CharacterEquip()
        self.stats = Stats(100, 100, 15)

    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.name, 'lost', damage, 'hp')

    def healing(self, heal):
        self.health = self.health + heal
        print(self.name,'healed',heal, 'hp')

    def print_stats(self):
        print('HERO',self.name,'STATS')
        print('Heath Points:', self.stats.health_attr.get(), '/',self.stats.health_attr.get_max())
        print('Mana Points:', self.stats.mana_attr.get(), '/', self.stats.mana_attr.get_max())
        print('Stamina:', self.stats.stamina_attr.get(), '/', self.stats.stamina_attr.get_max())
        
        if (self.equipment.slots['Helmet'].state() != 'Empty'):
            print('Helmet:', self.equipment.slots['Helmet'].slot.item_id)
        if (self.equipment.slots['Body'].state() != 'Empty'):
            print('Body Armour:', self.equipment.slots['Body'].slot.item_id)
        if (self.equipment.slots['Boots'].state() != 'Empty'):
            print('Boots:', self.equipment.slots['Boots'].slot.item_id)
        if (self.equipment.slots['Gloves'].state() != 'Empty'):
            print('Gloves:', self.equipment.slots['Gloves'].slot.item_id)
        if (self.equipment.slots['First Weapon'].state() != 'Empty'):
            print('First Weapon', self.equipment.slots['First Weapon'].slot.item_id)
        if (self.equipment.slots['Pants'].state() != 'Empty'):
            print('Pants', self.equipment.slots['Pants'].slot.item_id)
    
    def health_checking(self):
        return self.stats.health_attr.get_max + sum([item.bonus_health for item in self.equipment.slots])
    
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
                        self.equipment.equip(i)
                        self.backpack.remove_item(i)
                
            if (chose == 'exit'):
                return False

    def stats_update(self):
        print(self.print_stats())


            

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

    

