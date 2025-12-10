#List in Python
list = empty = [] #empty list
print("Empty List:", empty)

list = ["dev", 123, 45.67, True] #list with mixed data types 'Can also add dictionary, tuple, set as elements' in the list
print("List with mixed data types:", list) #['dev', 123, 45.67, True]

print()
#indexing and Slicing
sample_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Original List:", sample_list)  #['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Element at index 2:", sample_list[2])  #'c'
print("Elements from index 1 to 4:", sample_list[1:5])  #['b', 'c', 'd', 'e']
print()
print("Elements from start to index 3:", sample_list[:4])  #['a', 'b', 'c', 'd']
print("Elements from index 3 to end:", sample_list[3:])  #['d', 'e', 'f', 'g']
print("Elements with step 2:", sample_list[::2])  #['a', 'c', 'e', 'g']
print()
print("Reversed List:", sample_list[::-1])  #['g', 'f', 'e', 'd', 'c', 'b', 'a']
print()

#list mutable example
mutable_list = [1, 2, 3, 4, 5]
print("Original List:", mutable_list)  #[1, 2, 3, 4, 5]
mutable_list[2] = 99  #changing element at index 2
print("Modified List:", mutable_list)  #[1, 2, 99, 4, 5]
print()
#list methods examples
fruits = ['apple', 'banana', 'cherry']
print("Original Fruits List:", fruits)  #['apple', 'banana', 'cherry']
fruits.append('orange')  #adding element to the end
print("After append:", fruits)  #['apple', 'banana', 'cherry', 'orange']
fruits.insert(1, 'kiwi')  #inserting element at index 1
print("After insert:", fruits)  #['apple', 'kiwi', 'banana', 'cherry', 'orange']
print()
fruits.remove('banana')  #removing element 'banana'
print("After remove:", fruits)  #['apple', 'kiwi', 'cherry', 'orange']
#delete using del
del fruits[0]  #deleting element at index 0
print("After del:", fruits)  #['kiwi', 'cherry', 'orange']
fruits.pop()  #removing last element
print("After pop:", fruits)  #['apple', 'kiwi', 'cherry']
valueOfPopped = fruits.pop(2)  #removing element at index 2
print("Popped Value:", valueOfPopped)  #'cherry'
fruits.sort()  #sorting the list
print("After sort:", fruits)  #['apple', 'cherry', 'kiwi']
print()
fruits.reverse()  #reversing the list
print("After reverse:", fruits)  #['kiwi', 'cherry', 'apple']
print()
#extending list
more_fruits = ['mango', 'grape']
#removes duplicates while extending
for fruit in more_fruits:
    if fruit not in fruits:
        fruits.append(fruit)
print("After extending with more fruits:", fruits)  #['kiwi', 'cherry', 'apple', 'mango', 'grape']
print()
#add more fruits for duplicate removal demo
fruits.append('apple')
fruits.append('banana')
fruits.append('grape')
print("Before removing duplicates:", fruits)  #['kiwi', 'cherry', 'apple', 'mango', 'grape', 'apple', 'banana', 'grape']
#remove duplicates
fruits = list(dict.fromkeys(fruits))
print("After removing duplicates:", fruits)  #['kiwi', 'cherry', 'apple', 'mango', 'grape', 'banana']

fruits.extend(['banana', 'orange'])  #extending list with multiple elements
print("After one line extend: ", fruits)  #['kiwi', 'cherry', 'apple', 'mango', 'grape', 'banana', 'orange']
print()
print("Index of 'mango': ", fruits.index('mango'))  #3



#clearing the list
fruits.clear()
print("After clear:", fruits)  #[]

#length of list
print("Length of fruits list:", len(fruits))  #3
print()
#Nested list example
nested_list = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
print("Nested List:", nested_list)  #[[1, 2, 3], ['a', 'b', 'c'], [True, False]]
print("Element at nested index [1][2]:", nested_list[1][2])  #'c'
print()
#Concatenation of lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
combined_list = list1 + list2
print("Combined List:", combined_list)  #[1, 2, 3, 'a', 'b', 'c']
print()
#Repetition of lists
repeated_list = list1 * 3
print("Repeated List:", repeated_list)  #[1, 2, 3, 1, 2, 3, 1, 2, 3]
print()

#sorting examples
num_list = [5, 2, 9, 1, 5, 6]
print("Original Number List:", num_list)  #[5, 2, 9, 1, 5, 6]
num_list.sort()
print("Sorted Number List:", num_list)  #[1, 2, 5, 5, 6, 9]
num_list.sort(reverse=True)
print("Sorted in Descending Order:", num_list)  #[9, 6, 5, 5, 2, 1]
print()
#count and index methods
sample_list = [1, 2, 3, 2, 4, 2, 5]
count_of_2 = sample_list.count(2)   #counts occurrences of 2   
#index example
index_of_4 = sample_list.index(4)    #finds index of first occurrence of 4
print("Count of 2 in sample_list:", count_of_2)  #3
print("Index of 4 in sample_list:", index_of_4)  #4
print()

#list comprehension example
squared_numbers = [x**2 for x in range(1,6)] #squares of numbers from 1 to 5
print("Squared Numbers using List Comprehension:", squared_numbers)  #[1, 4, 9, 16, 25]
squares = [x*x for x in range(10)] #another way to get squares of numbers from 0 to 9
print("Squares using List Comprehension:", squares) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

square = [ x*x for x in range(2)]
print("Square of numbers from 0 to 1:", square) #[0, 1]


