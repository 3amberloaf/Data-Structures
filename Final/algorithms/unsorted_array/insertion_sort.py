def insertion_sort(array):
    """ inserting with a sorted sequence and doesnt use external data structure"""
    
    for i in range(1, len(array)):
        
        key = array[i] # array position starts at beginning
        
        j = i -1 # j is initialized
        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j] # moving array forward
            j -= 1 # moving j back
        array[j + 1] = key # key becomes array position moved forward

array = [12, 11, 13, 5, 6]
insertion_sort(array)
for i in range(len(array)):
    print ("% d" % array[i])
    

# Consider a binary tree search of size N, and let k be a number between 1 and N. Assuming that all elements of the tree are distinct, 
# write a function that returns the kth element of the tree. You have to do so by navigating the tree itself.

class 