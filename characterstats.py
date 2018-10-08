

class Attributes:
    def set(self):
        raise NotImplementedError
    
    def get(self):
        raise NotImplementedError

class CharHealth(Attributes):
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = self.max_health
    
    def set(self, value):
        self.current_health += value
        if (value > self.max_health):
            self.current_health = self.max_health

    def set_max(self, value):
        self.max_health =+ value
    
    def get(self):
        return self.current_health
    
    def get_max(self):
        return self.max_health

class CharMana(Attributes):
    def __init__(self, max_mana):
        self.max_mana = max_mana
        self.current_mana = self.max_mana
    
    def set(self, value):
        self.current_mana += value
        if (value > self.max_mana):
            self.current_mana = self.max_mana
    
    def set_max(self, value):
        self.max_mana += value
    
    def get(self):
        return self.current_mana
    
    def get_max(self):
        return self.max_mana

class CharStamina(Attributes):

    def __init__(self, max_stamina):
        self.max_stamina = max_stamina
        self.current_stamina = self.max_stamina
    
    def set(self, value):
        self.current_stamina = value
        if (value > self.max_stamina):
            self.current_stamina = self.max_stamina
    
    def set_max(self, value):
        self.max_stamina = value
    
    def get(self):
        return self.current_stamina

    def get_max(self):
        return self.max_stamina

class CharExpirience(Attributes):

    def __init__(self):
        self.exp = 0

    def set(self, value):
        self.exp =+ value
    
    def get(self):
        return self.exp

class Stats:
    def __init__(self, max_health, max_mana, max_stamina):
        self.health_attr = CharHealth(max_health)
        self.mana_attr = CharMana(max_mana)
        self.stamina_attr = CharStamina(max_stamina)
        self.exp_attr = CharExpirience()