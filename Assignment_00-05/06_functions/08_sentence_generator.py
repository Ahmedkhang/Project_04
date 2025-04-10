def sentence_generator(msg,num_input):
    if num_input == 0:
          print(f"I am excited to add this {msg} to my vast collection of them!")
    elif num_input == 1:
          print("It's so nice outside today it makes me want to " + msg + "!")  
    elif num_input == 2:
          print("Looking out my window, the sky is big and ", msg + "!")   
    else: 
         print('Invalid Input')             

def main():
    user_msg : str = input('Enter a word : ')
    print('is this a noun,verb or adjective ?')
    user_num: int = int(input('Type 0 for noun 1 for verb and 2 for adjective : '))
    sentence_generator(user_msg,user_num)
if __name__ == "__main__":
    main()    