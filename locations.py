from character import MainChar
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
        self.character.stats.stamina_attr.set(-1)

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
                self.character.stats['CurrentStamina'] - 1
                print('Door is Opened!')
        if (self.wall == True):
            print('This door is closed, you need a Key.')

class Box(Location):
    
    def __init__(self, level, box):
        self.wall = False
        self.level = level
        self.box = box

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
                for i in self.box.storage:
                    if (i.item_id == chose_2):
                        print(i)
                        character.backpack.add_item(i)
                        self.box.remove_item(i)
            if (chose == 'exit'):
                return False
    
    def show_chest(self):
        print('In Chest:')
        for i in self.box.storage:
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
            print(self.character.name, 'attacks: Hand/Leg/Boulder/Weapon')
            attack_type = input()
            my_damage = 0
            if(attack_type == 'Hand'):
                my_damage = random.randrange(0,5,1)
                self.enemy.stats.health_attr.set(-my_damage)
                print(self.enemy.name, 'lost', my_damage, 'HP and now has ', self.enemy.stats.health_attr.get())
            if(attack_type == 'Leg'):
                my_damage = random.randrange(5,10,1)
                self.enemy.stats.health_attr.set(-my_damage)
                print(self.enemy.name, 'lost', my_damage, 'HP and now has ', self.enemy.stats.health_attr.get())
            if(attack_type == 'Boulder'):
                my_damage = random.randrange(15,20,1)
                self.enemy.stats.health_attr.set(-my_damage)
                print(self.enemy.name, 'lost', my_damage, 'HP and now has ', self.enemy.stats.health_attr.get())
            if(attack_type == 'Weapon'):
                my_damage = 100
                self.enemy.stats.health_attr.set(-my_damage)
                print(self.enemy.name, 'lost', my_damage, 'HP and now has ', self.enemy.stats.health_attr.get())
                print(self.enemy.name,'is Dead')
                self.character.notify_obs()
                return False
            self.enemy.say_any('Never Surrender!')
            print(self.name, ' attacks!')
            enemy_damage = random.randrange(*self.enemy_damage)
            self.character.stats.health_attr.set(-enemy_damage)
            print('You lost', enemy_damage, 'HP and now have', self.character.stats.health_attr.get())
            if (self.character.stats.health_attr.get() <= 0):
                print('You Died...')
                break

            