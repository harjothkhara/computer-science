# Merge Sort
def merge_sort(arr):
  # basecase
    if len(arr) == 1:
        return arr[0]
  # logic
    if len(arr) > 1:
        #print(arr) [39, 51, 7, 14, 3, 86]
        pivot = round(len(arr)/2)
        # Divide LHS and RHS
        left = arr[:pivot]
        #print(left) [39, 51, 7]
        right = arr[pivot:]
        #print(right) [14, 3, 86]
    # recursively call merge_sort() on LHS, # recursively call merge_sort() on RHS


arr = [39, 51, 7, 14, 3, 86]
merge_sort(arr)

# once you have gotton down to a single element, you have sorted that element.
# a single element cannot be "out of order".
# once we've split and sorted the array to a single element only then do we return them to the merge function to be merged

# TO-DO: complete the helpe function below to merge 2 sorted arrays


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    return arr


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
