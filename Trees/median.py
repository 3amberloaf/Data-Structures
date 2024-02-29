# Tree Class
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.count = 1  # Count of nodes in the subtree rooted at this node.

# Count nodes, if no root return 0
def count_nodes(root):
    if root is None:
        return 0
    return root.count

def find_kth_smallest(root, k):
    # Find the kth smallest value in the BST.

    left_count = count_nodes(root.left)
    
    if k <= left_count:  # Target is in the left subtree
        return find_kth_smallest(root.left, k)
    elif k == left_count + 1:  # Target is the root itself
        return root.value
    else:  # Target is in the right subtree
        return find_kth_smallest(root.right, k - left_count - 1)

def find_median(root):
    if root is None:
        return None
    
    n = count_nodes(root)
    if n % 2 == 1:  # If count is odd, return the middle element
        return find_kth_smallest(root, n // 2 + 1)
    else:  # If count is even, return the average of the middle two elements
        a = find_kth_smallest(root, n // 2)
        b = find_kth_smallest(root, n // 2 + 1)
        return (a + b) / 2

# Example usage
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)

# Update counts for each node.
root.count = 7
root.left.count = 3
root.right.count = 3
root.left.left.count = 1
root.left.right.count = 1
root.right.left.count = 1
root.right.right.count = 1

median = find_median(root)
print("Median:", median)
