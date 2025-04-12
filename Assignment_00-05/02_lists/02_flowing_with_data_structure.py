def add_copies(my_list,user_msg):
    for i in range(3):
        my_list.append(user_msg)

def main():
    user_msg = input('Enter a message to copy 3 times : ')
    my_list = []
    print('before : ', my_list)
    add_copies(my_list,user_msg)
    print('after : ', my_list)
if __name__ == '__main__':
        main()
