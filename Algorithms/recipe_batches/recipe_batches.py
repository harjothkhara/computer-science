#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    counts = []
    # access key/value in recipe dict
    for name, value in recipe.items():
        # check how much ingredients can be used according to recipe specs
        if name in ingredients:
            # add complete ingredient batch to counter
            counts.append(math.floor(ingredients[name] / value))
        else:
            counts.append(0)
    # check how many times each ingredient can be used
    # print(counts)

    # see which ingredient can be used more than others by checking max value (any ingredient cycle more than others?) in counts array
    max_batches = max(counts)

    # check counts array for any ingredient usable in more cycles than the other ingredients, if found, set equal to max batch
    for count in counts:
        if count < max_batches:
            max_batches = count

    # return max batch
    return max_batches

# Dict Notes - items() returns all dict keys with values


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
