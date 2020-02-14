def double(x):  # being copied
    return x * 2


num = double(10)
val = double('something')

double(2)

print(num)  # 20
print(val)  # 'somethingsomething'

# define a doubling function, that doubles every element in a list


def double_list(li):  # li is being passed by reference, pointer
    for i in range(0, len(li)):
        li[i] *= 2


num_list = [1, 2, 3, 4, 5]
print(num_list)
double_list(num_list)
print(num_list)


def append_to_list(li, val):
    li.append(val)


append_to_list(num_list, 'something new')

print(num_list)

# pass a collection by value
num_list = [1, 2, 3, 4, 5]
print(num)

# ----------------------------------

# first pass solution


def centered_average(nums):
    min_num = nums[0]  # initializing min
    max_num = nums[0]  # initializing max
    total = 0  # running total
    for n in nums:
        total += n
        if n < min_num:
            min_num = n
        if n > max_num:
            max_num = n
    return (total - min_num - max_num) // (len(nums) - 2)


nums = [1, 2, 3, 4, 100]

centered_average(nums)

# second pass solution


def centered_optimized_average(nums):
    min_num = min(nums)
    max_num = max(nums)
    total_sum = sum(nums)
    return (total_sum - min_num - max_num) / (len(nums) - 2)
