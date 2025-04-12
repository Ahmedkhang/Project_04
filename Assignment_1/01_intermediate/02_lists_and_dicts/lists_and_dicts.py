# Now practice writing code with lists! Implement the functionality described in the comments below.
# Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# def main(): 
#     my_list = ['apple','pineapple','banana','orange','grape']
#     print(len(my_list))
#     my_list.append('mango')
#     print(my_list)
def access_elems(my_list,index):
  try:
    return my_list[index]
  except IndexError:
    return 'Index out of range'
def modify_list(my_list,index,new_value):
  try:
     my_list[index] = new_value
     return my_list
  except IndexError:
    return 'Index out of range'
def slicing_elems(my_list,start,end):
  try:
    return my_list[start:end]
    # return my_list
  except IndexError:
    return 'Invalid'   
    
  
def index_game():
  my_list = [1,2,3,4,5]
  print('my_list: ',my_list)
  print('Enter any of the following functions, access,modify,slicing : ')
  user_input = input('Enter your choice : ').lower()

  if user_input == 'access':
    index = int(input('Enter the index you want to access : '))
    print(access_elems(my_list,index))
  elif user_input == 'modify':
    index = int(input('Enter the index you want to modify : '))
    new_value = int(input('Enter the new value : ')) 
    print(modify_list(my_list,index,new_value))
  elif user_input =='slicing':
    start = int(input('Enter the start index : '))
    end = int(input('Enter the end index : '))
    print(slicing_elems(my_list,start,end)) 
index_game()    
