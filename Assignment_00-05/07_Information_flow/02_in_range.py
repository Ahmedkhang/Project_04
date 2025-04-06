def in_range(n:int,low:int,high:int):
    if n > low and n < high :
        return True
    else:
        return False
def main():
    n_num : int = int(input("Enter a number: "))
    low_num : int = int(input("Enter the lower bound: "))
    high_num : int = int(input("Enter the upper bound: "))
    print(in_range(n_num,low_num,high_num))
if __name__ == '__main__':
    main()    