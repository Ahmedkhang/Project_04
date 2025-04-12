max_num : int = 10000
def main():
    current_num = 0
    next_num = 1
    while current_num < max_num:
        print(current_num)
        add_num = current_num + next_num
        current_num = next_num
        next_num = add_num
    print(f'Fibonacci number is {current_num}')    

if __name__ == '__main__':
    main()    