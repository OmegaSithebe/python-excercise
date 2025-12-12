print('Hello World')

#Conditinal function
age = 25

if age < 18:
    print("You are a minor & your not allowed to drive.")
elif age >= 18 and age < 65:
    print("You are an adult & you are allowed to drive.")
else:
    print("You are a senior citizen & you are allowed to drive with caution.")
    
    
num = 40
if num % 2 > 0:
    print("zip")
elif num % 2 == 0:
    print("zoop")


    #conditional - string manipulation
    word = "yebo"
    if word[0] == "d":
        print("Almost there")
    else:
        print("You got it")
        
print("-----")
sentence = "The quick brown fox jumps over the lazy dog"
if sentence[-5] == "t":
    print("Not correct")
print("Pick another letter")

if len(sentence) <= 6:
    print("Sentence is too short")
else:
    print("Sentence long")
    
    
#Conditional - with mod
qty = 38
if qty > 30 and qty % 5 == 4:
    print("Swish")
else:
    print("Swoosh")
    
print("-----")
if qty > 0:
    print("Positive quantity")
    
    
a = "Celery"
b = "SQUASH"
if a == a.upper():
    print("Aplpha")

if b == b.upper():
    print("Beta")
    
    
nonsense = "blog trust fund tattooed williamsburg poke roof party"
has_ok = "ok" in nonsense

if has_ok:
    print("yeet")
elif len(nonsense) >= 10:
    print("yo")
else:
    print("no")
    
has_zoo = "zoo" in nonsense
has_fun = "fun" in nonsense

if has_zoo and has_ok:
    print("cool")
elif has_fun:
    print("yeepie")
elif has_zoo or has_fun:
    print("atleast")
else:
    print("Aahh no...")
    
    
#Write a function to calculate 2 numbers, & return the results
#A simple function definition, key word (def) defines the name of the function (calculator), & then the variables called the parameters 
# #(When you put a vaiable in a inside the parathensis of the function they are called parameters)
def calculator(n1, n2, symbol):
    if symbol == "+":
        return n1 + n2
    elif symbol == "-":
        if n1 > n2:
            return n1 - n2
        else:
            return n2 - n1
    elif symbol == "*":
        return n1 * n2
    elif symbol == "/":
        return n1 / n2
    elif symbol == "%":
        return n1 % n2
    
number1 = 6
number2 = 8
sym = "+"    
ans = calculator(number1, number2, sym)
print(ans)

modd = calculator(4, 7, "%")
print(modd)


#Function for defining an average
def average(num1, num2):
    print("Calculator...")
    return (num1 + num2) / 2

print(average(16, 20))
print()
print(average(1, 10))
print()
print(average(56, 20) - 19)
print()
print(average(16, 20) + 34)

a = 88
b = 6
n = average(a, b)
print()
print()
print(average(n, 18))


#Write a function 'is_div_by_4' that accepts a number as an arugment
#The function should return a boolean indicating whether or not the number is divisible by 4.
def is_div_by_4(aNum):
    if aNum % 4 > 0:
        return False
    else: 
        return True

print(is_div_by_4(8)) #True
print(is_div_by_4(12)) #True
print(is_div_by_4(24)) #True
print(is_div_by_4(9)) #False
print(is_div_by_4(10)) #False


# Write a function `starts_with_r` that accepts a string as an argument.
# The function should return True if the string starts with 'r' or 'R'.
# Otherwise, return False.
print('Check if a string starts with an r or an R')
def starts_with_r(string):
    if string[0] == "r":
        return True
    elif string[0] == "R":
        return True
    else:
        return False

print(starts_with_r("roger that"))        # True
print(starts_with_r("Row, row, row your boat"))  # True
print(starts_with_r("slip"))              # False
print(starts_with_r("Taxicab"))           # False

