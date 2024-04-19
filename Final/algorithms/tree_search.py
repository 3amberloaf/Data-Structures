class TreeNode:
    def __init__(self, key, size):
        self.left = None
        self.right = None
        self.val = key
        self.size = size

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

def treeInsertion(v, key):
    
    if v is None:
        return TreeNode(key)
    
    else:
        if v.val < key:
            v.right = treeInsertion(v.right, key)
        else:
            v.left = treeInsertion(v.left, key)
    
    return v

def tree_select(i, node):
    """
    Selects the ith smallest element in the BST i is a 1-based index.
    """
    if node is None:
        return None
    
    left_size = node.left.size if node.left else 0
    
    # If the size of the left subtree is i - 1, the root is the ith smallest element.
    if i == left_size + 1:
        return node.key
    
    # If i is less than the size of the left subtree, the ith smallest is in the left subtree.
    elif i <= left_size:
        return tree_select(i, node.left)
    
    # If i is greater than the size of the left subtree + 1, the ith smallest is in the right subtree.
    # We subtract (left_size + 1) because we're now looking for the (i - left_size - 1)th smallest element in the right subtree.
    else:
        return tree_select(i - left_size - 1, node.right)

# Example of creating a tree with sizes at each node
root = TreeNode(44, 14)
root.left = TreeNode(23, 5)
root.right = TreeNode(63, 8)

# Now we can select the ith smallest element
i = 10
ith_smallest_element = tree_select(i, root)
print(f"The {i}th smallest element in the BST is: {ith_smallest_element}")