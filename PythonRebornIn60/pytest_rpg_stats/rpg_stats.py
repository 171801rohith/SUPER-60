def generate_strength():
    return 5 

def is_stat_valid(stat_value):
    return True if stat_value >= 1 and stat_value<= 10 else False

class Character:
    def __init__(self, strength, intelligence, dexterity):
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity

    def get_combat_readiness(self):
        return self.strength + self.dexterity