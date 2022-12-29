def animal_leg_count(animals: list):
    for animal in animals:
        print(animal.leg_count())
        
animal_leg_count(animals)

class Animal:
    def leg_count(self):
        pass


class Lion(Animal):
    def leg_count(self):
        pass
