def main():
    num = int(input('Enter a number between 1-10 to double : '))
    while num < 100:
        print(num)
        num = num * 2
    print(f'Your number is {num} and it is greater than 100!')
if __name__ == '__main__':
    main()    