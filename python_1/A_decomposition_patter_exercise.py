#Practice 1

def double_vowel(str1):
    new_str = ''
    vowels = 'aeiou'
    for key in str1:
        if key in vowels:
            new_str += key + key
        else:
            new_str += key
    
    return new_str
    
    
print(double_vowel("runner"))
# 'ruunneer'

print(double_vowel("stoplight"))
# 'stoopliight'

print(double_vowel("gardener"))
# 'gaardeeneer'



#Practice 2

def funny_phrase(str1):
    new_str = []
    new_list = str1.split(' ')
    for i in range(len(new_list)):
        if i % 2 > 0:
            new_str.append(double_vowel(new_list[i]))
        else:
            new_str.append(new_list[i])
    return (' ').join(new_str)

    


print(funny_phrase("she dreamed of being a runner"))
# 'she dreeaameed of beeiing a ruunneer'

print(funny_phrase("park near the stoplight"))
# 'park neeaar the stoopliight'

print(funny_phrase("we need many gardeners"))
# 'we neeeed many gaardeeneers'


#Practice 3

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
print(is_prime(11))# True
print(is_prime(8))# False
print(is_prime(7))# True
print(is_prime(21))# False
print(is_prime(2))# True
print(is_prime(15))# False
print(is_prime(1))# False



#Practice 4

def pick_primes(list_num):
    new_list = []
    for i in list_num:
        if is_prime(i):
            new_list.append(i)
    return new_list
    
    
print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []

