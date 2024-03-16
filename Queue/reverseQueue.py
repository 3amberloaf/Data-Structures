# Reverse an array using a queue FIFO

from collections import deque
from queue import Queue

def reverse_array_with_queue_using_dequeue(A):
    n = len(A)
    queue = deque()

    # Insert elements into the queue
    for i in range(n):
        queue.append(A[i])

    # Remove elements from the queue and put them back into A in reverse order
    for i in range(n):
        A[i] = queue.pop()  # Using pop() instead of popleft() to simulate stack behavior

    return A


    