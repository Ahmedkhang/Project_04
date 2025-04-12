import random
     #  creating a tuple
options = ("rock","paper","scissor")
player = None
    #    Pickng random option
computer = random.choice(options)

game = True
            # initializing game with while loop
while game:
    player = None
    while player not in options:
        player = input("Enter a choice : ('rock','paper','scissor) : ")
    print(f'Player : {player}')
    print(f'Computer : {computer}')    
            #    definig conditions through if else ladder
    if player == computer:
        print("Game tied")
    elif player == 'rock'  and computer == 'scissor':
        print('You win!')   
    elif player == "scissor" and computer == 'paper':
        print('You win!')    
    elif player == 'paper' and computer == 'rock':
        print('You win!')  
    else: 
        print('you Lose')  
    if not input('Play Again? (y/n ): ').lower() == 'y':
        game = False      
print('Thanks for playing')        
