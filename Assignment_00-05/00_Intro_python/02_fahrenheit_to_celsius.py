def main():


    print('---------- Fahrenheit to Celsius ----------')

    fahrenheit = float(input('Enter the temperature in Fahrenheit : '))

    celsius = (fahrenheit - 32) * 5.0/9.0

    print(f'{fahrenheit}F = {celsius}C')

if __name__ == '__main__':
    main()
