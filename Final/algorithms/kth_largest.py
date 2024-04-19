# Consider a binary tree search of size N, and let k be a number between 1 and N. Assuming that all elements of the tree are distinct, 
# write a function that returns the kth element of the tree. You have to do so by navigating the tree itself.

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        
def nbNodes(node):
    """
    Returns the number of nodes in the binary tree.
    """
    # if tree is empty there are no nodes
    if node is None:
        return 0
    
    # if tree is not empty, count one for the root and recursion for left and right nodes
    else:
        return 1 + nbNodes(node.left) + nbNodes(node.right)

def kthLargest(node, k):
    """
    Selects the kth largest element in the BST. k is a 1-based index.
    """

    # current node is the largest element
    if nbNodes(node.left) + 1 == k:
        return node.value
    
    # largest element is in left subtree
    elif nbNodes(node.left) >= k:
        return kthLargest(node.left, k)
    
    # largest element is in right subtree
    else:
        return kthLargest(node.right, k - nbNodes(node.left) - 1)
        
        
    
    
root = TreeNode(9)
root.left = TreeNode(6)
root.right = TreeNode(17)
root.left.left = TreeNode(2)
root.left.right = TreeNode(8)
root.right.left = TreeNode(12)
root.right.right = TreeNode(25)
root.right.left = TreeNode(20)
root.right.left.right = TreeNode(15)
root.right.left.left = TreeNode(11)



# Finding the k-th largest element
k = 7
print(f"The {k}th largest element is: {kthLargest(root, k)}")