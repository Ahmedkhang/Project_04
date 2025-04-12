min_height = 55  

def main():
    user_age = input('Enter your height : ')
    while True:
        if user_age == '':
            break
        try:
            user_age = int(user_age)
        except ValueError: 
            print('Invalid Input, Please enter a number : ') 
            # user_age = input('Enter your height : ')
            continue
        if user_age >= 55:
             print('You are tall enough, you can ride')
             break
        else:
            print('You are not tall enough, Try next time')   
            break  
    
    



if __name__ == '__main__':
    main()    