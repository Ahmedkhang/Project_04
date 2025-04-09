import random
def get_name():

    # i have stored multiple names in a list  
    
    my_friends = ['Ahmed', 'Ali', 'Sara', 'Mona', 'Aisha', 'Omar', 'Hassan', 'Fatima', 'Yasmin', 'Zainab']
     # using random.choice() to select a random name from the list and that too stored in a var
    random_friend = random.choice(my_friends)
    # return that variable
    return random_friend
    # return 'Alice'
    
def main():
    name = get_name()
    print('hello' + ' ' + str(name) + '!!' )
if __name__ == "__main__":
    main()    