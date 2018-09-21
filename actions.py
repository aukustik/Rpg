from locations import *
class Command:
    def run(self):
        raise NotImplementedError

class MoveUp(Command):
    def __init__(self, level, character):
        self.level = level
        self.character = character
    def run(self):
        future_pos = []
        future_pos += self.level.char_pos[0], self.level.char_pos[1]
        if (future_pos[0] > 0):
            self.level.map_main[future_pos[0] - 1][future_pos[1]].event(self.character)
            self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = Road(self.level)
            self.level.char_pos[0] -= 1
            self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '0'
        else:
            print('You shall not path!!!')

class MoveDown(Command):
    def __init__(self, level, character):
        self.level = level
        self.character = character
    def run(self):
        future_pos = []
        future_pos += self.level.char_pos[0], self.level.char_pos[1]
        if (future_pos[0] < self.level.size - 1):
            self.level.map_main[future_pos[0] + 1][future_pos[1]].event(self.character)
            self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = Road(self.level)
            self.level.char_pos[0] += 1
            self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '0'
        else:
            print('You shall not path!!!')
class MoveLeft(Command):
    def __init__(self, level, character):
        self.level = level
        self.character = character
    def run(self):
        future_pos = []
        future_pos += self.level.char_pos[0], self.level.char_pos[1]
        if (future_pos[1] > 0):
            self.level.map_main[future_pos[0]][future_pos[1] - 1].event(self.character)
            self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = Road(self.level)
            self.level.char_pos[1] -= 1
            self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '0'
        else:
            print('You shall not path!!!')

class MoveRight(Command):
    def __init__(self, level, character):
        self.level = level
        self.character = character
    def run(self):
        future_pos = []
        future_pos += self.level.char_pos[0], self.level.char_pos[1]
        future_pos[1] += 1
        if (future_pos[1] < self.level.size):
            self.level.map_main[future_pos[0]][future_pos[1] + 1].event(self.character)
            self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = Road(self.level)
            self.level.char_pos[1] += 1
            self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '0'
        else:
            print('You shall not path!!!')

class Equip(Command):
    def __init__(self, level, character):
        self.character = character
        self.level = level

    def run(self):
        self.character.print_stats()

class OpenChest(Command):
    def __init__(self, level, character):
        self.character = character
        self.level = level
    
    def run(self):
        if (self.level.on_box == True):
            self.level.in_box(self.character)
        else:
            print('Nope.')

class MapPrint(Command):
    def __init__(self, level):
        self.level = level
    
    def run(self):
        self.level.map_output(self.level.map_turt)

class BackpackOutput(Command):
    def __init__(self, level, character):
        self.character = character
        self.level = level
    
    def run(self):
        self.character.show_backpack()

