import random
# declaring a var for game 

game = True

# lives in a game 
lives = 3

# generating a random number
computer_number = random.randint(1,10)
# initializing while loop 

while game and lives > 0:
    # taking input from user
    user_guess = int(input('Guess the number between 1-10 : '))
    # correct guess and the game will over
    if user_guess == computer_number:
     print('You Guess the correct number')
     game = False
    else:
     print('Wrong Guess, Try Again!')
     lives = lives - 1
     print(f'You have {lives} lives left' )

    #  if lives remains 0 game will  be over
     
     if lives == 0:
       print(f'Game Over!! You have {lives} lives left')
       game =False
       

