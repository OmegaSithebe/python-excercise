#Practice 1
# Write a function `remove_last_vowel` that accepts a string as an argument.
# The function should return the string with its last vowel removed.
# Vowels are the letters: a, e, i, o, u

def remove_last_vowel(str1):
    for i in range(len(str1)-1, -1, -1):
        char = str1[i]
        if char in 'aeiou':
            before = str1[:i]
            after = str1[i+1:]
            return before+after
    
    if str1 not in 'aeiou':
        return str1


print(remove_last_vowel("speaker"))# 'speakr'
print(remove_last_vowel("trading"))# 'tradng'
print(remove_last_vowel("thunder"))# 'thundr'
print(remove_last_vowel("myth"))# 'myth'



#Practice 2
# Write a function `pick_prefix(strings, prefix)` that accepts:
# - a list of strings
# - a prefix string
#
# The function should return a list of words that begin with the prefix.

def pick_prefix(str1, pref):
    new_list = []
    # for word in str1:
    #     if pref in word:
    #         new_list.append(word)
    # return new_list
    
    for word in str1:
        if pref in word[:3]:
            new_list.append(word)
    return new_list

print(pick_prefix(['connect','company','concert','cram'],'con'))
# ['connect', 'concert']

print(pick_prefix(['miner','mistake','misspeak','moose','mission'],'mis'))
# ['mistake', 'misspeak', 'mission']




#Practice 3
# Write a function `trendy_text` that accepts a sentence string as an argument.
# The function should return the sentence where the last vowel of every word
# is removed.

def trendy_text(str1):
    new_str = ''
    for word in str1:
        new_str += remove_last_vowel(word)
    return new_str

print(trendy_text("the concert will be epic"))
# 'th concrt wll be epc'

print(trendy_text("breakfast food is wonderful"))
# 'breakfst fod s wonderfl'

print(trendy_text("the weather will improve hopefully"))
# 'th weathr wll improv hopeflly'





#Practice 4
# Write a function `most_letter_word(sentence, char)` that accepts:
# - a sentence string
# - a single character
#
# The function should return the word in the sentence that contains the
# character the greatest number of times.
#
# You can assume the sentence contains at least one word.
# If there is a tie, return the word that appears first in the sentence.

def most_letter_word(sentence, char):
    # new_list = sentence.split(' ')
    # most_word = ''
    # high_count = 0
    # for word in new_list:
    #     count = word.count(char)
    #     if count > high_count:
    #         high_count = count
    #         most_word = word
    # return most_word
    
    list = sentence.split(' ')
    counts = []
    
    for word in list:
        counts.append(word.count(char))
        
    max_indx = counts.index(max(counts))
    
    return list[max_indx]
                

print(most_letter_word(
'she received an award for excellence in science','e'
))# 'excellence'

print(most_letter_word(
'she received an award for excellence in science','a'
))# 'award'

print(most_letter_word(
'I hope sophomore year comes soon','o'
))# 'sophomore'

print(most_letter_word(
'I hope sophomore year comes soon','s'
))# 'sophomore'
