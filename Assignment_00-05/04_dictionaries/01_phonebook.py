def read_phone_numbers():
    phone_number = {}
    # user_name = input('Name : ')
    while True:
        user_name = input('Name : ')
        if user_name == '':
          break
        user_phone = input('Number : ')
        phone_number[user_name] = user_phone
    # print(phone_number)    

    
    return phone_number
def print_phonebook(phone_number):
   for name in phone_number:
      print(f'{name} : {phone_number[name]}')
def lookup_numbers(phone_number):
   while True :
      name = input('enter a name to look up : ')
      if name == '':
         break
      if name not in phone_number:
         print(f'{name} is not available')
      else:
         print(phone_number[name])   
         
# print_phonebook(phone_number=)
def main():
   phone_number = read_phone_numbers()
   print_phonebook(phone_number)
   lookup_numbers(phone_number)
if __name__ == '__main__':
   main()   