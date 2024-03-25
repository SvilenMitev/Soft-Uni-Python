class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def get_area(self):
        return self.width * self.height
    
a1 = ImageArea(7, 10)
a2 = ImageArea(35, 2)
a3 = ImageArea(8, 9)
print(a1 == a2)
print(a1 != a3)
