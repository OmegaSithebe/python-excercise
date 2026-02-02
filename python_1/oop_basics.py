#Creating a simple class
# class Student:
#     def greet(self):
#         print('Hello from Student class')
        
# s1 = Student()
# s1.greet()


# class Student:
#     def set_name(self, name):
#         self.name = name
        
#     def show_name(self):
#         print(self.name)
        
# s1 = Student()
# s1.set_name('Jimmy')

# s2 = Student()
# s2.set_name('George')

# s1.show_name()
# s2.show_name()

# print(s1.name)


# class SchoolName:
#     school_name = 'ABC School'
    
#     def show_school(cls): #show_school is a class method
#         print('School: ', cls.school_name)  #cls is a class itself
        
# sc1 = SchoolName()
# sc1.show_school()

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def show_marks(self): #show_marks is an instance method, works with object data using self
#         print(self.name)
#         print(self.marks)

# s1 = Student('Rams', 86)
# s1.show_marks()

# s1.name = 'James'


class School:
    schoolName = 'ABC School'  #shared by all students
    totalStud = 0              #counts students created
    
    def __init__(self, name, marks):
        self.name = name            #instance variables
        self.marks = marks
        School.totalStud+= 1
    
    def display_info(self):             #instance method, it uses self
        print('Name: ', self.name)
        print('Marks: ', self.marks)

    @classmethod
    def show_school(cls):
        print('School:', cls.schoolName)    #class method, it uses cls
        
s1 = School('Gwen', 77)
s2 = School('Siya', 88)     #Each object has own name & marks

s1.display_info()
print('*************************')
s2.display_info()
School.show_school()
print('**************************')
print('Total Students:', School.totalStud)



#Credit Card
class CreditCard:
    def __init__(self, name, number, bank='ABC Bank'):
        self.name = name
        self.number = number
        self.bank = bank
        self.balance = 0
        
    def change(self, amount):
        if not(isinstance(amount, int)) or isinstance(amount, float) or (amount <= 0):
            print('Change denied')
        else:
            self.balance += amount
            
    def pay(self, amount):
        if not (isinstance(amount, int)) or isinstance(amount, float) or (amount <= 0) or (self.balance > amount):
            print("Pay denied")
        else:
            self.balance -= amount
            
    def __str__(self):
        info = f'Name: {self.name} \n Number: {self.number} \n Bank: {self.bank} \n Balance: {self.balance}'
        return info
    
u1 = CreditCard('James Gordin', 123456789)
print(u1)

u1.change(2000)
print(u1)

u1.pay(500)
print(u1)






