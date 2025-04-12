import random
def main():
    my_num = random.randint(1,99)
    lives = 7
    print('Welcome to the Guess My Number game!')
    # print('You have 7 lives to guess the number.')
    # user_guess = int(input('Guess a number between 1 and 99: '))
    while lives > 0:
        print('You have', lives, 'lives left')
        user_guess = int(input('Guess a number between 1 and 99: '))

        if user_guess == my_num:
          
            print('You guessed it! the number was', my_num)  
            break     
        elif user_guess < my_num:
            print('Too low!')
        elif user_guess > my_num:
            print('Too high!')
        else:
            print('Please enter a number between 1 and 99')    
        lives -= 1
        if lives == 0:
            print('Sorry, you are out of lives. The number was', my_num)
        
        
        
if __name__ == '__main__':
    main()
