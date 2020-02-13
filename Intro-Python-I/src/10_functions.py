# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")  # returns a string
num = int(num)  # convert to an int for math computation

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

# defining function


def is_even(number):
    if number % 2 == 0:
        print("Even!")
    else:
        print("Odd")


# calling function
is_even(num)
