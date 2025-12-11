#Dictionary are sort of storage containers that hold key-value pairs, similar to lists but with keys instead of indices.
#Dictionaries are mutable, meaning you can change their content without changing their identity.
#They are defined with {key : value} pairs. Keys must be unique and immutable (like strings or numbers), while values can be of any data type.
#Values can be anything. Fast lookup (hashing) based on keys.
#Dictionary examples
sample_dict = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science', 'Art'],
    101: 'Employee ID'
}

#Accessing dictionary elements
print('Printing data on the disctionary:')
print('Name: ', sample_dict['name'])  #Alice
print('Age: ', sample_dict.get('age'))  #30

#Mutable example - add new key-value pair
print()
sample_dict['age'] = 16 #Updating age from 30 to 16
print('Now we will update the age (this is a mutable exmple):')
print('Age updated to: ',sample_dict['age']) #16

#Adding a new key-value pair
print()
sample_dict['email'] = 'alice@gmail.com'
print('Added a new key-value pair in the dictionary:')
print(sample_dict)

#Remove item from the dictionary
print()
removed_value = sample_dict.pop('age')  #removes 'age' key

#Remove last inserted item
last_item = sample_dict.popitem()  #removes last inserted key-value pair

print('Now to print removed items from the dictionary:')
print('Removed Age:', removed_value) #16
print('Last removed item:', last_item)  #email

#Delete in the dictionary
del sample_dict['is_student'] #deletes 'is_student' key
print(sample_dict)
print()

#Clear the dictionary
sample_dict.clear()
print('After clearing the dictionary:', sample_dict)  #{}

#Dictionary methods examples
#Keys(), values(), items()
sample_dict = {
    'name': 'Alice',
    'age': 30,
    'is_student': False,
    'courses': ['Math', 'Science', 'Art'],
    101: 'Employee ID'
}

print('Now we are printing the dictionary methods exmples:')
print('Keys: ', sample_dict.keys())  #dict_keys(['name', 'age', 'is_student', 'courses', 101])
print('Values: ', sample_dict.values())  #dict_values(['Alice', 30, False, ['Math', 'Science', 'Art'], 'Employee ID'])
print('Items: ', sample_dict.items())  #dict_items([('name', 'Alice'), ('age', 30), ('is_student', False), ('courses', ['Math', 'Science', 'Art']), (101, 'Employee ID')])


#Update multiple values in the dictionary
sample_dict.update({'age': 28, 'is_student': True, 'email': 'alice@gmail.com'}) 
print("Now this is the updated list from the dictionary, after implementing the multiple updates:")
print(sample_dict)

#Running through each item in the Dictionary
print()
for key, value in sample_dict.items():
    print(f" the key is: {key} and the value is: {value}")
    
    
#Dictionary Comprehension example
squares = {x: x*x for x in range(6)}
squared_set = {x*x for x in range(6)}
print("Dictionary Comprehension example:")
print(squares)  #{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print()
print(squared_set) #{0, 1, 4, 9, 16, 25}


#Tuple is ordered, immutable (cannot be changed after creation) collection of items in Python.
#Tuples are defined using parentheses () and can contain elements of different data types.
#Define using(), Allows duplicate values, Can store different data types.
#Tuple examples
numbers = (10, 20, 30, 40)
data = ('Abby', 25, True, 5.6)
print()
print('Tuple examples:')
print('Numbers Tuple:', numbers)  #(10, 20, 30, 40)
print('Data Tuple:', data)  #('Abby', 25, True, 5.6)

#Why Tuple important (Simple)
#Immutable -> cannot change, Faster than Lists, Can be used as keys in dictionaries, Safer for fixed data, Memory efficient, Good for constants; coordinaties, database records, etc.
#Normal tuple
t = (1, 2, 3, 4, 5)
#Tuple with different data types
info = ('John', 28, False, 5.9)
#Single-element tuple (note the comma)
x = (42,)
#Tuple withouth parentheses (packing)
t = 1, 2, 3, 4, 5
#nNested tuple
nested_tuple = (1, (2, 3), (4, 5, 6)) 

print('Different types of Tuples:')
print('Normal Tuple:', t)  #(1, 2, 3, 4
print('Tuple with different data types:', info)  #('John', 28, False, 5.9)
print('Single-element Tuple:', x)  #(42,)
print('Tuple without parentheses:', t)  #(1, 2, 3, 4, 5)
print('Nested Tuple:', nested_tuple)  #(1, (2, 3), (4, 5, 6))
print()

#Difference between Packing & Unpacking
#Packing
packed_tuple = 1, 'hello', 3.14, True
#Unpacking
unpacking_tuple = (10, 20, 30)
a, b, c = unpacking_tuple

#The main difference between packing and unpacking in tuples is that packing is the process of combining multiple values into a single tuple, while unpacking is the process of extracting individual values from a tuple into separate variables.
#this is called destructuring assignment
print('Packing Tuple:', packed_tuple) #(1, 'hello', 3.14, True)
print('Now for a single item (Packed tuple):', packed_tuple[1]) #'hello'
print('Unpacking Tuple values:', a, b,c)  #10 20 30
print('Now for a single item (unpacked tuple):', b)  #20

