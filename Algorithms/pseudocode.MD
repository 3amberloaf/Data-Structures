# Array Max
Determines the max element in an array

### Pseudocode

```python
Algorithm arrayMax(A, n):
    Input: The array, A, storing n>= 1 integers
    Output: The maximum element in A

    currentMax <- A[0]
    for i <- 1 to n-1 do
        if currentMax < A[i] then 
            currentMax <- A[i]
    return currentMax
```

### Python

```python
def arrayMax(A):
    # Assuming A is a list of integers and contains at least one element
    currentMax = A[0]  # Initialize currentMax to the first element of A
    n = len(A)  # Get the number of elements in A
    for i in range(1, n):  # Iterate from the second element to the last element
        if currentMax < A[i]:  # If currentMax is less than the current element
            currentMax = A[i]  # Update currentMax to the current element
    return currentMax  # Return the maximum element found in A
```

# Recursive Max
Determines the max element in an array using recursion. 

### Pseudocode

```python
Algorithm recursiveMax(A, n):
    Input: The array, A, storing n>= 1 integers
    Output: The maximum element in A

    if n <- 1 then
        return A[0]
    return max{recursiveMax(A,n-1), A(n-1)}
```

### Python

```python
def recursiveMax(A, n):
    # Base case: If the array has only one element, return that element
    if n == 1:
        return A[0]
    # Recursive case: Return the maximum between the last element an the maximum of the rest of the array
    return max(recursiveMax(A, n-1), A[n-1])
```

# Maximum Sub Array
Compute the maximum of every possible subarray summation of the array A seperately. The outer loop, for index j, will iterate n times, its inner loop, for index k, will iterate at most n times, and the inner-most loop, for index i, will iterate at most n times. The running time is O(n^3).

### Pseudocode
```python
Algorithm MaxsubSlow(A):
    Input: An n-element array A of numbers, indexed from 1 to n
    Output: The maximum subarray sum of array A

    m <- 0 // the max found so far
    for j <- 1 to n do
        for k <- j to n do
        s <- 0 // the next partial sum we are computing
        for i <- j to k do
            s <- s + A[i]
        if s > m then
            m <- s
    return m
```

### Python

```python
def MaxsubSlow(A):
    n = len(A)  # Assuming the list is indexed from 0 to n-1 in Python
    m = 0  # The max sum found so far
    for j in range(n):  # Python uses 0-based indexing
        for k in range(j, n):
            s = 0  # The next partial sum we are computing
            for i in range(j, k + 1):
                s += A[i]
            if s > m:
                m = s
    return m
```
