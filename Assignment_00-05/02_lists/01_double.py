def main():


    # #   # create a int list
    # numbers_list :list[int] = [2,4,5,2,7] 
    # print(len(numbers_list))

    # for i in range(len(numbers_list)):
    #     elements = numbers_list[i]
    #     numbers_list[i] = elements * 2
    # print(numbers_list) 
     
    numbers : list[int] = [1,2,3,4,6,8,9]
    for i in range(len(numbers)):
        elements_at_index = numbers[i] 
        numbers[i] = elements_at_index * 2
    print(numbers)

if __name__ == '__main__':
    main()