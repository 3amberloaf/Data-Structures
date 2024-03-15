# Insert into a binary search tree

class BST:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    
    if root is None:
        return BST(key)
    # if there is no root, return the tree value
    
    else:
        if root.val < key:
            root.right = insert(root.right, key)
    # if the roots value is less than the key we are inserting, insert key to the right of the tree
        
        else:
            root.left = insert(root.left, key)
    
    return root

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

root = None
elements = [70, 35, 40, 90, 20, 50, 45, 60, 80, 95, 85]



# Insert elements into the BST
for element in elements:
    root = insert(root, element)

# Print the BST
print_tree(root)