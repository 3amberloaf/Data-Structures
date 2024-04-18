class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.children = []
        
    def add_child(self, child_node):
        self.children.append(child_node)
        
    def postorderTraversal(self):
        
        nodes = []
               
        for child in self.children:
            nodes.extend(child.postorderTraversal())
        
        nodes.append(self.value)

        return nodes
        
    def binaryPostorderTraversal(self):
        
        nodes = []
        
        if self.left:
            nodes += self.left.binaryPostorderTraversal()
        
        if self.right:
            nodes += self.right.binaryPostorderTraversal()
        
        nodes.append(self.value)
        
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


print(root.postorderTraversal())