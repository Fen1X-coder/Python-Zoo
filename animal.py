from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"

    def move(self):
        return "runs on four legs."

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name, "Bird")
        self.can_fly = can_fly

    def speak(self):
        return "Chirp!"

    def move(self):
        if self.can_fly:
            return "flies through the air."
        else:
            return "waddles on the ground."

class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name, "Fish")
        self.water_type = water_type

    def speak(self):
        return "Glub Glub!"

    def move(self):
        return "swims in the water."