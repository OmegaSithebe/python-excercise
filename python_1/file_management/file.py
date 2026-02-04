file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


file =open('output.txt', 'w')
file.write('Hello Python \n')
file.write('File handling is useful')
file.close()

file =open('output.txt', 'a')
file.write('\nLearning step by step')
file.close()


name = input('Enter student name: ')

file =open('student.txt', 'a')
file.write('Student name is: ' + name + '\n')
file.close()

with open('data.txt', 'r') as file:
    content = file.read()
print(content)


with open('output.txt', 'w') as file:
    file.write('This is the new writing, Hello Python \n')
    file.write('Using with statement')
    
    
with open('output.txt', 'a') as file:
    file.write('\n\nLearning best practices using the append function')