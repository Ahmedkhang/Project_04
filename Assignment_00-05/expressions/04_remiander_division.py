def main():
  num1 : int = int(input('Enter the value to be divided : '))
  num2 : int = int(input('Enter the value to divide by : ')) 

  divided_value = num1 // num2
  remainder_value = num1 % num2
  print(f'The result of a division is ' + str(divided_value) + ' and the remainder is ' + str(remainder_value))
if __name__ == '__main__':
    main()    