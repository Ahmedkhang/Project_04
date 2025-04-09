def main():
    for i in range(10):
        if is_odd(i):
            print(i,'is odd')
        else:
            print(i,'is even')
            
def is_odd(value: int):
    remiander = value % 2
    return remiander == 1
    # print(remainder)


if __name__ == '__main__':
    main()