# Predict what this will print:
for i in range(1, 5):
    for j in range(1, 4):
        print(i, j)


print('********************************')


for n in range(2):
    print("n=" + str(n))
    for m in range(5):
        print("   m=" + str(m))
    print("n=" + str(n))


print('********************************')


friends = ["philip", "abby", "phelipe", "simcha"]

for i in range(len(friends)):
    for j in range(len(friends)):
        print(friends[i], friends[j])


print('********************************')


locations = ["flatbush", "williamsburg", "bushwick", "greenpoint"]

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        print(locations[i], locations[j])


print('********************************')


colors = ["red", "purple", "orange"]

for color_str in colors:
    print(color_str)
    for char in color_str:
        print(char)
        
        
print('********************************')


# Write a function `pair_print(arr)` that accepts a list and prints all unique pairs
# of elements in the list. It doesn't need to return anything.

def pair_print(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i], arr[j])

# def pair_print(arr):
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             print(f"{arr[i]} - {arr[j]}")

# Example:
pair_print(["artichoke", "broccoli", "carrot", "daikon"])
# prints
# artichoke - broccoli
# artichoke - carrot
# artichoke - daikon
# broccoli - carrot
# broccoli - daikon
# carrot - daikon


# Write a function `print_combinations(arr1, arr2)` that accepts two lists.
# The function should print all combinations taking one element from the first list
# and one from the second list. It doesn't need to return anything.

def print_combinations(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            print(arr1[i], arr2[j])


# Example:
colors = ["gray", "cream", "cyan"]
clothes = ["shirt", "flannel"]
print_combinations(colors, clothes)
# prints:
# gray shirt
# gray flannel
# cream shirt
# cream flannel
# cyan shirt
# cyan flannel


# Write a function `two_sum(numbers, target)` that accepts a list of numbers and a target number.
# The function should return True if there exists a pair of distinct elements in the list that sum to the target.
# Otherwise, return False.

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
               return True
    return False

# Example:
two_sum([2, 3, 5, 9], 7) #-> True
two_sum([2, 3, 5, 9], 4) #-> False
two_sum([6, 3, 4], 10) #-> True
two_sum([6, 5, 1], 10) #-> False



#Example: Bubble sort:
def bubble_sort(arr):
    n = len(arr)
    # Outer loop to traverse through all array elements
    for i in range(n):
        swapped = False
        # Inner loop to compare adjacent elements
        # The last i elements are already in place (sorted)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # If no two elements were swapped by the inner loop,
        # then the list is already sorted, and we can stop
        if not swapped:
            break
    return arr
 
# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
print(f"Original list: {my_list}")
sorted_list = bubble_sort(my_list)
print(f"Sorted list: {sorted_list}")
