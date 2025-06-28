class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    
class Paul(Cat):
    def sing(self, sounds):
        return f'{sounds}'



my_cats = []
cat1 = Simon('Simon', 10)
cat2 = Sally('sally', 9)
cat3 = Paul('Paul', 3)
my_cats.append(cat1)
my_cats.append(cat2)
my_cats.append(cat3)

my_pets = Pets(my_cats)

my_pets.walk()