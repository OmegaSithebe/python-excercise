#Loop of list example
fruits = ["mango", "banana", "orange"]

print("This is a list of loop exmple:")
print(fruits[0])

for fruit in fruits:
    print(fruit)


#Loop in range of number 1 to 10
for i in range(1, 11):
    print(i)
    

#Loop in range of number 1 to 10
for i in range(1, 11, 2):
    print(i)
    

#Loop through the character
char = "Python"

for ch in char:
    print(ch)
    

#enumerate() - function used to give index & value

print("This loop the index & the character:")
for i, ch in enumerate(char):
    print(f"Index is {i} and character: {ch}")
    
print()    
#Loop through the dictionary
print("This will loop through the dictionary:")
students = {"name": "Robert Walker", "age": 45}

print()
print("This will loop through the keys:")
for key in students:
    print(key)
    
print()
print("This will loop through the values:")
for value in students.values():
    print(value)

print()
print("This will loop thtrough the items")
for key, value in students.items():
    print(f"The key in object is {key} and the value is: {value}")
    
    
#snippet1 - exercise
print("Hello")

for i in range(5):
    print("code")
    
print("goodbye")


#snippet2 - exercise
word = "street"

for i in range(len(word)):
    print(i)
    print(word[i])

print("After loop")

#Find the sum of 1 to 5
sum = 0

for i in range(1, 6):
    sum += i
    print(sum)
    
print("This is the total:")
print(sum)


#Write a function 'one_to_four' that prints the numbers 1 through 4 (inclusive).

print("This functions loops from 1 to 4")
def one_to_four():
    for i in range(1, 5):
        print(i)

one_to_four()


print('Hi')
for i in range(3, 8):
    print('program')
    print(i)
    
print('Bye')


def foo():
    for num in range(10, 0, -2):
        print(num)
        
print('begin')
foo()
print('end')
foo()


word = 'streets'

for i in range(len(word)):
    print(str(i) + ' - ' + word[i])
    

total = 0

for i in range(1, 5):
    total += i
    print(total)
    
print('The total is ' + str(total))

#count(6) this functions are called parameters as there should be a value passed with the function hence parameter

def one_to_four2():
    for i in range(1, 5):
        print(i)
        
print('Displaying the numbers 1 - 4, inclusively.')
one_to_four2()


def count_up(num):
    for num in range(1, num+1):
        print(num)
        
print('This function prints numbers to a maximum number given:')
count_up(5)
print('This function prints numbers to a maximum number given:')
count_up(3)


def min_to_max(min_num, max_num):
    for min_num in range(min_num, max_num+1):
        print(min_num)
        
min_to_max(5, 9)
min_to_max(11, 13)
min_to_max(20, 11)


def string_iterate(text):
    for num in range(len(text)):
        print(str(num) + ' - ' + text[num])
        
string_iterate('celery')
print('-------------')
string_iterate('hat')


def evens(max):
    for num in range(1, max):
        if num % 2 == 0:
            print(num)

evens(11)
print('----------------')
evens(8)


def sum_of_range(num):
    total1 = 0
    for i in range(1, num + 1):
        total1 += i
        print('Subtotal: ' + str(total1))
    return total1
        
results = sum_of_range(2)
print('The final total is: ', results)

results = sum_of_range(5)
print('The final total is: ', results)


def countdown(start):
    for i in range(start - 1 , -1, -1):
        print(i)
        
countdown(2)
print('******************')
countdown(5)
print('******************')
countdown(10)

def countdow(sta):
    for i in range(sta, 0, -1):
        print(i)
        
countdow(2)
print('******************')
countdow(5)
print('******************')
countdow(10)


def find_char_position(string, charac):
    for i in range(len(string)):
        if string[i] == charac:
            print('The position of the ' + charac + ' is at ' + str(i+1))
            
find_char_position('banana', 'a')        
    
    
def multiplication_table(multiple):
    for u in range(1, 11):
        print(u * multiple)
        
multiplication_table(4)