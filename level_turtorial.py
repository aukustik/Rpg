from character import *
from actions import *
from locations import *
import random

class LevelTurtorial:
    def __init__(self):
        self.complete = False
        self.turtorial_npc = MainChar('Ben')
        self.char_pos = [5,3]
        self.size = 7
        self.on_box = False

    def map_creation(self):
        self.map_main = [[Road(self)] * self.size for i in range(self.size)]
        self.map_main[self.char_pos[0]][self.char_pos[1]] = CharPosition(self)
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
        self.box_coords = [self.size//2,self.size//2]
        if(self.box_coords == self.char_pos):
            self.chest()
        self.map_main[self.box_coords[0]][self.box_coords[1]] = Box(self, self.treasure_box)
        self.map_main[self.box_coords[0]-1][self.box_coords[1]] = Door(self)
        self.map_main[self.box_coords[0]][self.box_coords[1]-1] = Door(self)
        self.map_main[self.box_coords[0]+1][self.box_coords[1]] = Door(self)
        self.map_main[self.box_coords[0]][self.box_coords[1]+1] = Door(self)
        self.map_main[self.box_coords[0]-1][self.box_coords[1]-1] = Wall(self)
        self.map_main[self.box_coords[0]+1][self.box_coords[1]+1] = Wall(self)
        self.map_main[self.box_coords[0]-1][self.box_coords[1]+1] = Wall(self)
        self.map_main[self.box_coords[0]+1][self.box_coords[1]-1] = Wall(self)
    
    def key_box(self):
        self.key_chest = Storage(1)
        item_key = Keys('Key', 1)
        self.key_chest.add_item(item_key)
        self.key_coords = [0, self.size - 1]
        self.map_main[self.key_coords[0]][self.key_coords[1]] = Box(self, self.key_chest)
        self.map_main[self.key_coords[0]][self.key_coords[1] - 1] = Wall(self)
        self.map_main[self.key_coords[0] + 1][self.key_coords[1] - 1] = Wall(self)
        self.map_main[self.key_coords[0] + 1][self.key_coords[1]] = Enemy(self, 'Ogre, The Defender of Key')
        print(self.key_chest.storage[0])

    def turtorial(self, character):
        map_turt = self.map_creation()
        self.actions = {'up':MoveUp(self, character),
                        'down':MoveDown(self, character),
                        'left':MoveLeft(self, character),
                        'right':MoveRight(self, character),
                        'equip':Equip(self, character),
                        'open chest':OpenChest(self, character),
                        'map':MapPrint(self),
                        'exit':Exit(),
                        'backpack':BackpackOutput(self, character)}
        self.chest()
        self.key_box()
        # self.turtorial_npc.say_any('Hello my blinded friend!')
        # self.turtorial_npc.say_any('I will help u, in this dark...')
        # character.say_any('Who are u???')
        # self.turtorial_npc.say_any('I\'m The BEN, black Lord.')
        # self.turtorial_npc.say_any('U are 0: ')
        self.map_output(map_turt)
        self.turtorial_npc.say_any('U can move on X, let\'s begin!')
        character.stats_update()
        while(True):
            direction = input()
            try:
                action = self.actions[direction]
                action.run()
            except KeyError:
                print('Unknown command.')
                pass
            self.map_output(map_turt)

