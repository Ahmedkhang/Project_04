# import random
# import string

# number = set(string.digits)
# upper_case = set(string.ascii_uppercase)
# lower_case = set(string.ascii_lowercase)
# special_char = (string.punctuation)

# length = int(input('Enter the length of password : '))
# pool = set()
# if input('Include Numbers? (y/n) : ').lower() == 'y':
#     pool.update(number)
# if input('Include uppercase? (y/n) : ').lower() == 'y':
#     pool.update(upper_case)
# if input('Include lowercase? (y/n) : ').lower() == 'y':
#     pool.update(lower_case)
# if input('Include Secial character? (y/n) : ').lower() == 'y':
#     pool.update(special_char)   
# if not pool:
#     print('Please enter atleast one character type')
# else:
#     password = ''.join(random.choices(list(pool), k=length) )
#     print(password)                 


# # password =random.choice(number,+ upper_case, + lower_case, +special_char)
# # print(password)

import string
import random

numbers = set(string.digits)
lower_case = set(string.ascii_lowercase)
upper_case = set(string.ascii_uppercase)
special_char = set(string.punctuation)


length = int(input('Enter the length of password : '))
pool = set()

if input('Do you want include numbers? (y/n) : ').lower() == 'y':
    pool.update(numbers)

if input('Do you want include Upercase? (y/n) : ').lower() == 'y':
    pool.update(upper_case)    

if input('Do you want include Lowercase? (y/n) : ').lower() == 'y':
    pool.update(lower_case)

if input('Do you want include Special Characters? (y/n) : ').lower() == 'y':
    pool.update(special_char)
if not pool:
    print('Please enter atleast one Character type')
else:  
    password = ''.join(random.choices(list(pool), k=length))       
    print(password)      