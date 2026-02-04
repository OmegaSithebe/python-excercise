# numbers = []
# for i in range(1, 6):
#     numbers.append(i*2)
    
# print(numbers)


print('New way using one line:')
numbers = [i*2 for i in range(1,6)]
print(numbers)


#With Conditions
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(even_numbers)


#Tuple comprehension
t = (i * 2 for i in range(1, 6))
print(t)
print(type(t))


t = tuple(i * 2 for i in range(1, 6))
print(t)


#Set comprehension
numbers = [1, 2, 2, 3, 3, 4]

unique_numbers = {i for i in numbers}
print(unique_numbers)


#with condition
odd_set = {i for i in range(1, 10) if i % 2 != 0}
print(odd_set)


#Dictionary comprehension
squares = {i: i * i for i in range(1, 6)}
print(squares)


#filter dictionary
scores = {
    'Ram':85,
    'Shyam':72,
    'Hari':90
}

passed = {name: marks for name, marks in scores.items() if marks >= 80}
print(passed)


#String comprehension
word = 'Python'

letters = [ch.upper()for ch in word]
print(letters)


#Comparison Table:
#List -> [x for x in data] -> [1, 4, 9] -> When order matters or duplicates allowed
#Tuple -> tuple(x for x in data)
#Set -> {x for x in data} -> {1, 4, 9} -> When you want unique values only
#Dict -> {k:v for k, v in data} : {key: value ...} -> {1:1, 2:8} -> When you need key value pairs




#Homework for students
# 1. Create a list of squares of even numbers from 1 to 20
# 2. Convert a list into a set using comprehension
# 3. Create a dictionary of numbers and their cubes

#Pracice 1
new_list = [i * i for i in range(1, 21) if i % 2 == 0]
print(new_list)


#Practice 2
new_set = {i * i for i in range(1, 21) if i % 2 == 0}
print(new_set)


#Practice 3
new_dict = {v: v**3 for v in range(1, 21)}
print(new_dict)


#Extra Exercises:
#1. List Comprehension — With Filtering
word = "Nkosingiphile"
vowels = [ch for ch in word if ch.lower() in 'aeiou']
print(vowels)

#Example: Numbers that are divisible by BOTH 2 and 3
nums = [i for i in range(1, 51) if i % 2 == 0 and i % 3 == 0]
print(nums)

#2. List Comprehension — With Multiple if Conditions
nums = [i for i in range(1, 31) if i > 10 if i % 5 == 0]
print(nums)

result = []
for i in range(1, 31):
    if i > 10:
        if i % 5 == 0:
            result.append(i)
            
#3. Set Comprehension — Remove duplicates from a list
items = [1, 3, 1, 5, 3, 7]
unique_items = {i for i in items}
print(unique_items)

#Example: Unique first letters of words
words = ["apple", "alive", "ball", "bat", "boy"]
letters = {w[0] for w in words}
print(letters)


#4. Dictionary Comprehension — Mapping Key → Value
squares = {n: n*n for n in range(1, 11)}
print(squares)

#Example: Convert two lists into a dictionary
names = ["Gwen", "Robert", "Siya"]
marks = [77, 85, 88]

student_marks = {name: mark for name, mark in zip(names, marks)}
print(student_marks)

#Example: Reverse dictionary (value → key)
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)


#5. Conditionals inside a comprehension (ternary operator)
labels = {i: ("Even" if i % 2 == 0 else "Odd") for i in range(1, 11)}
print(labels)

#6. Nested List Comprehension (double loops)
pairs = [(i, j) for i in range(1, 4) for j in range(1, 4)]
print(pairs)

pairs = []
for i in range(1, 4):
    for j in range(1, 4):
        pairs.append((i, j))

#Example: Flatten a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat = [num for row in matrix for num in row]
print(flat)

#7. Nested Dictionary Comprehension
table = {
    n: {"square": n*n, "cube": n**3}
    for n in range(1, 6)
}
print(table)

#The Differences
#List -> [expression for item in iterable] -> ordered list, allow duplicates
#Set -> {expression for item in iterable} -> unordered, unique values only
#Dictionary -> {key: value for item in iterable} -> key - value mapping
