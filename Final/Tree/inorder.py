class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None  
    
    def inorderTraversal(self):
        
        nodes = []
        
        if self.left:
            nodes += self.left.inorderTraversal()
        
        nodes.append(self.value)
        
        if self.right:
            nodes += self.right.inorderTraversal()
        
        return nodes
    
root = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)
child4 = TreeNode(4)
child5 = TreeNode(5)
child6 = TreeNode(6)

root.left = child2
root.right = child3
child2.left = child5
child2.right = child6
child3.right = child4

print(root.inorderTraversal())