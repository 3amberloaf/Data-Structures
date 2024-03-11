import random
import time

def selection_sort(arr):
    # Implementation of selection sort
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
        
def insertion_sort(arr):
    # Implementation of insertion sort
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        
def heap_sort(arr):
    # Implementation of heap sort
    def heapify(arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l

        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
def merge_sort(arr):
    # Implementation of merge sort
    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[l + i]
        for j in range(n2):
            R[j] = arr[m + 1 + j]

        i = j = 0
        k = l
        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def divide_conquer(arr, l, r):
        if l < r:
            m = (l + (r - 1)) // 2
            divide_conquer(arr, l, m)
            divide_conquer(arr, m + 1, r)
            merge(arr, l, m, r)

    divide_conquer(arr, 0, len(arr) - 1)

def quick_sort(arr):
    # Implementation of quick sort
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(arr, 0, len(arr) - 1)
    

def main():
    array_sizes = [10, 100, 1000, 10000, 1000000, 10000000]
    sorting_algorithms = [
        ("selection_sort", selection_sort),
        ("insertion_sort", insertion_sort),
        ("heap_sort", heap_sort),
        ("merge_sort", merge_sort),
        ("quick_sort", quick_sort)
    ]

    for size in array_sizes:
        print(f"Array Size: {size}")
        test_array = [random.randint(1, 100) for _ in range(size)]
        
        for name, sort_function in sorting_algorithms:
            copied_array = test_array.copy()
            start_time = time.time()
            sort_function(copied_array)
            duration = time.time() - start_time
            print(f"{name}: {duration:.6f} sec")
        
        print("\n")

if __name__ == "__main__":
    main()
