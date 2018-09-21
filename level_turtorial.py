from character import *
from actions import *
import random
class LevelTurtorial:
    def __init__(self):
        self.complete = False
        self.turtorial_npc = MainChar('Ben')
        self.char_pos = [5,3]
        self.size = 7
        self.on_box = False

    def map_creation(self):
        self.map_main = [['X'] * self.size for i in range(self.size)]
        self.map_main[self.char_pos[0]][self.char_pos[1]] = '0'
        return self.map_main

    def map_output(self, map):
        for row in map:
            print(' '.join([str(elem) for elem in row]))
    

    def chest(self):
        self.treasure_box = Storage(20)
        item_helmet = Helmets('Vedro',2)
        item_body = BodyArmour('Manatki Bomzha',2)
        item_body.set_stamina(random.randrange(3,7,1))
        item_helmet.set_health(random.randrange(8,13,1))
        self.treasure_box.add_item(item_helmet)
        self.treasure_box.add_item(item_body)
        self.box_coords = [random.randrange(0,self.size,1),random.randrange(0,self.size,1)]
        if(self.box_coords == self.char_pos):
            self.chest()
        self.map_main[self.box_coords[0]][self.box_coords[1]] = 'C'
    
    def in_box(self, character):
        while(True):
            self.show_chest()
            print('write take/exit')
            chose = input()
            if(chose == 'take'):
                print('what?')
                chose_2 = input()
                for i in self.treasure_box.storage:
                    if (i.item_id == chose_2):
                        print(i)
                        character.backpack.add_item(i)
                        self.treasure_box.remove_item(i)
            if (chose == 'exit'):
                return False
    def show_chest(self):
        for i in self.treasure_box.storage:
            print(i.info())

    def turtorial(self, character):
        map_turt = self.map_creation()
        self.actions = {'up':MoveUp(self),
                        'down':MoveDown(self),
                        'left':MoveLeft(self),
                        'right':MoveRight(self),
                        'equip':Equip(self, character),
                        'open chest':OpenChest(self, character),
                        'map':MapPrint(self),
                        'exit':'',
                        'backpack':BackpackOutput(self, character)}
        self.chest()
        self.turtorial_npc.say_any('Hello my blinded friend!')
        self.turtorial_npc.say_any('I will help u, in this dark...')
        character.say_any('Who are u???')
        self.turtorial_npc.say_any('I\'m The BEN, black Lord.')
        self.turtorial_npc.say_any('U are 0: ')
        self.map_output(map_turt)
        self.turtorial_npc.say_any('U can move on X, let\'s begin!')
        while(True):
            if (self.box_coords == self.char_pos):
                self.on_box = True
                print('You Found CHEST!')
            else:
                self.on_box = False
            direction = input()
            action = self.actions[direction]
            action.run()
            self.map_output(map_turt)

