#Practice 1
def greatest_population(dict1):
    high_popula = 0
    high_name = ''
    for key in dict1:
        if key['population'] > high_popula:
            high_popula = key['population']
            high_name = key['name']
    return high_name

countries1 = [
    {"name":"Cameroon","population":27744989,"gdp":38.68 },
    {"name":"Belarus","population":9477918,"gdp":59.66 },
    {"name":"Indonesia","population":267026366,"gdp":1042 },
    {"name":"Guyana","population":750204,"gdp":3.88 },
]

print(greatest_population(countries1))
# 'Indonesia'


countries2 = [
    {"name":"New Zealand","population":4925477,"gdp":204.9 },
    {"name":"Mozambique","population":30098197,"gdp":14.72 },
    {"name":"Greenland","population":57616,"gdp":2.71 },
    {"name":"Kazakhstan","population":19091949,"gdp":179.3 },
    {"name":"Burma","population":56590071,"gdp":71.21 },
]

print(greatest_population(countries2))
# 'Burma'



#Practice 2
def pluck(dict1, list1):
    name1 = list1[0]
    name2 = list1[1]
    new_dict = {name1 : dict1[name1], name2 : dict1[name2]}
    
    return new_dict        


print(pluck(
    {"name":"Fido","color":"Brown","breed":"German Shepherd" },
    ["name","breed"]
))
# { "name": "Fido", "breed": "German Shepherd" }

print(pluck(
    {"make":"Tesla","mpg":93,"model":"Model X","color":"white" },
    ["make","model"]
))
# { "make": "Tesla", "model": "Model X" }


#Practice 3

def object_add(dict1, dict2):
    new_dict = {}
    for key1, val1 in dict1.items():
        new_dict[key1] = val1
    
    for key2, val2 in dict2.items():
        if key2 in new_dict:
            new_dict[key2] += val2
        else:
            new_dict[key2] = val2
    return new_dict
                
        
obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }


obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))
# { "a": 3, "b": 7, "c": 0, "e": 4 }



#Practice 4

def secret_cipher(str1, dict1):
    new_str = ''
    for key in str1:
        if key in dict1:
            new_str += dict1[key]
        else:
            new_str += '?'
            
    return new_str


print(secret_cipher("jello", {"j":"r","l":"s","e":"i" }))
# 'riss?'

print(secret_cipher("lantern", {"e":"o","l":"p","n":"m","r":"j" }))
# 'p?m?ojm'



        
#Practice 3
def object_add(dict1, dict2):
    new_count = {}
    for key, value in dict1.items():
        new_count[key] = value
        
    for key, value in dict2.items():
        if key in new_count:
            new_count[key] += value
        else:
            new_count[key] = value
    return new_count

obj1 = {"x":3,"y":10 }
obj2 = {"y":2,"x":1 }

print(object_add(obj1, obj2))
# { "x": 4, "y": 12 }


obj3 = {"a":3,"b":2,"c": -1 }
obj4 = {"b":5,"c":1,"e":4 }

print(object_add(obj3, obj4))
# { "a": 3, "b": 7, "c": 0, "e": 4 }

