class Habitat:
    def __init__(self, name, climate, capacity):
        self.name = name
        self.climate = climate
        self.capacity = capacity
        self.animals = []

    def add_animal(self, animal):
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            return f"Success: Added {animal.name} to {self.name}."
        else:
            return f"Error: {self.name} is full! Cannot add {animal.name}."

    def roll_call(self):
        print(f"--- {self.name} Roll Call ---")
        if not self.animals:
            print("No animals here yet.")
        for animal in self.animals:
            print(f"- {animal.describe()} | Says: {animal.speak()} | Movement: {animal.move()}")

    def __str__(self):
        return f"[{self.climate}] {self.name} ({len(self.animals)}/{self.capacity})"