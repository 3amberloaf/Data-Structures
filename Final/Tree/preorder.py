
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.children = []
        
    def add_child(self, child_node):
        self.children.append(child_node)

        
    def preorderTraversal(self):
        
        nodes = [self.value]
        
        
        for child in self.children:
            nodes.extend(child.preorderTraversal())
            
        return nodes
        
    def binaryPreorderTraversal(self):
        
        nodes = []
        nodes.append(self.value)
        
        if self.left:
            nodes += self.left.binaryPreorderTraversal()
        
        if self.right:
            nodes += self.right.binaryPreorderTraversal()
        
        return nodes
    

root = TreeNode(1)
child2 = TreeNode(2)
child3 = TreeNode(3)
child4 = TreeNode(4)
child2.add_child(TreeNode(5))
child2.add_child(TreeNode(6))
child4.add_child(TreeNode(7))
root.add_child(child2)
root.add_child(child3)
root.add_child(child4)

# Preorder traversal (Should print [1, 2, 5, 6, 3, 4, 7])
print(root.preorderTraversal())