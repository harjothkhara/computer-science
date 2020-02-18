class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # Methods
    def greeting(self):
        return f"My name is {self.name} and I am {self.age}"

    def has_birthday(self):
        self.age += 1


# object instance - Init user object
myObject = User('Harjoth Khara', 'harjoth.khara@gmail.com', 33)
# creating object from the User class
print(type(myObject), myObject)
# <class '__main__.User'> <__main__.User object at 0x1011ad150>
print(myObject.name, myObject.email, myObject.age)
# Harjoth Khara, harjoth.khara@gmail.com, 33
print(myObject.greeting())
# My name is Harjoth Khara and I am 33
myObject.has_birthday()
# ^^^ invoke method (return nothing) on object instance
print(myObject.greeting())
# My name is Harjoth Khara and I am 34


# Extend class - Customer extends User
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0  # <---- added attribute

    # Methods
    def set_balance(self, balance):  # <--- added method
        self.balance = balance

    def greeting(self):  # <--- overwriting User method
        return f"My name is {self.name} and I am {self.age} and my balance is {self.balance}"


# object instance - Init Customer object
customer_Object = Customer('Janet Smith', 'janet@gmail.com', 25)
print(customer_Object.name)  # Janet Smith
customer_Object.set_balance(500)
# we can still access methods from the parent User class
print(customer_Object.greeting())
# 'My name is Janet Smith and I am 25' BUT if I now uncomment greeting() with the additional balance attribute we can overite the existing greeting method: 'My name is Janet Smith and I am 25 and my balance is 500'
