# Basic implementation of stack operations

class Stack:
    def __init__(self): # Initializes the stack
        self.items = []
    
    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the top of the stack."""
        self.items.append(item)
    
    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            return None
        return self.items.pop()
    
    def peek(self):
        """Return the top item from the stack without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]
    
    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)
