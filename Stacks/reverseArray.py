# Reverse an array using a stack

def reverseArray(array):
    n = len(array)
    stack = []
    
    # Iterate through length of array and insert items from arrays index
    for i in range(n):
        stack.append(array[i])
    
    # Iterate through length of array and remove items from arrays index in reverse order
    for i in range(n):
        array[i] = stack.pop()
    
    return array

original_array = [1, 2, 3, 4, 5]
reversed_array = reverseArray(original_array.copy())  # Using .copy() to avoid modifying the original array
print(reversed_array)


