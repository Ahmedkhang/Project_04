def main():
# Anton is 21 years old.

# Beth is 6 years older than Anton.

# Chen is 20 years older than Beth.

# Drew is as old as Chen's age plus Anton's age.

# Ethan is the same age as Chen.

 AntonAge : int = 21
 BethAge :int = AntonAge + 6
 ChenAge : int = BethAge + 20
 DrewAge : int = ChenAge + AntonAge
 EthanAge : int = ChenAge
 
 print(f'Anton is {AntonAge}')
 print(f'Beth is {BethAge}')
 print(f'Chen is {ChenAge}')
 print(f'Drew is {DrewAge}')
 print(f'Ethan is {EthanAge}')

if __name__ == '__main__':
    main()    