def get_first_elem(list):
   print(list[0])
   
def user_list():
    list = []
    elements : str = input('Enter the one element of list or press enter to stop : ')
    
    while elements != "":
     list.append(elements)
     
     elements : str = input('Enter the one element of list or press enter to stop : ')
    return list
def main():

   list = user_list()
   get_first_elem(list)

if __name__ == '__main__':
    main()    
