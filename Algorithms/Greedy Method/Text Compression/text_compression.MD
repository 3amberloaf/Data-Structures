# Text Compression

Given a string X, efficiently encode X into a smaller string Y. This helps save memory and bandwith.

1. Code - a mapping of each character of an alphabet to a binary code word
2. Prefix code - a  binary code such that no code word is the prefix of another code word
3. Encoding tree - represents a prefix code
- Each internal node stores a character
- The code word of a character is given by the path from the root to  the external node storing the character (0 for a left child and 1 for a right child)

# Huffman's Algorithm

Huffman's algorithm is a popular greedy algorithm used for lossless data compression. It's a process for creating a binary tree that represents the most efficient way to encode data, typically text, based on the frequency of the elements. The goal is to minimize the total length of the message once encoded.

It runs in O(n + dlog d) where n is the size of the string and d is the number of distinct characters in the string. 

![alt text](../algorithm_photos/huffman2.png)

**Steps**

1. Frequency Table: Calculate the frequency of each element in the data to be encoded
2. Create Leaf Nodes: For each unique element, create a leaf node with the element and its frequency
3. Build a Priority Queue(Min-Heap): Place all leaf nodes into a priority queue (min-heap) based on their frequency
4. Construct the Huffman Tree
- While there is more than one node in the queue:
    - Remove the two nodes of the lowest frequency from the queue.
    - Create a new internal node with these two nodes as children and a frequency that is the sum of the two nodes' frequencies.
    - Insert the new node back into the priority queue.
5. Assign Codes to Characters: Once the tree is built, traverse the tree from the root to the leaves, assigning a '0' for one branch and a '1' for the other at each split. The path to each leaf node determines the binary code for the corresponding element.

```python
def Huffman(X):
    Input: String X of length n with d distinct characters
    Output: Coding tree for X
    
    Compute the frequency f(c) of each character c of X.
    Initialize a priority queue Q.

    for each character c in X do
        Create a single-node binary tree T storing c
        Inster T into Q with key f(c)
    while len(Q) > 1 do
        (f1, T1) = Q.remove_min()
        (f2, T2) = Q.remove_min()
        Create a new binary tree T with left subtree T1 and right subtree T2
        Inster T into Q with key f1 + f2
    (f,T) = Q.remove_min()
    return tree T
```

**Example**

Encode "abracadabra"

1. Calculate the frequency of each letter

    a: 5
    b: 2
    c: 1
    d: 1
    r: 2

2. Create leaf nodes for unique elements and its frequency
3. Build Huffmans Tree
    - Step 1: The two nodes with the smaallest frequencies (c and d, each with a frequency of 1) are removed from the queue and combined into a new node with a combined frequency of 2. This new node becomes their parent
    - Step 2: The next two nodes with the smallest frequencies (r and the combined cd. each with a frequency of 2) are removed and combined into a new node with the combined frequency of 4
    - Step 3: Process continues until two remaining nodes (a and combined node brcd, with frequency of 6) are combined into the root node. This has a total frequency of all characters.

![alt text](../algorithm_photos/huffman1.png)

