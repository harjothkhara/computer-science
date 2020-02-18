from category import Category


class Store:
    # constructor - initialize instance of class
    def __init__(self, name, categories=["toys", "food"]):
        # self.attribute = parameter
        self.name = name
        self.categories = categories

    def __str__(self):
        # return self.name
        output = f"Welcome to {self.name}!\n"
        i = 1
        for cat in self.categories:
            output += f"\n {i}. {cat}"
            i += 1
        return output


my_store = Store('Pets Unlimited', [Category('Toys', ['chew toy', 'cat nip', 'ball'])'Fish', 'Bedding/Cages', 'Food')]


print(my_store)
choice = int(input("Please choose a category (#): "))
print(choice)

# SHOULD add some error handling to our input parser
# ex. non-integer data, ints outside of (0-size_of_categories)
while choice != 0:
    print(my_store)
    choice = int(input("Please choose a category (#): "))
    print(choice)
print("Thanks for stopping by!")
