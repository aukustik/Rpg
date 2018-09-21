from character import *
import random
class Location:
    def __init__(self, level):
        self.wall = False 
        self.level = level

class Road(Location):
    def __init__(self, level):
        self.wall = False
    
    def __str__(self):
        return '#'

    def event(self, character):
        self.character = character
        self.character.stamina -= 1

class Wall(Location):
    def __init__(self, level):
        self.wall = True
    
    def __str__(self):
        return 'W'
    
    def event(self, character):
        print('This is Wall! Hello!')

class Door(Location):
    def __init__(self, level):
        self.wall = True
    
    def __str__(self):
        return '?'

    def event(self, character):
        self.character = character
        for i in self.character.backpack.storage:
            if (i.item_id == 'Key'):
                self.character.backpack.remove_item(i)
                self.wall = False
                self.character.stamina - 1
                print('Door is Opened!')
        if (self.wall == True):
            print('This door is closed, you need a Key.')

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

class KeyBox(Location):
    def __str__(self):
        return 'K'
    
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
                for i in self.level.key_chest.storage:
                    if (i.item_id == chose_2):
                        print(i)
                        character.backpack.add_item(i)
                        self.level.key_chest.remove_item(i)
            if (chose == 'exit'):
                return False
    
    def show_chest(self):
        print('In Chest:')
        for i in self.level.key_chest.storage:
            print(i.info())
        print('_____________________')

class CharPosition(Location):
    def __str__(self):
        return '0'
    
    def __init__(self, level):
        self.wall = False
    
    def event(self, character):
        character.say_any('So scary...')

class Enemy(Location):

    def __str__(self):
        return 'E'

    def __init__(self, level, name):
        self.wall = False
        self.name = name
    
    def event(self, character):
        self.character = character
        self.enemy = MainChar(self.name)
        self.enemy_damage = [5,10,1]
        self.enemy.say_any('Stop! Or i will kill you!')
        self.fight()

    def fight(self):
        while(True):
            if (self.enemy.health <= 0):
                print(self.enemy.name,'is Dead')
                return False
            if (self.character.health <= 0):
                print('You Died...')
                break
            print(self.character.name, 'attacks: Hand/Leg/Boulder/Weapon')
            attack_type = input()
            my_damage = 0
            if(attack_type == 'Hand'):
                my_damage = random.randrange(0,5,1)
                self.enemy.health -= my_damage
                print(self.enemy.name, 'lost', my_damage, 'HP and now has ', self.enemy.health)
            if(attack_type == 'Leg'):
                my_damage = random.randrange(5,10,1)
                self.enemy.health -= my_damage
                print(self.enemy.name, 'lost', my_damage, 'HP and now has ', self.enemy.health)
            if(attack_type == 'Boulder'):
                my_damage = random.randrange(15,20,1)
                self.enemy.health -= my_damage
                print(self.enemy.name, 'lost', my_damage, 'HP and now has ', self.enemy.health)
            if(attack_type == 'Weapon'):
                my_damage = 100
                self.enemy.health -= my_damage
                print(self.enemy.name, 'lost', my_damage, 'HP and now has ', self.enemy.health)
            self.enemy.say_any('Never Surrender!')
            print(self.name, ' attacks!')
            enemy_damage = random.randrange(*self.enemy_damage)
            self.character.health -= enemy_damage
            print('You lost', enemy_damage, 'HP and now have', self.character.health)

            