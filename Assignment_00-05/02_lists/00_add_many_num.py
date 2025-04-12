
def add_numbers(numbers_list):


    total : int = 0
    for numbers in numbers_list:
        total += numbers


    return total    

def main():



    numbers_list : list[int] = [10,4,3,5,2,6]
    # num : int = [3,4,5,6,3,5,2,3,4,4,5,6,7]
    sum_of_numbers = add_numbers(numbers_list)
    print(sum_of_numbers)



if __name__ == '__main__':
    main()