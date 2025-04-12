def get_numbers():
    empty_arr=[]
    user_input = int(input('Enter a number: '))
    while True:
        empty_arr.append(user_input)
        user_input = input('Enter a number: ')
        try:
            user_input = int(user_input)
        except ValueError:
            # print("Invalid input. Please enter a number.")
            break
   
    return empty_arr    

def get_dict(numbers):
    numbers_dict = {}
    for number in numbers:
        if number in numbers_dict:

            numbers_dict[number] += 1
        else:
            numbers_dict[number] = 1
    # print(numbers_dict)        
    return numbers_dict    
        
def print_num_in_list(numbers_dict):
    for num in numbers_dict:
        print(f'{num} appears {numbers_dict[num]} times')
        
def main():
    num_list = get_numbers()
    num_dict = get_dict(num_list)
    print_num_in_list(num_dict)
if __name__ == "__main__":
    main()    