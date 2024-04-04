from base_peak import BasePeak

class ArcticPeak(BasePeak):
    def __init__(self,  name: str, elevation: int):
        self.name = name
        self.elevation = elevation

        
        
    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]
    
    def calculate_difficulty_level(self):
        if self.elevation >= 3000:
            return "Extreme"
        elif self.elevation <= 3000 and self.elevation >= 2000:
            return "Advanced"

        