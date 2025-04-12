max_length : int= 3

def shorten(empty_list):
    while len(empty_list) > max_length:
        last_element = empty_list.pop()
        print(last_element)    
def get_1st():
    # create an empty list
    empty_list = []
    # take input from user
    user_input = input('Enter a value : ')

    # initilize while loop in which the condition will be : if a user enter nothing like an empty string it will stop while loop

    while user_input != '':
          empty_list.append(user_input)
          user_input = input('Enter a value : ')
    # print(empty_list)

    return empty_list
def main():
    empty_list = get_1st()
    shorten(empty_list)
if __name__ == '__main__':
    # get_1st()
    main()
