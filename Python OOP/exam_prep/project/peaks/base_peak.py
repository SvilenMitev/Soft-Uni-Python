

class BasePeak:
    def __init__(self, name: str, elevation:int,):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = calculate_difficulty_level()

    def get_recommended_gear(self):
        return self.recommended_gear
    
    def calculate_difficulty_level():
        pass
        
