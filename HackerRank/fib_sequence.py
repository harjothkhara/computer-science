# Fib sequence begins with fib(0) = 0 and fib(1) = 1
# as its first and second terms. After these two
# elements, each subsequent element is equaly to the
# sum of the previous two elements
# fib(0) = 0, fib(1) = 1, fib(2) = fib(n-1)+fib(n-1)...
# complete the recursion function fib. it must
# return the nth element in the fib sequence

# attempt 1


def fibonacci(n):
    # basecase
    if n == 0:  # fib(0) = 0
        return 0
    if n == 1:  # fib(1) = 1
        return 1
    # recursive call
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(4) # 3


# attempt 2 - use dynamic programming
# (check for already computed fib value)
# goal: return arr that finds the fib path leading up to n
 # fib(0),fib(1), fib(2), fib(3)
       |     |     |       |
# e.g [0,    1,    1,      2]

# fib sequence leading upto, but not including fib(n) - fib sequence to get to n
arr = [0, 1] # # stores fib values for fib(0),fib(1) for easy retrieval ...
             # instead of recursively calling fib(0) and fib(1) again, and saving on memory
def fibonacci(n):
    # basecase
    if n <= len(arr):
      return arr[n-1]
    # recursive call
    else:
        temp = (fibonacci(n-1) + fibonacci(n-2))
        arr.append(temp)
        return temp

fibonacci(4)

# resources: https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/
# https://www.mathsisfun.com/numbers/fibonacci-sequence.html
