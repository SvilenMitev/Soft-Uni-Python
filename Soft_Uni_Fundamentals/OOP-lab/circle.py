class Circle:

    def __init__(self, diameter):
        self.diameter = diameter
        self.__pi = 3.14

    def calculate_circumference(self):
        circumference = self.__pi * self.diameter
        return circumference

    def calculate_area(self) :
        area = self.__pi * self.diameter ** 2 / 4
        return area
    def calculate_area_of_sector(self, angle):
        self.angle = angle
        sector = (self.angle/360) * self.__pi * (self.diameter/2)**2
        return sector

circle = Circle(10)
angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")


