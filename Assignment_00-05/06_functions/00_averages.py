def average_num(num1:float,num2:float):
    total = num1 + num2
    return total / 2
    
def main():

    task1 = average_num(100,324)
    task2 = average_num(289,731)
    average = average_num(task1,task2)
    print('Task1 :', task1)
    print('task2 :', task2)
    print(average)


if __name__ == "__main__":
    main()
    