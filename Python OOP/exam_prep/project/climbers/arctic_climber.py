from base_climber import BaseClimber
from peaks.base_peak import BasePeak

class ArcticClimber(BaseClimber):
    def __init__(self, name):
        self.name = name
        self.strength = 200

    def can_climb(self):
        if self.strength >= 100:
            return True
        else:
            return False
    def climb(self, peak: BasePeak):
        if self.difficulty_level == "Extreme":
            self.strength -+ 20*2
        else:
            self.strength -= 20*1.5
            self.conquered_peaks.append(peak)
        
