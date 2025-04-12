def main():
    user_input = input("Enter a number: ")
    curr_val = int(user_input)
    while curr_val < 100:

        curr_val = curr_val + curr_val
        print(curr_val)

if __name__ == '__main__':
    main()   