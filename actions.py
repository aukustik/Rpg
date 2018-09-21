class Command:
    def run(self):
        raise NotImplementedError

class MoveUp(Command):
    def __init__(self, level):
        self.level = level
    
    def run(self):
        self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '|'
        self.level.char_pos[0] -= 1
        self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '0'

class MoveDown(Command):
    def __init__(self, level):
        self.level = level
    
    def run(self):
        self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '|'
        self.level.char_pos[0] += 1
        self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '0'

class MoveLeft(Command):
    def __init__(self, level):
        self.level = level
    
    def run(self):
        self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '-'
        self.level.char_pos[1] -= 1
        self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '0'

class MoveRight(Command):
    def __init__(self, level):
        self.level = level
    
    def run(self):
        self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '-'
        self.level.char_pos[1] += 1
        self.level.map_main[self.level.char_pos[0]][self.level.char_pos[1]] = '0'

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