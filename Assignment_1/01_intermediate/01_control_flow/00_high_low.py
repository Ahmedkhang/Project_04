import random
rounds = 1
score = 0

while rounds <= 5:
    print(f'\nRound {rounds}\n')
    my_num = random.randint(1,99) 
    print(f'My number : {my_num}\n')
    computer_num = random.randint(1,99)
    user_input = input('High or Low? : ').lower()
    if my_num > computer_num and user_input == 'high':
        score += 1
        print('You guessed right!')
        print(f'Your score is {score}\n')
    elif my_num < computer_num and user_input == 'low':
        score += 1
        print('You guessed right!')
        print(f'Your score is {score}\n')
    else:
        print('You guessed wrong!')
        print(f'Your score is {score}\n') 
    if rounds == 5:
        if score >= 3:
            print('----------You win!----------')
            break
        else:
            print('----------You lose!----------')           
        

    
    
    rounds += 1