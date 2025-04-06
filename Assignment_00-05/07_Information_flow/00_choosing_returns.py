adult_age = 18
def is_adult(user_age:int):
    if user_age >= 18:
        return True
    return False
def main():
    user_age = int(input("Enter your age: ")) 
    print(is_adult(user_age))
    # print(is_adult)
if __name__ == '__main__':
    main()    