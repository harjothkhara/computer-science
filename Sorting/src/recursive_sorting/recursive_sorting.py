# Merge Sort

# merge sort helper function yo merge 2 sorted arrays
# arrA and arrB must be sorted!


def merge(arrA, arrB):  # putting back together part
    # merging two sorted arrays back together
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements  # performance
    # start merging your single lists of one element together into larger, sorted sets
    # Repeat above until the entire data set has been assembled
    a_i = 0  # a_i is the current index of arrA (counter)
    b_i = 0  # b_i is the current index for arrB
    # for each index in the merged array `elements`...
    # Find the smallest first-item between arrA and arrB
    # Add that to `elements` at the given index
    # Increment the a/b counter

    return merged_arr

    a_i = 2  # a_i is the current index of arrA
    b_i = 0  # b_i is the current index for arrB
    i = 2  # i is the index of the new merging-into array

    arrA[a_i] < arrB[b_i]
    [1, 2, 3][4, 5, 6]

    [1,     2,        3,   None, None, None]
    | | | | | |
    i = 0     i = 1     i = 2      i     i    i

    # at i = 0 in the merging-into-array we compare sub arrays arrA[a] and arrB[b]

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):  # spliting part
    # basecase - while your dataset container more than one item split it in half
    # once you have gotton down to a single element, you have sorted that element (a single element cannot be out of order)
    print(arr)
    if len(arr) == 1:
        return arr[0]
    # logic
    if len(arr) > 1:  # Split
        #print(arr) [39, 51, 7, 14, 3, 86]
        pivot = round(len(arr)/2)
        # Divide LHS and RHS
        left_arr = arr[:pivot]
        #print(left) [39, 51, 7]
        right_arr = arr[pivot:]
        #print(right) [14, 3, 86]
        # recursively run merge_sort and sort each of the split arrays
        sorted_left = merge_sort(left_arr)
        sorted_right = merge_sort(right_arr)
        # merge the sorted arrays
        arr = merge(sorted_left, sorted_right)
    return arr

    # recursively call merge_sort() on LHS, # recursively call merge_sort() on RHS


arr1 = [39, 51, 7, 14, 3, 86]
merge_sort(arr1)

# once you have gotton down to a single element, you have sorted that element.
# a single element cannot be "out of order".
# once we've split and sorted the array to a single element only then do we return them to the merge function to be merged


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
