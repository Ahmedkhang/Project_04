def subtract_7(num:int):
   subt_value = num - 7
   return subt_value

def main():
    user_input = int(input('Enter a number to subtract 7 : '))
    result = subtract_7(user_input)
    print(f'The result of subtracting 7 from {user_input} is: {result}')
if __name__ == '__main__':
    main()