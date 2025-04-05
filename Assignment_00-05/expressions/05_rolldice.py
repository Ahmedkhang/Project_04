import random
die_sides:int = 6

def main():

   die_1 = random.randint(1,die_sides)
   die_2 = random.randint(1,die_sides)

   total = die_1 + die_2
    
   print('Dice has ' + str(die_sides) + ' sides each')
   print('die 1 = ' + str(die_1)) 
   print('die 2 = ' + str(die_2)) 
   print('Total Score = ' + str(total)) 
    
   


if __name__ == '__main__':
    main()    