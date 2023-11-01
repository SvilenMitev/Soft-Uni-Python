class Zoo:
    __animals = 0
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals += 1
        self.name = name
        if species == 'mammal':
            self.mammals.append(self.name)
        if species == 'fish':
            self.fishes.append(self.name)
        if species == 'bird':
            self.birds.append(self.name)

    def get_info(self,species):
        if species == 'mammal':
            return f"Mammals in {self.zoo_name}: {', '.join(self.mammals)} \nTotal animals: {self.__animals}"

        if species == 'fish':
            return f"Fishes in {self.zoo_name}: {', '.join(self.fishes)} \nTotal animals: {self.__animals}"
        if species == 'bird':
            return f"Birds in {self.zoo_name}: {', '.join(self.birds)} \nTotal animals: {self.__animals}"

zoo_name = input()
zoo = Zoo(zoo_name)
count = int(input())

for i in range(count):
    animal = input().split(" ")
    species = animal[0]
    name = animal[1]
    zoo.add_animal(species, name)


info = input()
print(zoo.get_info(info))