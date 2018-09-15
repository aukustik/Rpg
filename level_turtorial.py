from character import *
import random
class LevelTurtorial:
    def __init__(self, character):
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
    
    def show_chest(self):
        for i in self.treasure_box.storage:
            print(i.info())

    def turtorial(self, character):
        map_turt = self.map_creation()
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
            if (direction == 'up'):
                self.map_main[self.char_pos[0]][self.char_pos[1]] = '|'
                self.char_pos[0] -= 1
                self.map_main[self.char_pos[0]][self.char_pos[1]] = '0'
                self.map_output(map_turt)
            if (direction == 'down'):
                self.map_main[self.char_pos[0]][self.char_pos[1]] = '|'
                self.char_pos[0] += 1
                self.map_main[self.char_pos[0]][self.char_pos[1]] = '0'
                self.map_output(map_turt)
            if (direction == 'left'):
                self.map_main[self.char_pos[0]][self.char_pos[1]] = '-'
                self.char_pos[1] -= 1
                self.map_main[self.char_pos[0]][self.char_pos[1]] = '0'
                self.map_output(map_turt)
            if (direction == 'right'):
                self.map_main[self.char_pos[0]][self.char_pos[1]] = '-'
                self.char_pos[1] += 1
                self.map_main[self.char_pos[0]][self.char_pos[1]] = '0'
                self.map_output(map_turt)
            if (direction == 'equip'):
                character.print_stats()
            if (direction == 'map'):
                self.map_output(map_turt)
            if (direction == 'exit'):
                return False
            if (direction == 'open chest'):
                self.show_chest()
        
