#Dictionary exercise examples:

movie = {
'title' : 'Fight Club',
'duration' : 168,
'starring' : ['Brad Pitt', 'Edward Norton'],
'genre' : ['Drama', 'Thriller']
}

print(movie['title'])
print(movie['duration'])
print(movie['starring'])
print(movie['genre'][0])
print(movie['genre'][1])


restaurant = {
    'owner' : 'Chris Ndlovu',
    'established' : 1996,
    'location' : 'Johanessburg',
    'menu' : ['Chicken', 'Pizza', 'Burger']
}


print('established' in restaurant)
print('employees' in restaurant)

some_key = 'menu'
print(restaurant['menu'])
print(restaurant[some_key])
print(restaurant.get(some_key))
print(restaurant.get('some_key'))
print(len(restaurant['menu']))

print('Pizza' in restaurant['menu'])

print('***************************************')


dog = {
    'name' : 'Ace',
    'breed' : 'German Shepard',
    'age' : 5,
    'color' : 'brown',
    'favoritefood' : ['dogmore', 'chicken'],
}


print(dog['age'])
print(dog['color'])
print(dog['favoritefood'])

dog['age'] += 1
dog['color'] = dog['color'].upper()
dog['favoritefood'].append('sausage')

print(dog['age'])
print(dog['color'])
print(dog['favoritefood'])

for key in dog: #key = name, breed, age, color, favouritefood
    print(key, 'is', dog[key])
    
    

#Practice 1
def email_parse(add_string):
    new_list = add_string.split('@')
    return {'username':new_list[0], 'domain':new_list[1]}

print(email_parse("coolcoder42@goodmail.com"))
# { 'username': 'coolcoder42', 'domain': 'goodmail.com' }

print(email_parse("az@woohoomail.com"))
# { 'username': 'az', 'domain': 'woohoomail.com' }

print(email_parse("1337pr0graMmer@coldmail.edu"))
# { 'username': '1337pr0graMmer', 'domain': 'coldmail.edu' }


#Practice 2
def key_pair(dict1, dict2, key_str):
    # return [dict1[key_str], dict2[key_str]]
    new_list = []
    for key in dict1, dict2:
        new_list.append(key[key_str])
    return new_list

cat1 = {"name":"jinkee","breed":"calico" }
cat2 = {"name":"garfield","breed":"red tabby" }

print(key_pair(cat1, cat2,"breed"))
# ['calico', 'red tabby']

print(key_pair(cat1, cat2,"name"))
# ['jinkee', 'garfield']


#Practice 3
def element_quantities(dict):
    new_list = []
    # for key in dict:
    #     for i in range(dict[key]):
    #         new_list.append(key)
    # return new_list

    for key, value in dict.items():
        for i in range(value):
            new_list.append(key)
    return new_list


quantities1 = {"cat":3,"bird":1,"dog":2 }
print(element_quantities(quantities1))
# ['cat', 'cat', 'cat', 'bird', 'dog', 'dog']

quantities2 = {"blue":3,"brown":1 }
print(element_quantities(quantities2))
# ['blue', 'blue', 'blue', 'brown']


#Practice 4
def max_object_value(dict1):
    new_list = []
    value_key = ''
    highest = 0
    for key in dict1:
        if dict1[key] > highest:
            value_key = key
            highest = dict1[key]
    new_list.append((value_key, highest))
    #return new_list
    return[value_key, highest]

print(max_object_value({"a":5,"b":2,"c":6,"d":7,"e":4 }))
# ['d', 7]

print(max_object_value({"lychee":11,"rambutan":13,"papaya":9 }))
# ['rambutan', 13]
