# Write a function `divisible_range(min_val, max_val, num)` that prints all numbers
# between min_val and max_val (exclusive) that are divisible by num.
# The function does not return a value, just prints.

def divisible_range(min_val, max_val, num):
    for i in range(min_val, max_val):
        if i % num == 0:
            print(i)


# Example:
divisible_range(17, 40, 9)
# 18
# 27
# 36

divisible_range(10, 24, 4)
# 12
# 16
# 20


# Write a function `reverse_iterate(text)` that prints each character of the string
# in reverse order. The function does not return a value, just prints.

def reverse_iterate(text):
    for n in range(len(text)-1, -1, -1):
        print(text[n])


# Example:
reverse_iterate("carrot")
# t
# o
# r
# r
# a
# c

reverse_iterate("box")
# x
# o
# b



# Write a function `remove_capitals(text)` that returns a new string with all
# capital letters removed.

def remove_capitals(text):
    results = ''
    for t in range(len(text)):
        if text[t].lower() == text[t]:
            results = results + text[t]
    return results
    

# Example:
remove_capitals("fOrEver")     #-> 'frver'
remove_capitals("raiNCoat")    #-> 'raioat'
remove_capitals("cElLAr Door") #-> 'clr oor'



# Write a function `raise_power(base, exponent)` that returns the result of
# base raised to the exponent using loops (do not use ** operator or math.pow).

def raise_power(base, exponent):
    power = 1
    for i in range(1, exponent +1):
        power *= base
    return power


# Example:
raise_power(2, 5)  #-> 32
raise_power(4, 3)  #-> 64
raise_power(10, 4) #-> 10000
raise_power(7, 2)  #-> 49


# Write a function `censor_e(text)` that returns a new string where all 'e' characters
# are replaced with '*'.

def censor_e(text):
    results = ""
    for i in range(len(text)):
        if text[i] == "e":
            results = results + "*"
        else:
            results += text[i]
    return results


# Example:
censor_e("speedy")  #-> 'sp**dy'
censor_e("pending") #-> 'p*nding'
censor_e("scene")   #-> 'sc*n*'
censor_e("heat")    #-> 'h*at'




# Write a function `fizz_buzz(max_num)` that prints all numbers <= max_num
# that are divisible by 3 or 5 but not both.
# The function does not return a value, just prints.

def fizz_buzz(max_num):
    for i in range(1, max_num + 1):
        dev_3 = i % 3 == 0
        dev_5 = i % 5 == 0
        if (dev_3 or dev_5) and not(dev_3 and dev_5):
            print(i)


# Example:
fizz_buzz(18)
# 3
# 5
# 6
# 9
# 10
# 12
# 18

fizz_buzz(33)
# 3
# 5
# 6
# 9
# 10
# 12
# 18
# 20
# 21
# 24
# 25
# 27
# 33

