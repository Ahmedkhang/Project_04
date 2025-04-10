def print_multiple_msg(msg:str, times:int):
    # msg = input('Enter a message: ')
    # times = int(input('Enter how many times to print a message : '))

    while times > 0:
        print(msg)
        times -= 1 # decrement the times variable by 1, so that the loop will eventually stop


def main():
    msg = input('Enter a message: ')
    user_input = int(input('Enter how many times to print a message : '))
    print_multiple_msg(msg, user_input)

if __name__ == "__main__":
    main()    