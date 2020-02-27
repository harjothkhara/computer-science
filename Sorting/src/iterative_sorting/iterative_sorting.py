# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)

        # TO-DO: swap

    return arr


# TO-DO:  implement the Bubble Sort function below

#           ✅     ✅    ✅   ✅   ✅ 
# # index    0      1     2     3    4
#     arr = [2,     3,    5,    6,   8]
#     #      |      |     |     |    |- 'sorted bubbled number'
#    i=3    j=0   j+1

#    swap = False


def bubble_sort(arr):
    # 1. Loop through your array
    # get index and loop through array -  no need to check end 'bubbled number'
    for i in range(0, len(arr)-1):
        # print(i)  # 0, 1, 2, 3,
        # iterate through list j times for every i so we catch every unsorted item
        # -i representes the index of the last moving unsorted item in list.
        for j in range(0, len(arr)-i-1):
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


bubble_sort(arr=[5,  2,  6,  3,  8])

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
