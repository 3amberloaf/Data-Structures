# Recursive binary search that locates the left-most occurrence of the search key X in the array

def left_most_binary_search(array, left, right, x):
    
    if right >= left:
        mid = (left + right) // 2
    # sets mid
        
        if array[mid] == x:
        # If mid is x, check if it's the left-most by checking element before mid
        
            if mid == left or array[mid - 1] != x:
                return mid
            # if mid is the first element or element before mid is not x, then return mid

            else:
                return left_most_binary_search(array, left, mid - 1, x)
            
        # if the element is greater than the middle array element, shift search to the right
        elif x > array[mid]:
            return left_most_binary_search(array, mid + 1, right, x)
        # if element is smaller than middle, shift search to the left
        else:
            return left_most_binary_search(array, left, mid -1, x)
    else:
        return -1  
        # x is not in the array

array = [2, 4, 5, 5, 5, 8, 10, 20, 25]
x = 5

result = left_most_binary_search(array, 0, len(array) - 1, x)

if result != -1:
    print("element present at index", str(result))
else:
    print("Element not in array")