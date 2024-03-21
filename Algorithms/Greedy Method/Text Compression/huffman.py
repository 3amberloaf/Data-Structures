## Huffmans Algorithm

import heapq
from collections import defaultdict

class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
        
    def __lt__(self, other): # Less than
        return self.frequency < other.frequency
    
    def __eq__(self, other): # Equal to
        if other is None:
            return False
        if not isinstance(other, Node):
            return False
        return self.frequency == other.frequency
    
    def __gt__(self, other): # Greater than
        return self.frequency > other.frequency
    
# Calculate each strings frequency
def calculate_frequency(string):
    return defaultdict(int, {character: string.count(character) for character in set(string)})

# Implement Huffmans encoding
def huffmanEncoding(string):
    
    # Calculate string frequency
    frequency = calculate_frequency(string)
    
    # Create priority queue using frequency
    priority_queue = [Node(character, frequency) for character, frequency in frequency.items()]
    heapq.heapify(priority_queue) 
    
    # Iterate until queue has more than one node
    while(len(priority_queue) > 1):
        
        # Remove two nodes with lowest frequency
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        
        # Merge these two nodes into one internal node with combined frequency
        merged = Node(None, left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        
        # Add the merged node back into priority queue
        
        heapq.heappush(priority_queue, merged)
        
    # Remaining node is root node
    root = priority_queue[0]
    return root

def print_codes(node, code=""):
    # The code for each character is determined by the path taken to reach it from the root
    if node.character is not None:
        print(f"{node.character}: {code}")
        return
    
    # traverse to left
    print_codes(node.left, code + "0")
    
    # Traverse to right
    print_codes(node.right, code + "1")
    
string = "Amber Sautner"
root = huffmanEncoding(string)
print_codes(root)