import random
def greetings(name:str):

    greet :str  = ['Hello', 'Hi', 'Hey']
    random_greet = random.choice(greet)
    print(random_greet, name)
    
def main():
    user_name = input("Enter your name: ")
    greetings(user_name)
if __name__ == '__main__':
    main()