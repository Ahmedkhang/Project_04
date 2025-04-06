def get_user_data():
    f_name = input('Enter your first name: ')
    l_name = input('Enter your last name: ')
    email = input('Enter your email address: ')
    print(f'First Name: {f_name}')
    print(f'Last Name: {l_name}')
    print(f'Email: {email}')

    return f_name, l_name, email
def main():

    user_data = get_user_data()
    print('User data received:',user_data)

if __name__ == '__main__':
    main()