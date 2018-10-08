class Slot:
    def __init__(self):
        self.slot = 'Empty'
    
    def equip(self, item):
        self.slot = item
    
    def unequip(self):
        item = self.slot
        self.slot = 'Empty'
        return item
    
class HelmetSlot(Slot):

    def equip(self, item):
        if (item.type == 'Helmet'):
            self.slot = item

class BodySlot(Slot):

    def equip(self, item):
        if (item.type == 'Body'):
            self.slot = item

class GlovesSlot(Slot):

    def equip(self, item):
        if (item.type == 'Gloves'):
            self.slot = item

class BootsSlot(Slot):

    def equip(self, item):
        if (item.type == 'Boots'):
            self.slot = item

class PantsSlot(Slot):

    def equip(self, item):
        if (item.type == 'Pants'):
            self.slot = item

class FirstWeaponSlot(Slot):

    def equip(self, item):
        if (item.type == 'First Weapon'):
            self.slot = item

class CharacterEquip:
    def __init__(self):
        self.slots = {
            'Helmet': HelmetSlot(),
            'Body': BodySlot(),
            'Gloves': GlovesSlot(),
            'Boots': BootsSlot(),
            'Pants': PantsSlot(),
            'First Weapon': FirstWeaponSlot()
        }
    
    def equip(self, item):
        self.slots[item.type].equip(item)

    

