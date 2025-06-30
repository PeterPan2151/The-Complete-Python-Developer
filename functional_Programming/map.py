# map, filter, zip, reduce functions
# map
# def multiply_by2(item):
#     return item * 2

# print(list(map(multiply_by2, [1, 2, 3])))

# Filter
my_list = [1, 2, 3]
def check_odd(item):
    return item % 2 == 1

print(list(filter(check_odd, my_list)))

# Zip
# your_list = [10, 20, 30]
# thier_list = [5, 4, 3]
# print(list(zip(your_list, my_list, thier_list)))

# reduce
from functools import reduce

def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, my_list, 0))
