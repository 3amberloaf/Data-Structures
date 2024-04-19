
def search(array, key, n):
    for i in range(n):
        if (array[i] == key):
            return i
    
    # if key is not found, we print error
    return -1

def insert(array, element):
    """ Insert elements at the end"""
    array.append(element)

def insertPosition(array, n, x, position):
    """ Insert element at specific position"""

    for i in range(n-1, position-1, -1):
        array[i + 1] = array[i]
    
    array[position] = x

def remove(array, key):
    array.remove(key)

if __name__ == '__main__':
    
    array = [12, 34, 10, 6, 40]
    key = 14
    n = 5
    
    insert(array, element = 60)
    insertPosition(array, n, x= 14, position=2)

    remove(array, key=14)
    index = search(array, key, n)
        
    if index != -1:
            print("Element Found at position: " + str(index + 1))
    else:
            print("Element not found")