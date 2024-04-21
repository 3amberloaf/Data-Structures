def merge(subset1, subset2):
   i = 0
   j = 0
   result = []
   
   while (i < len(subset1) and j < len(subset2)):

       if subset1[i] < subset2[j]:
           result.append(subset1[i])
           i += 1
            
       else:
           result.append(subset2[j])
           j += 1
   
   while i < len(subset1):
        result.append(subset1[i])
        i += 1

   while j < len(subset2):
        result.append(subset2[j])
        j += 1
    
   return result
    
def mergeSort(array):
    
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    subset1 = mergeSort(array[:mid])
    subset2 = mergeSort(array[mid:])

    return merge(subset1, subset2)
        
        
array = [2, 1, 4, 8, 3, 6]
result = mergeSort(array)
print(result)