def double(num:int):
    return num * 2
  
    
def main():
    user_input = input('Enter an integer: ')
    nums = double(int(user_input))
    print(nums)
if __name__ == "__main__":
    main()    