#Extended unpacking
a, *b = (1, 2, 3, 4, 5, 6, 7, 8)
print('Extended unpacking: ', a) #1
print('Extended unpacking (rest of the values): ', b) #[2, 3, 4, 5, 6, 7, 8]
#Tuple methods
sample_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = sample_tuple.count(2)   #counts occurrences of 2   
index_of_4 = sample_tuple.index(4)    #finds index of first occurrence of 4
print()
print('Tuple methods example:')
print("Count of 2 in sample_tuple:", count_of_2)  #3
print("Index of 4 in sample_tuple:", index_of_4)  #4
print()
#Tuple immutability demo
immutable_tuple = (1, 2, 3)
try:
    immutable_tuple[1] = 20  #Attempting to change value at index 1
except TypeError as e:
    print("Error:", e)  #TypeError: 'tuple' object does not support item assignment
#This error occurs because tuples are immutable, meaning their elements cannot be changed after the tuple is created.
print()

#indexing in tuples
t = (10, 20, 30, 40, 50)
print(t[0])
print(t[-4])  #20
print(t[-1])

#tuple slicing
p = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(p[2:5])  #(3, 4, 5)
print(p[:4])   #(1, 2, 3, 4)
print(p[:3])   #(1, 2, 3)
print(p[::4]) #(1, 5, 9)
print(p[::3]) #(1, 4, 7)

#Immutable (Cannot modify tuple)
d = (100, 200, 300)
d[0] = 150  #This will raise a TypeError

#Allowed tuple manipulation (since tuple is mutable)
#You cannot update items but you can:
#Concatenation 
w = (1, 2, 3)
v = (4, 5, 6)
combined = w + v
print("Concatenated Tuple:", combined)  #(1, 2, 3, 4, 5, 6)

#Repitition tuple
print((1, 2) * 3)  #(1, 2, 1, 2, 1, 2)

#Check element exists
g = (10, 20, 30)
print(30 in g)  #True

#Count elements
h = (1, 2, 2, 3, 2, 4)
print('Count of 2 in h:', h.count(2))  #3

#Find index
print((10, 20, 30).index(20))  #1

#When to use tuple in real world cases:
#Days of the weeek
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print('Days of the week tuple:', days)
#Coordinates
coordinates = (40.7128, -74.0060)  #Latitude and Longitude of New York City
print('Coordinates tuple:', coordinates)
#Database records
record = (1, 'Alice', 'Developer', 75000)
print('Database record tuple:', record)
#Return multiple values from frunction 
def caluculate(a, b):
    return a + b, a * b
print('Return multiple values from function tuple:', caluculate(5, 10))

sun_val, prod_val = caluculate(5, 10)
print('Sum:', sun_val)
print('Product:', prod_val)

#Dictionary keys (only immutable types allowed)
my_dict = {
    (1, 2): 'Point A',
    (3, 4): 'Point B'
}

#Set in Python is an unordered collection of unique items. Sets are mutable, meaning you can add or remove items after creation, but the items themselves must be immutable (like numbers, strings, or tuples).
#Sets are defined using curly braces {} or the set() function.
#No duplicate values, Unordered (no indexing), Mutable (can add/remove items), Immutable items only(meaning the items themselves cannot be changed), fast membership check, unordered (indexing not allowed).
myset = {1, 2, 2, 3, 4, 5, 5, 5, 6}
print(myset)  #{1, 2, 3, 4, 5, 6} stores only unique values
#Set examples
print()
print('Set examples:')
empty_set = set()  #empty set
print('Empty Set:', empty_set)  #set()
mixed_set = {1, 'hello', 3.14, (2, 3)}  #set with mixed data types
print('Set with mixed data types:', mixed_set)  #{1, 'hello', 3.14, (2, 3)}


#No indexing or slicing in sets
myset = {10, 20, 30, 40, 50}
myset[0] #This will raise a TypeError, not allowed

#Set manipulation examples, add element
myset.add(60)
print('After adding 60:', myset)  #{10, 20, 30, 40, 50, 60}

#update multiple elements
myset.update([70, 80, 90])
print('After updating with multiple elements:', myset)  #{70, 40, 10, 80, 50, 20, 90, 60, 30}

#Remove element (throws error if missing)
myset.remove(20)
print('After removing 20:', myset)  #{70, 40, 10, 80, 50, 90, 60, 30}

#Discard element (no error if missing)
myset.discard(70)
print('After discarding 70:', myset)  #{40, 10, 80, 50, 90, 60, 30}

#Pop element (removes random item)
popped_value = myset.pop()
print('Popped Value:', popped_value)
print('After popping an element:', myset)
#Clear the set
myset.clear()

#Set operations examples, Union
setA = {1, 2, 3, 4, 5} 
setB = {4, 5, 6, 7, 8}
print(setA | setB)  #{1, 2, 3, 4, 5, 6, 7, 8} Union


#Intersection
print(setA & setB)  #{4, 5} Intersection

#Difference
print(setA - setB)  #{1, 2, 3} Difference

#Symmetric Difference
print(setA ^ setB)  #{1, 2, 3, 6, 7, 8} Symmetric Difference

#Set Use Cases
#Unique items storage
#Removing duplicates from a list
#Fast membership testing
#Mathematical set operations
#Searching unique values