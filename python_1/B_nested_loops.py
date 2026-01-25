# Write a function `print2d(matrix)` that accepts a 2D list and prints all inner elements.

def print2d(matrix):
    for items in matrix:
        for char in items:
            print(char)

array1 = [
    ["a", "b", "c", "d"],
    ["e", "f"],
    ["g", "h", "i"]
]

print2d(array1)
# prints:
# a
# b
# c
# d
# e
# f
# g
# h
# i

array2 = [[9, 3, 4], [11], [42, 100]]
print2d(array2)
# prints:
# 9
# 3
# 4
# 11
# 42
# 100



# Write a function `make_matrix(m, n, value)` that returns a 2D list of m rows and n columns
# filled with `value`.

def make_matrix(m, n, value):
    new_list = []
    
    for i in range(m):
        row = []
        for j in range(n):
            row.append(value)
        new_list.append(row)
    return new_list

print(make_matrix(3, 5, None))
print(make_matrix(4, 2, "x"))
print(make_matrix(2, 2, 0))

# Example [
#  [None, None, None, None, None],
#  [None, None, None, None, None],
#  [None, None, None, None, None]
#  ]


# Write a function `total_product(matrix)` that returns the product of all numbers in a 2D list.

def total_product(matrix):
    product = 1
    for i in matrix:
        for j in i:
            product *= j
    return product
   

array1 = [[3, 5, 2], [6, 2]]
array2 = [[4, 6], [2, 3], [1, 2]]

print(total_product(array1))  # 360
print(total_product(array2))  # 288



# Write a function `two_sum_pairs(numbers, target)` that returns all unique pairs from
# numbers that sum to target.

def two_sum_pairs(numbers, target):
    new_list = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                new_list.append([numbers[i], numbers[j]])
    return new_list
   

print(two_sum_pairs([2, 3, 4, 6, 5], 8))  # [[2, 6], [3, 5]]
print(two_sum_pairs([10, 7, 4, 5, 2], 12))  # [[10, 2], [7, 5]]
print(two_sum_pairs([3, 9, 8], 11))  # [[3, 8]]
print(two_sum_pairs([3, 9, 8], 10))  # []



# Write a function `zipper(list1, list2)` that returns a 2D list containing pairs of elements at
# the same indices. Assume lists have same length.

def zipper(list1, list2):
    new_list = []
    
    # for i in list1:
    #     for j in range(i+1, len(list2)):
    #         new_list.append([[i], [j]])
    # return new_list

    for i in range(len(list1)):
        new_list.append([list1[i], list2[i]])
    return new_list

array1 = ["a", "b", "c", "d"]
array2 = [-1, -2, -3, -4]
print(zipper(array1, array2))

array3 = ["whisper", "talk", "shout"]
array4 = ["quiet", "normal", "loud"]
print(zipper(array3, array4))


# Example Usage:
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 92, 78]

# [['Alice', 85], ['Bob', 92], ['Charlie', 78]]