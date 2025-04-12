def main():
    empty_list = []
    user_val = input('Enter a value : ')

    while user_val:
        empty_list.append(user_val)
        user_val = input('Enter a value : ')
    print('Here the list', empty_list)    
if __name__ == '__main__':
    main()        