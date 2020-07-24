# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting&isFullScreen=true

# Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

# Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
# First Element: firstElement, where  is the first element in the sorted array.
# Last Element: lastElement, where  is the last element in the sorted array.

# Complete the countSwaps function below.
def countSwaps(arr):
    swaps = 0
    # outer loop that scans the full array (after each iteration of i the highest number on most left bubbles to right end side)
    for i in range(len(arr)):
    # inner loop that checks for swaps - no need to check last item in the array as if a previous int was larger then current then it would have already been bubbled to the right
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swaps+=1
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {arr[0]}")
    print(f"Last Element: {arr[-1]}")

# worst case: 0(n**2). best case: o(n) already sorted