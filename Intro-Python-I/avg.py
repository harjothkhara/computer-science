# Return the "centered" average of an array of ints, which we'll say is the mean
# average of the values, except ignoring the largest and smallest values in the array


# centered_average([1,2,3,4,100]) -> 3
sum([2, 3, 4]) / 3

# centered_average([1,1,5,5,10,8,7]) -> 5
sum([1, 5, 5, 8, 7]) // 5

# centered_average([-10,-4,-2,-4,-2,0]) -> -3
sum([-4, -2, -4, -2]) // 4

# Plan: sort the list, remove min and max value, then take the average of the remaining ints


def centered_avg(ints):
    # don't mutate original list
    ints_copy = ints.copy()
    # sort the ints
    ints_copy.sort()  # expensive sort nlogn2
    # slice off the first and last value
    ints_copy = ints_copy[1:-1]
    # sum the remaining values and divide by the length of the list
    avg = sum(ints_copy) // len(ints_copy)
    return avg


def centered_avg_semi_optimized(ints):
    # Find the max and min value
    smallest = min(ints)
    largest = max(ints)
    # Remove max and min
    ints.remove(smallest)
    ints.remove(largest)
    # Find sum of new array // length of new array
    return sum(ints) // len(ints)


def centered_avg_optimized(ints):
    # helps us initialize for first number. also, ints[0]
    largest = float("-inf")
    # helps us initialize for first number. also, ints[0]
    smallest = float("inf")
    total = 0
    # for integer in ints
    for i in ints:
        # If the integer is smaller than min, set min to the int
        if i < smallest:
            smallest = i
        # If the integer is larger than max, set max to the int
        if i > largest:
            largest = i
        # Keep running total of the sum
        total += i  # total = total + i -> increment total by i
    # Return the sum minus largest and smallest divided by the length - 2
    return (total - largest - smallest) // (len(ints) - 2)

# computational efficient since we're doing this in one pass ^^ its 5
# and without mutating our original values
