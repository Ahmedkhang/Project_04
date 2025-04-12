import random
def main():
    number = random.randint(0,99)
    print(number)
    user_guess = int(input('Enter a guess : '))
    while user_guess != number:
        if user_guess > number:
            print('your Guess is too high!')
        elif user_guess < number:
            print('Your guess is too low!') 
        
        else:
            print('Invalid input!')
        user_guess = int(input('Enter a guess : ')) 
    print(f'Your guess was correct {number}!')                   
    

if __name__ == '__main__':
    main()    