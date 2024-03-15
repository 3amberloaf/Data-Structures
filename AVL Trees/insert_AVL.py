# Insert into AVL tree

class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    
    # Initialize root
    def __init__(self):
        self.root = None
    
    # Get height
    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def max(self, a, b):
        return a if a > b else b

    def right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + self.max(self.get_height(y.left),
                                self.get_height(y.right))
        x.height = 1 + self.max(self.get_height(x.left),
                                self.get_height(x.right))

        # Return new root
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + self.max(self.get_height(x.left),
                                self.get_height(x.right))
        y.height = 1 + self.max(self.get_height(y.left),
                                self.get_height(y.right))

        # Return new root
        return y

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def insert(self, node, key):
        # Perform the normal BST insertion
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:  # Duplicate keys not allowed
            return node

        # Update height of this ancestor node
        node.height = 1 + self.max(self.get_height(node.left),
                                    self.get_height(node.right))

        # Get the balance factor of this ancestor node to check if it became unbalanced
        balance = self.get_balance(node)

        # If node becomes unbalanced, then 4 cases
        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def pre_order(self, node):
        if node:
            print(node.key, end=' ')
            self.pre_order(node.left)
            self.pre_order(node.right)


# Driver code
if __name__ == "__main__":
    tree = AVLTree()

    # Constructing tree given in the above figure
    tree.root = tree.insert(tree.root, 10)
    tree.root = tree.insert(tree.root, 20)
    tree.root = tree.insert(tree.root, 30)
    tree.root = tree.insert(tree.root, 40)
    tree.root = tree.insert(tree.root, 50)
    tree.root = tree.insert(tree.root, 25)

    # The constructed AVL Tree would be
    #         30
    #        /  \
    #      20   40
    #     / \     \
    #    10  25    50
    print("Preorder traversal of constructed tree is: ")
    tree.pre_order(tree.root)
