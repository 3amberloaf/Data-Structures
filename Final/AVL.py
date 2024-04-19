class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 
    
class AVLTree(object):
        
        def insert(self, root, key):
            
            # look for key
            if not root:
                return TreeNode(key)
            
            elif key < root.value:
                root.left = self.insert(root.left, key)
            
            else:
                root.right = self.insert(root.right, key)
            
            # update height after insertion    
            root_height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
            
            # balance factor
            balance = self.getBalance(root)
            
            # if node is unbalanced, rebalance
            """ Left Left Rotation """
            if balance > 1 and key < root.left.value: 
                return self.rightRotate(root) 
  
            """ Right Right Rotation """
            if balance < -1 and key > root.right.value: 
                return self.leftRotate(root) 
    
            """Left Right Rotation """
            if balance > 1 and key > root.left.value: 
                root.left = self.leftRotate(root.left) 
                return self.rightRotate(root) 
    
            """ Right Left Rotation """
            if balance < -1 and key < root.right.value: 
                root.right = self.rightRotate(root.right) 
                return self.leftRotate(root) 
    
            return root
        
        def leftRotate(self, z):
            
            y = z.right
            T2 = y.left
            
            y.left = z
            z.right = T2
            
            z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
            y.height = 1 + max(self.getHeight(y.left), 
                            self.getHeight(y.right)) 
    
            # Return the new root 
            return y 
            
            
        def rightRotate(self, z): 
  
            y = z.left 
            T3 = y.right 
    
            # Perform rotation 
            y.right = z 
            z.left = T3 
    
            # Update heights 
            z.height = 1 + max(self.getHeight(z.left), 
                            self.getHeight(z.right)) 
            y.height = 1 + max(self.getHeight(y.left), 
                            self.getHeight(y.right)) 
    
            # Return the new root 
            return y 
  
        def getHeight(self, root): 
            if not root: 
                return 0
    
            return root.height 
    
        def getBalance(self, root): 
            if not root: 
                return 0
    
            return self.getHeight(root.left) - self.getHeight(root.right) 
    
        def preOrder(self, root): 
    
            if not root: 
                return
    
            print("{0} ".format(root.value), end="") 
            self.preOrder(root.left) 
            self.preOrder(root.right) 
  
  
# Driver program to test above function 
myTree = AVLTree()
root = None
  
root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 
  
"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
  
# Preorder Traversal 
print("Preorder traversal of the constructed AVL tree is") 
myTree.preOrder(root) 
print() 

