# Practice 1
# Write a function `lala_language` that accepts a sentence string as an argument.
# The function should return a new sentence where words longer than 3 characters
# are modified.
#
# Modified words should have each vowel followed by 'l' and the same vowel again.
# See the examples below.

def lala_language(sent):
    words = sent.split(' ')
    results = []
    
    for word in words:
        if len(word) > 3:
            new_word = change_vowel(word)
            results.append(new_word)
        else:
            results.append(word)
    return results
                   
                   
def change_vowel(word):
    vowels = 'aeiou'
    changed = ''
    
    for char in word:
        if char in vowels:
            changed += char + 'l' + char
        else:
            changed += char
            
    return changed
            

print(lala_language('this is pretty strange'))
# 'thilis is preletty stralangele'

print(lala_language('can you speak our language'))
# 'can you spelealak our lalangulualagele'

print(change_vowel('stephan')) 
#stelephalan


#Practice 2
# Write a function `pick_perfect_squares` that accepts a list of numbers.
# The function should return a list containing only the perfect squares.
#
# A perfect square is a number that can be written as n * n.

def pick_perfect_squares(numbers):
    new_list = []
    
    for num in numbers:
        for i in range(1, num):
            if i * i == num:
                new_list.append(num)
                
    return new_list
        
        
        
print(pick_perfect_squares([6,4,81,21,36]))
# [4, 81, 36]

print(pick_perfect_squares([100,24,144]))
# [100, 144]

print(pick_perfect_squares([30,25]))
# [25]



#Practice 3
# Write a function `censor_sentence(sentence, target_words)` that accepts:
# - a sentence string
# - a list of target words
#
# The function should return a new sentence where each target word
# is replaced with '*' characters of the same length.

def censor_sentence(senten, target_word):
    new_sent = senten.split(' ')
    new_list = []
    for word in new_sent:
        if word in target_word:
            replace = len(word)  * '*'
            new_list.append(replace)
        else:
            new_list.append(word)
    return new_list
           

print(censor_sentence('where the heck is my celery', ['heck','celery']))
# 'where the **** is my ******'

print(censor_sentence('why you little sweetheart', ['sweetheart','salad']))
# 'why you little **********'
