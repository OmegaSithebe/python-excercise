#Modules is the python libraries or program, created by somebody else (someone else written the code). We import that & then we use it.
#In large programming we have separate files with their functions, then we import those functions to other files.
#A module is a Python file that contains: - variables, - functions, - classes

#Why Do We Use Modules?✅ Code reusability, ✅ Better organization, ✅ Easier maintenance, ✅ Team collaboration, ✅ Cleaner projects
# from math import sqrt, pow

# help(math)

# print(sqrt(16))

# print(pow(2, 3))


from my_modules.my_math import add, subtract

print(add(5, 6))

print(subtract(10, 12))