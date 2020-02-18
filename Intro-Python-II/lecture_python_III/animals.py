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

    def move(self):  # movement defined locally
        if self.environment == 'WATER':
            movement = 'swims'
        elif self.environment == 'AIR':
            movement = 'flies'
        else:
            movement = 'walks'
        print(f"{self.name} {movement}")

    def speak(self):  # sound defined locally
        if self.species == 'DOG':
            sound = 'woof'
        elif self.species == 'CAT':
            sound = 'meow'
        elif self.species == 'BIRD':
            sound = 'tweet'
        else:
            sound = '???'
        print(sound)


# instantiate new object
a = Animal("furry", "DOG", 12, "brown", "fido", "LAND")
a.move()  # fido walks
a.speak()  # woof

# Create a subclass if you see a lot of repetition i.e species


class Dog(Animal):
    def __init__(self, name, weight, color):  # unique to Dog
        # inherit from super class
        super().__init__("fur", "DOG", weight, color, name, "LAND")


# instantiate new object
d = Dog('rover', 15, "black")
d.move()  # rover walks
d.speak()  # woof
