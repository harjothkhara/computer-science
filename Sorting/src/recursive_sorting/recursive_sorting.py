# Merge Sort [watch: https://www.youtube.com/watch?v=XaqR3G_NVoo]
# Python Tutor is your best friend for this one!

# merge sort helper function yo merge 2 sorted arrays
# arrA and arrB must be sorted!


def merge(arrA, arrB):  # putting back together part
    print(f"MERGE, {arrA} - {arrB}")
    # merging two sorted arrays back together
    num_elements = len(arrA) + len(arrB)
    merged_arr = [None] * num_elements  # performance
    # start merging your single lists of one element together into larger, sorted sets
    # Repeat above until the entire data set has been assembled
    a_i = 0  # a_i is the current index of arrA (counter)
    b_i = 0  # b_i is the current index for arrB
    # for each index in the merged array `elements`...
    for i in range(0, num_elements):
      # Find the smallest first-item between arrA and arrB
      # Add that to `elements` at the given index
      # Increment the a/b counter
      # Cases:
        if a_i >= len(arrA):
          # 1. A is empty, B is not empty # error checking for 3.
            merged_arr[i] = arrB[b_i]
            b_i += 1
        elif b_i >= len(arrB):
          # 2. B is empty, A is not empty # error checking for 4.
            merged_arr[i] = arrA[a_i]
            a_i += 1
        elif arrA[a_i] < arrB[b_i]:
          # 3. A has the smaller element
            merged_arr[i] = arrA[a_i]
            a_i += 1
        else:  # arrB[b_i] < arrA[a_i]
          # 4. B has the smaller element
            merged_arr[i] = arrB[b_i]
            b_i += 1
    return merged_arr

    # a_i = 2  # a_i is the current index of arrA
    # b_i = 0  # b_i is the current index for arrB
    # i = 2  # i is the index of the new merging-into array

    # arrA[a_i]   <     arrB[b_i]
    # [1,2,3]           [4,5,6]

    # [1,     2,        3,   None, None, None ]
    #  |      |         |      |     |    |
    # i=0     i=1     i=2      i     i    i

    # at i = 0 in the merging-into-array we compare sub arrays arrA[a] and arrB[b]


def merge_sort(arr):  # spliting part
    # basecase - while your dataset container more than one item split it in half
    # once you have gotton down to a single element, you have sorted that element (a single element cannot be out of order)
    # print(arr)
    # if len(arr) == 1:
    #     return arr[0]
    # logic
    print(f"MERGE SORT, {arr}")
    if len(arr) > 1:  # Split
        # print(arr) [39, 51, 7, 14, 3, 86]
        pivot = len(arr)//2
        # Divide LHS and RHS
        left_arr = arr[:pivot]
        # print(left) [39, 51, 7]
        right_arr = arr[pivot:]
        # print(right) [14, 3, 86]
        # recursively run merge_sort and sort each of the split arrays
        sorted_left = merge_sort(left_arr)
        sorted_right = merge_sort(right_arr)
        # merge the sorted arrays
        arr = merge(sorted_left, sorted_right)  # defined above
    return arr

    # recursively call merge_sort() on LHS, # recursively call merge_sort() on RHS


arr1 = [39, 51, 7, 14, 3, 86]
arr2 = merge_sort(arr1)
print(arr2)


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
