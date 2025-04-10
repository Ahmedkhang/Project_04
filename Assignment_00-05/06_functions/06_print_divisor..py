def print_divisor(num:int):
    print(f'Here are numbers which are divisible by {num}')
    for i in range(num):
        # if i % 2 == 0:
            curr_divisor = i + 1
            # print(curr_divisor)
            if num % curr_divisor == 0:
               print(curr_divisor)
 
def main():
    num = int((input('Enter a number: ')))
    print_divisor(num)
if __name__ == "__main__":
    main()    