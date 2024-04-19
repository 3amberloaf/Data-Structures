import heapq

def pqSort(array):
    
    priority_queue = []
    
    # iterate through keys and add to priority queue
    for keys in array:
        heapq.heappush(priority_queue, keys) 
        
    # iterate through array and heappop removes the smallest element from priority queue and adds to array in order
    for i in range(len(array)):
        array[i] = heapq.heappop(priority_queue)
    
    return array

array = [12, 34, 10, 6, 40]
sorted_array = pqSort(array.copy())  # We copy the array to avoid in-place sorting for demonstration
print(sorted_array)