def binary_search(array, k, low, high):
    
    if low > high:
        return None
    
    else:
        mid = (low + high) //2
        
        if k == array[mid]:
            return mid
        
        elif k < array[mid]:
            return binary_search(array, k, low, mid - 1)
        
        else:
            return binary_search(array, k, mid + 1, high)
        
array = [1,3,4,5,7,8,8]

result = binary_search(array,k=3, low=0, high=len(array) - 1)
print(result)