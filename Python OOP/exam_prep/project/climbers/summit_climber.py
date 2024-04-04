from base_climber import BaseClimber
from peaks.base_peak import BasePeak

class SummitClimber(BaseClimber):
    def __init__(self, name):
        self.name = name
        self.strength = 150

    def can_climb(self):
        if self.strength >= 75:
            return True
        else:
            return False
    def climb(self, peak: BasePeak):
        if self.difficulty_level == "Advanced":
            self.strength -+ 30*1.3
        else:
            self.strength -= 30*2.5
            self.conquered_peaks.append(peak)
        
