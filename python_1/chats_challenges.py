#Challenge 1
#Write a function that returns the longest word with all unique characters.
#If multiple words qualify, return the last one.


def longest_unique_word(lists):
    new_longList = []
    long_word = ''
    unique_cha = ''
    new_longList = lists.split(' ')
    for char in new_longList:
        if len(char) >= len(long_word):
            long_word = char
    print(long_word)


longest_unique_word("apple cherry date banana") #-> "cherry"



#Challenge 2
#Capitalize each word except common stop-words:
#["and", "or", "the", "of", "in"]

#Stop-words should remain lowercase unless they are the first word.

def title_cleaner(lists):
    new_list = []
    new_list = lists.split(' ')
    for char in new_list:
        if char == 'and' or char == 'or' or char == 'the' or char == 'of' or char == 'in':
            new_list.append(char)
        else:
            new_list.append(char.capitalize())
    print(new_list.join(' '))
            

title_cleaner("the lord of the rings") #-> "The Lord of the Rings"



#List Challenge 3: numeric_summary(numbers)
#Return a dictionary containing: "min", "max", "average" (rounded to 2 decimals)

def numeric_summary(numbers):
    min = 0
    max = 0
    average = 0
    for i in range(len(numbers)):
        if numbers[i] < numbers[i]:
            min = numbers[i]
        if numbers[i] > max:
            max = numbers[i]
            average += numbers[i]
    
    new_average = average / len(numbers) 
    new_list = 'min: ' + str(min) + ' max: ' + str(max) + ' average: ' + str(round(new_average, 2))
        
numeric_summary([10, 5, 8, 20])  #-> {'min': 5, 'max': 20, 'average': 10.75}


