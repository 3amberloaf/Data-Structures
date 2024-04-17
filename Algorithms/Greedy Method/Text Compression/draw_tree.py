import heapq

from collections import Counter

def create_frequency_table(input_string):
    # Count the frequency of each character in the string
    frequency_table = Counter(input_string)
    
    # Display the frequency table
    print("Character Frequencies:")
    for char, freq in frequency_table.items():
        print(f"   '{char}': {freq}")

    return frequency_table

input_string = "dogs do not spot hot pots or cats"
frequency_table = create_frequency_table(input_string)

def build_huffman_tree(frequency_table):
    # Convert the frequency table into a list of tuples
    nodes = [(freq, [char, ""]) for char, freq in frequency_table.items()]

    # Use heapq to create a priority queue (min heap)
    heapq.heapify(nodes)

    while len(nodes) > 1:
        # Combine the two nodes with the lowest frequency
        lo = heapq.heappop(nodes)
        hi = heapq.heappop(nodes)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(nodes, (lo[0] + hi[0], lo[1:] + hi[1:]))

    # Return the root of the Huffman tree
    return nodes[0]

root = build_huffman_tree(frequency_table)

def generate_huffman_codes(node, prefix=""):
    """ Recursively generate Huffman codes. """
    # Base case: if the list in the node has only one element, it's a leaf node.
    if len(node[1]) == 1:
        char, code = node[1][0]
        return [(char, prefix + code)]
    else:
        # Recursive case: combine codes from the left and right subtrees.
        result = []
        for subnode in node[1]:
            char, code = subnode
            result.extend(generate_huffman_codes((node[0], [subnode]), prefix + code))
        return result


huffman_codes = generate_huffman_codes(root)

# Display the Huffman codes
print("\nHuffman Codes:")
for char, code in huffman_codes:
    print(f"   '{char}': {code}")