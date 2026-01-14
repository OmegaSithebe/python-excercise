# Write a function `total(numbers)` that accepts a list of numbers as an argument.
# The function should return the sum of all elements in the list.

# def total(numbers):
#     sum = 0
#     for x in range(len(numbers)):
#         sum += numbers[x]
#     print(sum)


def total(numbers):
    sum = 0
    for x in numbers:
        sum += x 
    print(sum)

# Example:
total([3, 2, 8]) #-> 13`
total([-5, 7, 4, 6]) #-> 12
total([7]) #-> 7
total([]) #-> 0



# Write a function `stay_positive(numbers)` that accepts a list of numbers.
# The function should return a new list containing only the positive numbers.

def stay_positive(numbers):
    positive = []
    for num in numbers:
        if num > 0:
            positive.append(num)
    return positive


# Example:
stay_positive([10, -4, 3, 6]) #-> [10, 3, 6]
stay_positive([-5, 11, -40, 30.3, -2]) #-> [11, 30.3]
stay_positive([-11, -30]) #-> []




# Write a function `bleep_vowels(text)` that accepts a string and returns
# a new string where all vowels (a, e, i, o, u) are replaced with '*'.

# def bleep_vowels(string):
#     store = ''
#     for cha in string:
#         if cha == 'a' or cha == 'e' or cha == 'i' or cha == 'o' or cha == 'u':
#             store += '*'
#         else:
#             store += cha
#     print(store)
    
    

def bleep_vowels(string):
    vowels = 'aeiou'
    store = ''
    for cha in string:
        if cha.lower() in vowels:
            store += '*'
        else:
            store += cha
    print(store)


# Example:
bleep_vowels("skateboard") #-> 'sk*t*b**rd'
bleep_vowels("slipper") #-> 'sl*pp*r'
bleep_vowels("range") #-> 'r*ng*'
bleep_vowels("brisk morning") #-> 'br*sk m*rn*ng'



# Write a function `filter_long_words(words)` that accepts a list of strings.
# The function should return a new list containing only the words that have
# less than 5 characters.

def filter_long_words(words):
    new_list = []
    for s in words:
        if len(s) < 5:
            new_list.append(s)
    print(new_list)

# Example:
filter_long_words(["kale", "cat", "retro", "axe", "heirloom"]) #-> ['kale', 'cat', 'axe']
filter_long_words(["disrupt", "pour", "trade", "pic"]) #-> ['pour', 'pic']




# Write a function `num_odds(numbers)` that accepts a list of numbers.
# The function should return the count of odd numbers in the list.

def num_odds(numbers):
    sum = 0
    for i in numbers:
        if i % 2 > 0:
            sum += 1
    print(sum)

# Example:
num_odds([4, 7, 2, 5, 9]) #-> 3
num_odds([11, 31, 58, 99, 21, 60]) #-> 4
num_odds([100, 40, 4]) #-> 0




# Write a function `strings_to_lengths(strings)` that accepts a list of strings.
# The function should return a new list containing the lengths of each string.

def strings_to_lengths(strings):
    new_list = []
    for chars in strings:
        new_list.append(len(chars))
    print(new_list)

# Example:
strings_to_lengths(["belly", "echo", "irony", "pickled"]) #-> [5, 4, 5, 7]
strings_to_lengths(["on", "off", "handmade"]) #-> [2, 3, 8]



# Write a function `divisors(num)` that accepts a number.
# The function should return a list containing all positive numbers that divide num exactly.
#The absolute value of a number is its distance from zero on the number line, without considering whether it’s positive or negative. For positive numbers, abs() returns the same number. For negative numbers, abs() removes the negative sign. For zero, it returns 0.


def divisors(num):
    # new_num = abs(num)
    new_num = num
    new_list = []
    for g in range(1, num + 1):
        if new_num % g == 0:
            new_list.append(g)
    return new_list

# Example:
divisors(15) #-> [1, 3, 5, 15]
divisors(7) #-> [1, 7]
divisors(24) #-> [1, 2, 3, 4, 6, 8, 12, 24]




