# Binary search using recursion
# Time complexity O(log n)
# Space complexity O(log n)

def binary_search(array, low, high,x):
    # returns index of x in array if present
    
    if high >= low:
        # checks base case
        
        mid = (low + high) // 2
        
        if array[mid] == x:
            return mid
        # if the element is present in the middle return the middle
        
        elif array[mid] > x:
            return binary_search(array, low, mid - 1, x)
        # if element is smaller than middle element then rerun algorithm on left subarray
        
        else:
            return binary_search(array, mid + 1, high, x)
        # otherwise element must be in the right subarray
    
    else:
        return -1
    # element isnt in the array

array = 2, 4, 5, 5, 5, 8, 10, 20, 25
x = 2

result = binary_search(array, 0, len(array) - 1, x)

if result != -1:
    print("element present at index", str(result))
else:
    print("Element not in array")