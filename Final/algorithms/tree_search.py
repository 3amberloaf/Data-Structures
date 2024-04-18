class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def tree_search(k, v):
    # If v is an external node (in Python, this means v is None), return it.
    if v is None:
        return v
    
    # If the search key k equals the key of node v, return v.
    if k == v.val:
        return v
    
    # If the search key k is less than the key of node v, search the left subtree.
    elif k < v.val:
        return tree_search(k, v.left)
    
    # If the search key k is greater than the key of node v, search the right subtree.
    else:
        return tree_search(k, v.right)

# Example of using the TreeNode class to create a tree and using tree_search to find a node.
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(12)
root.right.right = TreeNode(18)

# Searching for a node with value 15 in the tree.
found_node = tree_search(15, root)
if found_node:
    print(f"Node with value {found_node.val} found.")
else:
    print("Node not found.")
