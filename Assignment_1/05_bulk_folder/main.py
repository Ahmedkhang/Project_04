import os

def main():
    i = 0
    path = 'C:/python/Project_4/Assignment_1/03_bulk_folder/images/'
    for filename in os.listdir(path):
        my_dest = 'img' + str(i) + '.png'
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source,my_dest)
        i += 1


if __name__ == '__main__':
    main()    