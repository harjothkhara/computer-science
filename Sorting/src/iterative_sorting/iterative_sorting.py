import random
# TO-DO: Complete the selection_sort() function below
# Selection Sort -  in-place comparison sort. During each iteration select the smallest item from the unsorted partition and move it to the the sorted partition. Sets the first unsorted item as the min and then scan through the rest of the items until it finds a new item less then the current min, if a new min is found, we set it equal to the min variable. Once we've finished scanning for a min during the current iteration, we check if the min index was changed from i (first value in the unsorted section) with a new min, if so we swap the item at the current index(i) with the smallest element, now set to the min variable.
# sorted |
# initial min
#                0      1      2     3    4
#         arr = [2,     3,     5,    6,   8]
#                |      |      |     |    |
#         i=3    ✅    ✅     ✅    ✅  #min (last element will naturally be sorted)
#                                         j
# c_min_index = 3


def selection_sort(arr):
    # Start with current index = 0
    # For all indices EXCEPT the last index:
    # loop through n-1 elements or repeat num of elements -1 times
    # after all iterations, the last element will naturally be sorted
    for i in range(0, len(arr) - 1):
        # set the first unsorted element as the min
        c_min_index = i  # tracking min index in each iteration of i
        # for each of the unsorted elements
        # scanning elements to the end of list for a min
        for j in range(i+1, len(arr)):
            # if element < current min
            if arr[j] < arr[c_min_index]:
                # finding and setting element as new min (if there is one)
                c_min_index = j  # swapping index
        # once we've looped through j, we check if our current min index changed
        # and swap min with first unsorted partition
        if c_min_index != i:  # swapping values
            # b. Swap the element at current index with the smallest element found in above loop
            arr[i], arr[c_min_index] = arr[c_min_index], arr[i]

    print(arr)

    # a. Loop through elements on right-hand-side of current index and find the smallest element

    # TO-DO: find next smallest element
    # (hint, can do in 3 loc)

    # TO-DO: swap


randomlist = random.sample(range(7, 76), 10)

print("selection sort")
selection_sort(arr=[5,  2,  6,  3,  8])

# time complexity(best,worst, average): n^2


# TO-DO:  implement the Bubble Sort function below

# Bubble Sort - Repeatedly steps through the list, compares adjacent elements (L > R), and swaps them if in wrong order.

# #         ✅     ✅    ✅   ✅  ✅
# # index    0      1     2    3    4
#     arr = [2,     3,    5    6,   8]
#     #      |      |     |     |    |- 'sorted bubbled number'
#    i=3     j=0   j+1

#    swap = True


def bubble_sort(arr):
    # 1. Loop through your array
    # get index and loop through array -  no need to check end 'bubbled number'
    for i in range(0, len(arr)-1):  # outer loop
        # print(i)  # 0, 1, 2, 3,
        # iterate through list j times for every i so we catch every unsorted item
        # -i representes the index of the last moving unsorted item in list.
        for j in range(0, len(arr)-i-1):  # inner loop
            #     - Compare each element to its neighbor
            if arr[j] > arr[j+1]:
               #     - If elements in wrong position (relative to each other, swap them)
                swap = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
# 2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
            else:
                swap = False
    print(arr)

# [2, 5, 3, 6, 8] <-- our list is not ordered yet (need to iterate through each list int and compare more then once). need to do a nested for loop

# [2, 3, 5, 6, 8] < --- our list is now ordered after adding the nested loop


randomlist = random.sample(range(7, 76), 10)

print("bubble sort")
bubble_sort(arr=[5,  2,  6,  3,  8])

# time complexity(best=n,worst, average): n^2


# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
