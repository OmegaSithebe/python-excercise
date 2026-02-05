#Types of Errors in Python
#SyntaxError -> Missing colon
#NameError -> Variable not defined
#TypeError -> Adding int + string
#ValueError -> Invalid input
#ZeroDivisionError -> Divide by Zero
#FileNotFoundError -> File not found


#Try, Except & Finally
#Try:
## (risky code)
#except:
## (error handling code)
#finally:
## (always runs)


#Example 1: Simple Try-Except
try:
    x = int(input('Enter a number: '))
    print(10 / x)
except:
    print('Something went wrong!') 
      
      
#Example 2: Using finally
try:
    print(10/0)
except:
    print('Error occurred')
finally:
    print('Program finished, last line code.')
    
    
#Catching Multiple Exceptions
try:
    x = int(input('Enter a number: '))
    print(10 / x)
    
except ZeroDivisionError:
    print('You cannot divide by zero')
    
except ValueError:
    print('Please enter a valid number')
    
    
#Catch multiple together
except(ValueError, TypeError):
    print('Invalid input')
    
    
#Raise your own error(raise)
try:
    age = int(input('Enter age: '))
    
    if age < 18:
        raise ValueError('Age must be 18 or above.')
    
    print('Access granted!')
    
except ValueError as e:
    print('Error:', e)
    
    

#Creating Custom Exceptions
class NegativeNumberError(Exception):
    pass

try:
    num = int(input('Enter a number: '))
    
    if num < 0:
        raise NegativeNumberError('Negative numbers not allowed')
    
    print('Valid number')
    
except NegativeNumberError as e:
    print(e)
    
    

#ATM Simulation (With exception handling)
balance = 5000

try:
    amount = int(input('Enter withdrawal amount: '))
    
    if amount <= 0:
        raise ValueError('Amount must be positive')
    
    if amount > balance:
        raise ValueError('Insufficient balance')
    
    balance -= amount
    print('Withdrawal successful')
    print('Remaining balance:', balance)
    
except ValueError as e:
    print('Error:', e)
    
finally:
    print('Thank you for using MEGA ATM')
    
    
    
    