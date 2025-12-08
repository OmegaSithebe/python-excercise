# string concatination operator

str1 = "Hello, "
str2 = "World!"

print(str1 + str2) 
print("Hello " + "Python!")

#Math operators
# +, -, *, /, %, //, **

num1 = 10
num2 = 3

print(5 + 5)
print(num1 + num2)

result = (5 + 5) - 2 * 6 / 2
print(result)

print(7 % 2)

print(6 % 2)

print(7 // 2)

print(2 ** 3)


#Assignment operators
# =, +=, -=, *=, /=, %=, //=, **=

x = 15
y = 20

x = x + 10 

x += 10

print(x)

dev = "Sipho Kunene"

print(dev)

#comparison operators
# ==, !=, >, <, >=, <=, return boolean, true or false

print(5 >= 4) #True
print(3 != 3) #False
print(5 != 5) #False
print(5 == 5) #True

#Logical operators
# and, or, not

value = 5 > 4 and 6 > 4 #True
value2 = 5 > 4 or 6 > 7 #False

#And must have both side (conditions) to be true
#Or must have at least one side (condition) to be true

print(True or False)
print(True and False)

print(not True) #False
print(False or not True) #False
print(False or True) #True 
print(False or True)
print(not False) #True
print(not False or True) #True
print(not (False or True)) #False
print(not (False and True)) #True
print(not (True and True)) #False
print(not (False and False)) #True
print(not (True or True)) #False
print(not (True or False)) #False