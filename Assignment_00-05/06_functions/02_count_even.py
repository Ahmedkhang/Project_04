def count_even(empty_list):

    count = 0
    for num in empty_list:
        if num % 2 == 0:
            count += 1
    print(f'The number of even numbers in the list is {count}')    
def get_list_of_evens():
    empty_list = []
    user_input = input('Enter an integer or press enter to stop : ')
    while user_input != '':
        empty_list.append(int(user_input))
        user_input = input('Enter an integer or press enter to stop : ')
    return empty_list    
def main():
   empty_list = get_list_of_evens()
   count_even(empty_list)
if __name__ == "__main__":
    main() 