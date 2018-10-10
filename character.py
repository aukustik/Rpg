import time
import random
from achievments import FirstKill
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


            

class Item:
    def __init__(self, name):
        self.item_id = name
        self.quantity = 1
        self.item_size = 1
        self.type = 'Other'
        self.bonuses = ItemBonus(self.type, 1)
    def generate(self):
        raise NotImplementedError

    def __str__(self):
        return self.item_id
    
    def info(self):
        self.message = self.type + ': ' + self.item_id + ' (' + self.bonuses.about_item() + ')'
        return self.message

class HealingPotion(Item):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Potion'
        self.bonuses = ItemBonus(self.type, 1)

class Helmet(Item):
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Helmet'
        self.bonuses = ItemBonus(self.type, 1)

class Key(Item):

    def __init__(self, name):
        super().__init__(name)
        self.type = 'Key'
        self.bonuses = ItemBonus(self.type, 1)

class BodyArmour(Item):
    
    def __init__(self, name):
        super().__init__(name)
        self.type = 'Body'
        self.bonuses = ItemBonus(self.type, 1)

class ItemBonus:
    def __init__(self, type, charlevel):
        item_type = type
        self.bonuses = {
            'MaxHealth': random.randrange(0, charlevel+10, 1),
            'MaxMana': random.randrange(0, charlevel+10, 1),
            'MaxStamina': random.randrange(0, charlevel+5, 1),
            'Damage': random.randrange(charlevel+10, charlevel+20, 1),
            'Defence': random.randrange(charlevel+5, charlevel+10, 1)
        }
        if (item_type == 'Helmet' or item_type == 'Body' or item_type == 'Boots' or item_type == 'Pants' or item_type == 'Gloves'):
            self.bonuses['Damage'] = 0
        
        if (item_type == 'First Weapon'):
            self.bonuses['Defence'] = 0
        
        if (item_type == 'Key' or item_type == 'Potion'):
            self.bonuses = {
                'Key': 'TREASURE KEY'
            }
        
    def about_item(self):
        bonus_attributes = 'Info:'
        for key in self.bonuses.keys():
            if (self.bonuses[key] != 0):
                bonus_attributes += str(key) + ' = ' + str(self.bonuses[key]) + ', '
        return bonus_attributes
    #Необходимо добавить эти бонусы в Item, и сделать def refresh_stats()

class Storage:
    
    def __init__(self, maxSize):
        self.size = maxSize
        self.storage = []
    
    def add_item(self, item):
        if(len(self.storage) + item.item_size > self.size):
            print('Not enough space')
        else:
            self.storage.append(item)
        
    def remove_item(self, item):
        self.storage.remove(item)

    def use_item(self, item):
        print('Using item', item.item_id)
        self.storage.remove(item)

    

