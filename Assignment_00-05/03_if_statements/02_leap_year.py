def main():
    user_input = int(input('Enter a year : '))
    if user_input % 4 == 0:
        if user_input % 100 == 0:
            if user_input % 400 == 0:
                print('Thats a leap year')
            else:
                print('Thats not a leap year')  
        else:
            print('Thats a leap year')    
    else:
        print('Thats not a leap year')                 
if __name__ == '__main__':
    main()