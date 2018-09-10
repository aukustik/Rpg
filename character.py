class MainChar:
    def __init__(self, nameChar):
        self.health = 100
        self.name = nameChar
        self.exp = 0
    
    def take_damage(self, damage):
        self.health = self.health - damage
        print(self.name)
        print(self.health)

    def healing(self, heal):
        self.health = self.health + heal
        print(self.health)


class Item:
    def __init__(self, name, size):
        self.itemId = name
        self.itemSize = size
        self.quantity = 1


class Storage:
    def __init__(self, maxSize):
        self.size = maxSize
        self.storage = []
    
    def add_item(self, item):
        if (item in self.storage):
            self.storage.remove(item)
            item.quantity = item.quantity + 1
            self.storage.append(item)
        else:
            self.storage.append(item)

    def remove_item(self, item):
        self.storage.remove(item)