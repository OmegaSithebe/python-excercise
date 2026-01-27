# Exercise 1:
def character_count(string1):
    new_dict = {}
    for key in string1:
        if key in new_dict:
            new_dict[key] += 1
        else:
            new_dict[key] = 1
    return new_dict
    
    
print(character_count("evening"))
# { 'e': 2, 'v': 1, 'n': 2, 'i': 1, 'g': 1 }

print(character_count("mississippi"))
# { 'm': 1, 'i': 4, 's': 4, 'p': 2 }

print(character_count("chili"))
# { 'c': 1, 'h': 1, 'i': 2, 'l': 1 }


#Excercise 2

def letter_map(string1, dict1):
    new_str = ''
    for key in string1:
        if key in dict1:
            new_str += dict1[key]
        else:
            new_str += key
    return new_str
        
    
print(letter_map("symbolic", {"y":"i","o":"a","c":"k" }))
# 'simbalik'

print(letter_map("colossal", {"o":"x","s":"p" }))
# 'cxlxppal'

print(letter_map("miniscule", {"u":"t","i":"f","e":"q" }))
# 'mfnfsctlq'



#Exercise 3
def most_common_letter(string1):
    counts = {}
    for key in string1:
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    
    com_value = 0
    com_key = ''
    for k, v in counts.items():
        if v > com_value:
            com_value = v
            com_key = k
            
    return com_key

print(most_common_letter("building"))
# 'i'

print(most_common_letter("shoestring"))
# 's'

print(most_common_letter("preparedness"))
# 'e'

