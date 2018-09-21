from character import *
import random
class Location:
    def __init__(self, level):
        self.wall = False 
        self.level = level
class Road(Location):
    
    def __str__(self):
        return '#'

    def event(self, character):
        self.character = character
        self.character.stamina -= 1

class Wall(Location):
    def __str__(self):
        return 'W'
    
    def event(self):
        self.wall = True

class Door(Location):
    def __str__(self):
        return '?'

    def event(self, character):
        self.character = character
        self.wall = True
        for i in self.character.backpack.storage:
            if (i.item_id == 'Key'):
                self.character.backpack.remove_item(i)
                self.wall = False
                self.character.stamina - 1
                print('Door is Opened!')
        if (self.wall == True):
            print('You need Key.')

class Box(Location):
    def __str__(self):
        return 'C'
    
    def event(self, character):
        print('You found CHEST!')
        while(True):
            self.show_chest()
            print('write take/exit')
            chose = input()
            if(chose == 'take'):
                print('take what?')
                self.show_chest()
                chose_2 = input()
                for i in self.level.treasure_box.storage:
                    if (i.item_id == chose_2):
                        print(i)
                        character.backpack.add_item(i)
                        self.level.treasure_box.remove_item(i)
            if (chose == 'exit'):
                return False
    
    def show_chest(self):
        print('In Chest:')
        for i in self.level.treasure_box.storage:
            print(i.info())
        print('_____________________')


            