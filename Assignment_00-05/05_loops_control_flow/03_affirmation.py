#                import a random module
import random
    #   i have created an list of affirmations
affirmations = ["I am capable of achieving my goals.","I am strong and resilient.", "I am worthy of love and respect.", "I am constantly growing and improving.", "I am in control of my thoughts and emotions."]
    #   i have used the random module to select a random affirmation from the list
#   and stored it in a variable called random_affirmation
random_affirmation = random.choice(affirmations) 
def main():
          # print random affirmation
    print('write the following affirmation', random_affirmation)
    # take user input
    user_input = input()
    # initialze a while loop to check if the user input is equal to the random affirmation
    while user_input != random_affirmation:
        print('Incorrect affirmation. Try again.')
        user_input = input()
        
    print('Correct affirmation!')    

if __name__ == '__main__':
    main()