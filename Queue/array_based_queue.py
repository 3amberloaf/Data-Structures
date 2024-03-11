# Implementation of array-based queue

class ArrayQueue:
    def __init__(self, capacity):
        self.items = [None] * capacity  # Initialize the array with a fixed capacity
        self.front = 0  # Points to the front of the queue
        self.rear = -1  # Points to the rear of the queue
        self.size = 0  # Keeps track of the number of items in the queue
        
    def is_empty(self):
        return self.size == 0
    
    def is_full(self):
        return self.size == len(self.items)
    
    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full")
        self.rear = (self.rear + 1) % len(self.items)  # Circular increment MODULO OPERATION
        self.items[self.rear] = item # inserted the item at rear position
        self.size += 1 # increments size to keep track 
        
    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        item = self.items[self.front] # retrieve the front item
        self.items[self.front] = None  # Helps clear the slot
        self.front = (self.front + 1) % len(self.items)  # Circular increment
        self.size -= 1 # decrements size
        return item 

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[self.front]
