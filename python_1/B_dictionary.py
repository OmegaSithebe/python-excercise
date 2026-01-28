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


def word_replace(str1, dict1):
    str2 = str1.split(' ')
    new_str = []
    for key in str2:
        if key in dict1:
            new_str.append(dict1[key])
        else:
            new_str.append(key)
    return ' '.join(new_str)
    
print(word_replace(
"I never take naps during the day",
    {"never":"always","day":"weekend" }
))
# 'I always take naps during the weekend'

print(word_replace(
"the park is closed",
    {"closed":"open","the":"a" }
))
# 'a park is open'

print(word_replace(
"I do what I want",
    {"I":"we","cat":"dog" }
))
# 'we do what we want'


#Exercise 5
def get_average_age(dict1):
    tot_age = 0
    for key in dict1:
        tot_age += key['age']
    return round(tot_age/len(dict1), 2)


peeps = [
    {"name":"Lovelace","age":36,"born":"London, UK" },
    {"name":"Kleene","age":85,"born":"Connecticut, US" },
    {"name":"Turing","age":41,"born":"London, UK" },
    {"name":"Hopper","age":85,"born":"New York, US" },
]

print(get_average_age(peeps))
# 61.75


people = [
    {"name":"Orwell","age":46,"born":"Bihar, India" },
    {"name":"Bradbury","age":91,"born":"California, US" },
    {"name":"Huxley","age":69,"born":"California, US" },
]

print(get_average_age(people))
# 68.67


