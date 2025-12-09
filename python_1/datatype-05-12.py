object_by_id = {}

print("Hello World!")

x = 10
y = 20

print(x + y)

#data type (int, float, str, bool)

x = 30
print(type(x))  #int
print(id(x))    #memory address

object_by_id[id(x)] = x
addr = id(x)
print(f"Object with id {addr} has value {object_by_id[addr]}")  


y = 40.5
print(type(y))  #float
print(id(y))    #memory address

#list is mutable data type
nums = [5, 10, 9, 4, 2]

print(type(nums))  #list
print(id(nums))    #memory address
print(nums)

#Mutable vs Immutable data types
#Mutable - can be changed (list, dict, set) 
#Immutable - cannot be changed (int, float, str, tuple)

#immutable example tuple
#tuple example
coordinates = (10.0, 20.0)
print(type(coordinates))  #tuple
print(id(coordinates))    #memory address
print(coordinates)

#mutable example dictionary
#dict example
person = {
    "name": "Sipho",
    "age": 30,
    "isDeveloper": True
}

person["age"] = 31  #modifying age value
print(type(person))  #dict
print(id(person))    #memory address
print(person)
#Or only one side (condition) to be true


#set (mutable, no duplicate values)
fruits = {"apple", "banana", "orange", "apple"}
print(type(fruits))  #set
print(id(fruits))    #memory address
print(fruits)
#Converting set to list to allow modifications, is mutable
unique_fruits = list(fruits)
print(type(unique_fruits))  #list
print(id(unique_fruits))    #memory address
print(unique_fruits)
unique_fruits.append("mango")
print(unique_fruits)
unique_fruits.remove("banana")
print(unique_fruits)
#Converting back to set
unique_nums = {1, 2, 3, 2, 1, 4, 5}
print(type(unique_nums))  #set
print(id(unique_nums))    #memory address
print(unique_nums)  #prints {1, 2, 3, 4, 5}

print()

#frozenset (immutable, no duplicate values)
immutable_fruits = frozenset(["apple", "banana", "orange", "apple"])
print(type(immutable_fruits))  #frozenset
print(id(immutable_fruits))    #memory address
print(immutable_fruits)  #prints frozenset({'apple', 'banana', 'orange'})


# bytes (immutable sequence of bytes)
byte_data = bytes([65, 66, 67, 68])  # ASCII values for 'A', 'B', 'C', 'D'
print(type(byte_data))  # <class 'bytes'>
print(id(byte_data))    # memory address
print(byte_data)        # b'ABCD'

# Try to modify it - THIS WILL FAIL!
try:
    byte_data[0] = 69  # Trying to change 'A' (65) to 'E' (69)
    print("Modified byte_data:", byte_data)
except TypeError as e:
    print(f"ERROR: {e}")  # 'bytes' object does not support item assignment

# Even trying to append will fail
try:
    byte_data.append(69)
except AttributeError as e:
    print(f"ERROR: {e}")  # 'bytes' object has no attribute 'append'
    
    
# bytearray (mutable sequence of bytes)
byte_array_data = bytearray([65, 66, 67, 68])
print(type(byte_array_data))  # <class 'bytearray'>
print(id(byte_array_data))    # memory address
print(byte_array_data)        # bytearray(b'ABCD')

# You CAN modify bytearray
byte_array_data[0] = 69  # Change 'A' (65) to 'E' (69)
print("Modified byte_array_data:", byte_array_data)  # bytearray(b'EBCD')

# You can append to it
byte_array_data.append(70)  # Add 'F' (70)
print("After append:", byte_array_data)  # bytearray(b'EBCDF')

# You can insert
byte_array_data.insert(1, 71)  # Insert 'G' (71) at position 1
print("After insert:", byte_array_data)  # bytearray(b'EGBCDF')

ba = bytearray(b"Hello")
print(ba)  # bytearray(b'Hello')
ba[0] = 74  # Change 'H' (72) to 'J' (74)
print(ba)  # bytearray(b'Jello')
print()
