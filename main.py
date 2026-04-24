"""
Python Zoo assignment
Zach Harriz | 4/24/26

"""



from animal import Dog, Bird, Fish
from habitat import Habitat
from zoo import Zoo
from zookeeper import Zookeeper

def main():
    # 1. Create Animals (1 Dog, 2 Birds, 1 Fish)
    rex = Dog("Rex", "Golden Retriever")
    tweety = Bird("Tweety", can_fly=True)
    pete = Bird("Penguin Pete", can_fly=False)  # Bird that cannot fly
    nemo = Fish("Nemo", "Saltwater")

    # 2. Create Habitats (Savanna, Aviary, Aquarium)
    savanna = Habitat("Savanna Exhibit", "tropical", 5)
    aviary = Habitat("Sky Dome Aviary", "temperate", 10)
    aquarium = Habitat("Deep Blue Aquarium", "aquatic", 20)

    # 3. Add animals to habitats
    savanna.add_animal(rex)
    aviary.add_animal(tweety)
    aviary.add_animal(pete)
    aquarium.add_animal(nemo)

    # 4. Create one zoo and add all habitats
    city_zoo = Zoo("Hexworth Wildlife Park")
    city_zoo.add_habitat(savanna)
    city_zoo.add_habitat(aviary)
    city_zoo.add_habitat(aquarium)

    # 5. Create at least one zookeeper and assign a habitat
    sara = Zookeeper("Sara", "Birds")
    sara.assign(aviary)
    city_zoo.hire_keeper(sara)

    # 6. Run the final reports
    city_zoo.full_report()
    sara.daily_report()

    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()