import math
def main():
   AB : float = float(input('Enter the length of AB : '))
   AC : float = float(input('Enter the length of AC : '))

   BC = math.sqrt((AB ** 2) +(AC ** 2))
   print(BC) 
   
   

if __name__ == '__main__':
    main()    
