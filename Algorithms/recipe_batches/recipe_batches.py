#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    counts = []
    # access key/value in recipe dict
    for name, value in recipe.items():
        print(f"recipe items, {name}, {value}")
        # check how much ingredients can be used according to recipe specs
        if name in ingredients:
            print(f"name is also in ingredient", {name})
            # add complete ingredient batch to counter
            counts.append(math.floor(ingredients[name] / value))
        else:
            counts.append(0)
    # check how many times each ingredient can be used
    print(counts)

    # see which ingredient can be used more than others

    # check counts array for any ingredient usable in more cycles than the other ingredients, if found, set equal to max batch

    # return max batch


recipe_batches({'milk': 100, 'butter': 50, 'cheese': 10},
               {'milk': 198, 'butter': 52, 'cheese': 10})

# Dict Notes - items() returns all dict keys with values

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = {'milk': 100, 'butter': 50, 'flour': 5}
#     ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
#         batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
