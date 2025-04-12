def main():

    fruits_menu = {
        'apple': 100,
        'banana': 50,
        'orange': 80,
        'grape': 120,
    }
    total_bill = 0
    for fruits in fruits_menu:
        price = fruits_menu[fruits]
        amount = int(input(f'How many {fruits} do you want ? : '))
        total_bill += price * amount
    print(f'Total bill is : {total_bill}')    
if __name__ == '__main__':
    main()        