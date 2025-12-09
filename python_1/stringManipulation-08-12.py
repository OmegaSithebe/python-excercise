#string manipulation operators
s = "PYTHON"
#Positive indexing
# P  Y  T  H  O  N
# 0  1  2  3  4  5
print(s[0])  #P
print(s[3])  #H

print()
#Negative indexing
# P  Y  T  H  O  N
#-6 -5 -4 -3 -2 -1
print(s[-6])  #P
print(s[-3])  #H

print()
e = "HELLO WORLD!!!!!!!!!!!!!!!!!!!!!!!!"
print(e.count("!"))  #counts the number of ! in the string
print(e.lower())    #converts to lowercase
print(e.upper())    #converts to uppercase
print()
print(e.replace("!", "."))  #replaces ! with .
print(e.split(" "))  #splits the string at space and returns a list
print(e.find("WORLD"))  #finds the starting index of the substring WORLD
print()
print(e.index("WORLD"))  #finds the starting index of the substring WORLD
print(e.startswith("HELLO"))  #checks if the string starts with HELLO, returns
print(e.endswith("!"))  #checks if the string ends with !, returns
print()
print(e.capitalize())  #capitalizes the first letter of the string
print(e.title())  #capitalizes the first letter of each word in the string
print(e.strip("!"))  #removes ! from the start and end of the string
print()
print(e.replace("!", "").strip())  #removes all ! and extra spaces from start
print(len(e))  #returns the length of the string
print(e[0:5])  #slicing the string from index 0 to 4
print()
print(e[-6:])  #slicing the string from index -6 to end
print(e[:5])  #slicing the string from start to index 4
print(e[::2])  #slicing the string to get every second character
print()
print(e[::-1])  #reverses the string
print(e.center(50, "-"))  #centers the string in a field of width 50, padded with -

list = ['Hello', 'World']
ans = list[0]
rev = ans[::-1]
print(rev)  #olleH
print

#stripping examples
r = "hello this is python"
print(r)
print(r.strip())  #removes leading and trailing whitespace
print(r.lstrip("h"))  #removes leading H
print(r.rstrip("n"))  #removes trailing !

print()
#split & join examples
words = r.split(" ")  #splits the string into a list of words
print(words) #prints the list of words

print()
print(r)
arr = r.split(" ") #splits the string into a list of words
print(arr)
for word in arr:
    print(word) #prints each word in the list
    
    
#Check methods (boolean methods)
w = "Is this a string 45 1234 55 with numbers?"
print(w)
print(w.isalpha())  #checks if all characters are alphabetic
print(w.isdigit())  #checks if all characters are digits
print(w.isalnum())  #checks if all characters are alphanumeric
print(w.isspace())  #checks if all characters are whitespace
print()

#isDigit examples
num_str1 = "12345"
print(num_str1.isdigit())  #True

print()
#isNumeric examples
num_str2 = "123.45"
print(num_str2.isnumeric())  #False
num_str3 = "8"
print(num_str3.isnumeric())  #True

print()
#isalnum examples
alnum_str = "Hello123"
print(alnum_str.isalnum())  #True


#is upper & is lower examples
upper_str = "HELLO"
lower_str = "hello"
print(upper_str.isupper())  #True
print(lower_str.islower())  #True


print()

#Encoding & Decoding (UTF-8)
#Encoding
sample_str = "Hello, Python!"
encoded_str = sample_str.encode("utf-8")
print(encoded_str)  #b'Hello, Python!'

#Decoding
print()
decoded_str = encoded_str.decode("utf-8")
print(decoded_str)  #Hello, Python!
print()


 #format strings examples
name = "Alice"
age = 30
formatted_str = "My name is {} and I am {} years old.".format(name, age)
print(formatted_str)  #My name is Alice and I am 30 years old.

print()
#f-strings examples
print(f"My name is {name} and I am {age} years old.")  #My name is Alice and I am 30 years old.

print()

#Join examples
words_list = ["Hello", "from", "Python"]
joined_str = " ".join(words_list)
print(joined_str)  #Hello from Python