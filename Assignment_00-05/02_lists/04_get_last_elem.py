def get_last_elem(list):
  
      print(list[- 1])
   
def user_list():

    list = []
    elements : str = input('Enter the one element of list or press enter to stop : ')
    
    while elements != "":
     list.append(elements)
     
     elements : str = input('Enter the one element of list or press enter to stop : ')
    return list

def main():

   list = user_list()
   get_last_elem(list)

if __name__ == '__main__':
    main()    
