import heapq

from numpy import character


class Node:
    def __init__(self, frequency, character, left=None, right=None):
        self.frequency = frequency
        self.character = character
        self.left = left
        self.right = right
        self.huffman = ''
        
    def __lt__(self, next):
        return self.frequency < next.frequency
    
def printNodes(node, value = ''):
    newValue = value + str(node.huffman)
    
    if (node.left):
        printNodes(node.left, newValue)
    if (node.right):
        printNodes(node.right, newValue)
    
    if (not node.left and not node.right):
        print(f"{node.character} -> {newValue}")

characters = ['a', 'b', 'c', 'd', 'e', 'f'] 

# frequency of characters 
frequencies = [5, 9, 12, 13, 16, 45] 

# list containing unused nodes 
nodes = []

for x in range(len(characters)):
    heapq.heappush(nodes, Node(frequencies[x], characters[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    
    left.huffman = 0
    right.huffman = 1
    
    newNode = Node(left.frequency + right.frequency, left.character + right.character, left, right)
    
    heapq.heappush(nodes, newNode)

printNodes(nodes[0])