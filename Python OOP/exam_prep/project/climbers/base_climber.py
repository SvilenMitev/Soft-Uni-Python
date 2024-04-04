from peaks.base_peak import BasePeak

class BaseClimber:
    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks = []
        self.is_prepared = True
    
    def can_climb():
        pass
    def climb(self, peak: BasePeak):
        pass

    def rest(self):
        self.strength += 15
    def __str__(self):
        return f"{type(self).__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered "  f" peaks: {', '.join(self.conquered_peaks)} ///"

