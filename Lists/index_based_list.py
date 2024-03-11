# Implementation of Index-Based List

class IndexBasedList:
    def __init__(self, capacity=10):
        self.capacity = capacity  # Initial capacity of the list
        self.size = 0  # Current size of the list (number of elements it contains)
        self.data = [None] * self.capacity  # Allocate storage for the elements

    def __resize(self, new_capacity):
        """Resize the internal storage of the list to a new capacity."""
        new_data = [None] * new_capacity
        for i in range(self.size):  # Copy existing elements to the new storage
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, item):
        """Add an item to the end of the list."""
        if self.size == self.capacity:
            self.__resize(2 * self.capacity)  # Double the capacity if no space
        self.data[self.size] = item
        self.size += 1

    def add(self, index, item):
        """Insert an item at a specified index."""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self.__resize(2 * self.capacity)  # Double the capacity if no space

        # Shift elements to the right to make space for the new item
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = item
        self.size += 1

    def get(self, index):
        """Get the item at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]

    def set(self, index, item):
        """Set the item at the specified index."""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = item

    def remove(self, item):
        """Remove the first occurrence of the item from the list."""
        for i in range(self.size):
            if self.data[i] == item:
                # Shift elements to the left to fill the gap
                for j in range(i, self.size - 1):
                    self.data[j] = self.data[j + 1]
                self.data[self.size - 1] = None  # Clear the last element
                self.size -= 1
                return
        raise ValueError("Item not found in the list")

    
    def __str__(self):
        return "[" + ", ".join(str(self.data[i]) for i in range(self.size)) + "]"

# Example usage
iblist = IndexBasedList()
iblist.append(1)
iblist.append(2)
iblist.append(3)
print(iblist)  # Output: [1, 2, 3]

iblist.add(3, 4)
print(iblist)  # Output: [1, 4, 2, 3]

print(iblist.get(2))  # Output: 2
iblist.set(2, 5)
print(iblist)  
