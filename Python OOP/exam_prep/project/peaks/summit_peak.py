from base_peak import BasePeak

class SummitPeak(BasePeak):
    def __init__(self,  name: str, elevation: int):
        self.name = name
        self.elevation = elevation

        
        
    def get_recommended_gear(self):
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]
    
    def calculate_difficulty_level(self):
        if self.elevation >= 2500:
            return "Extreme"
        elif self.elevation <= 2500 and self.elevation >= 1500:
            return "Advanced"
