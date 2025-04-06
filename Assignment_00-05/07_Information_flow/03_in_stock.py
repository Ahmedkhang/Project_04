def in_stock(fruit:str):
    fruit = ['banana', 'apple', 'orange', 'grape']
    if 'banana' in fruit:
        return 12
    if 'apple' in fruit:
        return 10
    if 'orange' in fruit:
        return 8
    if 'grape' in fruit:
        return 5
    else:
        return 0
        print("Yes, we have bananas")
def main():
    user_input = input("Enter the fruit you want to check: ")
    stock = in_stock(user_input)
    if stock > 0:
        print(f'{user_input} is in stock with {stock} items.')
    else:
        print(user_input,'is not in stock.')    
if __name__ == '__main__':
    main()    