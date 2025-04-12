import random
prompt : str = 'What do you want? '
jokes = ['Why do programmers prefer dark mode?Because light attracts bugs', 'Why do Java developers wear glasses?Because they don\'t see sharp', 'How many programmers does it take to change a light bulb?None, that\'s a hardware problem', 'Why do Python programmers prefer using Jupyter notebooks?Because they can\'t handle the pressure of a full IDE', 'Why do programmers hate nature?It has too many bugs']
random_joke = random.choice(jokes)
sorry_statement = 'Sorry, I can only generate joke.'

def main():
    user_input = input(prompt).strip().lower()
    if user_input == 'joke':
        print(random_joke)
    else:
        print(sorry_statement)
if __name__ == '__main__':
    main()            

