def print_ones_digit(num:int):
   
       num2 = num % 10
       if num2 % num:
            print('The last digit is ',num2)
       else:
            print('Please enter a number which is greater than 10!!')     

def main():
    user_input = int(input('Enter a number : '))
    # num = int(user_input)
    # print(num)
    # print(user_input)
    print_ones_digit(user_input)
    
if __name__ == '__main__':
    main()    