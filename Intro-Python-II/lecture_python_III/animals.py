class Animal:
    # constructor
    def __init__(self, skin_type, species, weight, color, name, environment):
        # instance attributes
        self.skin_type = skin_type
        self.species = species
        self.weight = weight
        self.color = color
        self.name = name
        self.environment = environment

    def move(self):
        print(f"???")

    def speak(self):
        print('???')


# instantiate new object
a = Animal("furry", "DOG", 12, "brown", "fido", "LAND")
a.move()  # fido walks
a.speak()  # ???

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


#  new object instance
d = Dog('rover', 15, "black")
d.move()  # rover walks
d.speak()  # woof

# another object instance
d2 = Dog('king', 35, "spotted")
d2.move()
d2.speak()
