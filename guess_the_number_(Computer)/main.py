import random



low = 1
high = 10
feedback = ''
attempts = 0

print('Think of a number between 1-10, and computer will try to guess it')

while feedback != 'c':
    guess = random.randint(low,high)
    attempts += 1
    print(f'Computer guess : {guess}')
    feedback = input('Is the guess too high(h) or too low(l) or correct(c): ').lower()
    if guess == 'h':
      high = high - 1
    elif guess == 'l':
       low = low + 1
    
print(f'Computer Guess your number {guess} correctly in attempts : {attempts} ')      