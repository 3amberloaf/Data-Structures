class Node:
    def __init__(self, data):
        self.data = data  # Data stored in the node
        self.next = None  # Reference to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the list with no nodes
    
    def append(self, data):
        """Append a new node with the given data to the end of the list."""
        if not self.head:  # If the list is empty, new node becomes the head
            self.head = Node(data)
            return
        last = self.head
        while last.next:  # Traverse the list to find the last node
            last = last.next
        last.next = Node(data)  # Create a new node and link it at the end

    def print_list(self):
        """Print all elements of the list."""
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')  # Indicate the end of the list

    def search(self, key):
        """Search for the first node with 'key' as its data and return it."""
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None  # Key not found in the list

# Example usage:
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)

llist.print_list()  # Output: 1 -> 2 -> 3 -> None

search_result = llist.search(2)
if search_result:
    print(f"Node with data {search_result.data} found.")
else:
    print("Node not found.")
