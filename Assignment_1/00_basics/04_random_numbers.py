import random
def main():
    nums = 0
    while nums <=10:
        
        num = random.randint(1,99)

        print(f'{nums}: {num}')
        nums += 1

if __name__ == '__main__':
    main()    