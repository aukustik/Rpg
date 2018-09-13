from character import *
import random
class LevelTurtorial:
    def __init__(self, character):
        self.complete = False
        self.turtorial_npc = MainChar('Ben')
        self.char_pos = [5,3]
    def map_creation(self):
        size = 6
        boxes = 1
        self.map_main = [['X'] * size for i in range(size)]
        self.map_main[self.char_pos[0]][self.char_pos[1]] = '0'
        return self.map_main

    def map_output(self, map):
        for row in map:
            print(' '.join([str(elem) for elem in row]))


    def turtorial(self, character):
        map_turt = self.map_creation()
        self.turtorial_npc.say_any('Hello my blinded friend!')
        self.turtorial_npc.say_any('I will help u, in this dark...')
        character.say_any('Who are u???')
        self.turtorial_npc.say_any('I\'m The BEN, black Lord.')
        self.turtorial_npc.say_any('U are 0: ')
        self.map_output(map_turt)
        self.turtorial_npc.say_any('U can move on X, let\'s begin!')
        while(True):
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