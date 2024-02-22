# Iterative heap sort

def buildMaxHeap(arr, n): 
    # converts array into max Heap
	for i in range(n):
		
		# if child is bigger than parent 
		if arr[i] > arr[int((i - 1) / 2)]:
			j = i 
	
			# while the child is greater than the parent
			while arr[j] > arr[int((j - 1) / 2)]:
				(arr[j], arr[int((j - 1) / 2)]) = (arr[int((j - 1) / 2)], arr[j]) # swap child and parent 
				j = int((j - 1) / 2) # j becomes the parent node

def heapSort(arr, n): 
    
	buildMaxHeap(arr, n) 

	for i in range(n - 1, 0, -1):
		
		# swap root of array (aka maximum) with last element
		arr[0], arr[i] = arr[i], arr[0]
	
		# maintaining heap property after each swapping 
		j, index = 0, 0
		
		while True:
            # restores heap property
			index = 2 * j + 1 # left child of the current node
			
			# if left child is smaller than right child point index variable to right child 
			if (index < (i - 1) and arr[index] < arr[index + 1]): 
				index += 1
		
			# if parent is smaller than child then swapping parent with child having higher value 
			if index < i and arr[j] < arr[index]: 
				arr[j], arr[index] = arr[index], arr[j] 
		
			j = index 
			if index >= i:
				break

# Driver Code
if __name__ == '__main__':
	arr = [10, 20, 15, 17, 9, 21] 
	n = len(arr) 
	
	print("Given array: ")
	for i in range(n):
		print(arr[i], end = " ") 
		
	print() 

	heapSort(arr, n) 

	# print array after sorting 
	print("Sorted array: ")
	for i in range(n):
		print(arr[i], end = " ")
