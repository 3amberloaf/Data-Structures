def insertion_sort(array):
    """ inserting with a sorted sequence and doesnt use external data structure"""
    
    for i in range(1, len(array)):
        
        key = array[i]
        
        j = i -1
        
        while j >= 0 and key > array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

array = [12, 11, 13, 5, 6]
insertion_sort(array)
for i in range(len(array)):
    print ("% d" % array[i])