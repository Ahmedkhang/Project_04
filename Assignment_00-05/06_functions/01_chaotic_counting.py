import random
DONE_LIKELIHOOD = 0.1
def chaotic_counting():
    for i in range (1,10):
      
        if done():
            return
        print(i)

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False
def main(): 
       print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
       chaotic_counting()
       print('i am done')
if __name__ == "__main__":
    
    main()       