# Write a function `five_multiples_of(n)` that prints the first five multiples of n.
# The function does not return a value, just prints.



def five_multiples_of(n):
    for i in range(1, 6):
        print(i * n)

five_multiples_of(7)

# Example:
# 7
# 14
# 21
# 28
# 35


# Write a function `sum_up_to(max_num)` that returns the sum of all whole numbers
# from 1 to max_num inclusive.

def sum_up_to(max_num):
	total = 0
	for i in range(1, max_num + 1):
		total += i
	print(total)


# Example:
sum_up_to(4)  #-> 10
sum_up_to(5)  #-> 15
sum_up_to(2)  #-> 3


# Write a function `no_ohs(text)` that prints each character of the string except 'o'.
# The function does not return a value, just prints.

def no_ohs(text):
    for char in range(len(text)):
        if text[char] != 'o':
            print(text[char])


# def no_ohs(text):
#     for char in text:
#         if char != 'o':
#             print(char)


# Example:
no_ohs('code')
# c
# d
# e



# Write a function `odd_sum(max_num)` that returns the sum of all odd numbers
# from 1 to max_num inclusive.

def odd_sum(max_num):
    sum = 0
    for i in range(1, max_num):
        if i % 2 > 0:
            sum += i
    print(sum)

# Example:
odd_sum(10) #-> 25  # 1 + 3 + 5 + 7 + 9
odd_sum(5)  #-> 9   # 1 + 3 + 5


# Write a function `string_repeater(text, n)` that returns a new string
# consisting of `text` repeated `n` times.

def string_repeater(text, n):
        print(text * n)

# Example:
string_repeater("q", 4)  #-> 'qqqq'
string_repeater("go", 2) #-> 'gogo'
string_repeater("tac", 3) #-> 'tactactac'


# Write a function `product_up_to(max_num)` that returns the product of all numbers
# from 1 to max_num inclusive. (1*2*3*...*max_num)

def product_up_to(max_num):
    product = 1
    for i in range(1, max_num + 1):
        product *= i
    print(product)
        
        

# Example:
product_up_to(4) #-> 24
product_up_to(5) #-> 120
product_up_to(7) #-> 5040


# Write a function `div_by_either(num1, num2, max_num)` that prints all positive numbers
# less than max_num that are divisible by num1 or num2.
# The function does not return a value, just prints.

def div_by_either(num1, num2, max_num):
    for n in range(1, max_num):
        if n % num1 == 0 or n % num2 == 0:
            print(n)

# Example:
div_by_either(4, 3, 16)
# 3
# 4
# 6
# 8
# 9
# 12
# 15
