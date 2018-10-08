from character import Character

class Spells:
    def cast(self):
        raise NotImplementedError

class Fireball(Spells):
    def __init__(self, character):
        self.damage = 1
        self.manacost = 10
        self.character = character

    def cast(self, target):
        
        self.damage = int(self.character.stats['MagicPower']) * self.damage
        target.stats['CurrentHealth'] -= self.damage
        self.character.stats['CurrentMana'] -= self.manacost
        print(self.character.name, 'casts Fireball, and deal', self.damage, 'damage to', target.name)
    
class IceBlast(Spells):
    def __init__(self, character):
        self.damage = 1
        self.manacost = 10
        self.character = character
    
    def cast(self, target):
        self.damage = int(self.character.stats['MagicPower']) * self.damage
        target.stunned['state'] = True
        target.stunned['duration'] = 1
        target.stats['CurrentHealth'] -= self.damage
        self.character.stats['CurrentMana'] -= self.manacost
        print(self.character.name, 'casts IceBlast, and deal', self.damage, 'damage to', target.name)

