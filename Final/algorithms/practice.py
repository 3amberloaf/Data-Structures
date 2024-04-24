class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(inorder, preorder):
    if not inorder or not preorder:
        return None
    
    if len(inorder) == 1:
        return TreeNode(inorder[0])

    root_val = preorder[0]
    root = TreeNode(root_val)
    root_index_in_inorder = inorder.index(root_val)

    inorder_left = inorder[:root_index_in_inorder]
    inorder_right = inorder[root_index_in_inorder + 1:]

    preorder_left = preorder[1:1 + len(inorder_left)]
    preorder_right = preorder[1 + len(inorder_left):]

    root.left = build_tree(inorder_left, preorder_left)
    root.right = build_tree(inorder_right, preorder_right)

    return root

inorder_sequence = ['D', 'B', 'E', 'A', 'F', 'C']
preorder_sequence = ['A', 'B', 'D', 'E', 'C', 'F']
tree = build_tree(inorder_sequence, preorder_sequence)
print(tree)