def naive_search(l,target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1
def binary_search(l,target,low=None,high=None):
    if low is None:
        low = 0
    if high is None :
        high = len(l) - 1
    if high < low:
        return -1    
    midpoint = (low + high) // 2
    if l[midpoint] == target :
        return midpoint
    elif l[midpoint] < target:
        return binary_search(l,target,low,midpoint - 1)    
    else:
        return binary_search(l,target,midpoint+1,high)
if __name__ == "__main__":
        l = [1,2,3,4,5,6,64,8,9,10]
        target = 4
        print(naive_search(l,target))
        # print(binary_search(l,target))
        print(binary_search(l,target)) 
          