from abc import ABC, abstractmethod


class Animal(ABC):
    # constructor
    def __init__(self, skin_type, species, weight, color, name, environment):
        # instance attributes
        self.skin_type = skin_type
        self.species = species
        self.weight = weight
        self.color = color
        self.name = name
        self.environment = environment

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def speak(self):
        pass


# Create a subclass if you see a lot of repetition i.e species


class Dog(Animal):
    def __init__(self, name, weight, color):  # unique to Dog
        # inherit from super class
        super().__init__("fur", "DOG", weight, color, name, "LAND")

    # overiding speak method from super class
    def speak(self):
        print("woof")

    # overiding move method from super class
    def move(self):
        print(f"{self.name} walks")


# instantiate new object - won't work until methods are filled out otherwise you get an error: 'Can't instantiate abstract class Animal with abstract methods move, speak'
#a = Animal("furry", "DOG", 12, "brown", "fido", "LAND")

#  new instance (object)
d = Dog('rover', 15, "black")
d.move()  # rover walks
d.speak()  # woof

# another instance (object)
d2 = Dog('king', 35, "spotted")
d2.move()  # king walks
d2.speak()  # woof
