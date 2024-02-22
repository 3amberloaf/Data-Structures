# Check if a given Binary Tree is Heap using Complete Binary Tree

class GFG:
	def __init__(self, value):
		self.key = value # node has a value
		self.left = None # left child doesnt have a value
		self.right = None # right child doesnt have a value

	def count_nodes(self, root):
		if root is None: # base case 
			return 0
		else:
			return (1 + self.count_nodes(root.left) + self.count_nodes(root.right)) # counts three (for parent and two children)

	def heap_property_util(self, root):
    # checks if the heap property is satisfies and returns True/False
    
		if (root.left is None and root.right is None): # root has no children so satisfies heap property by being the largest value
			return True

		if root.right is None:
			return root.key >= root.left.key # if no right child, the root must be greater than the left child
		else: # triggered if there is two children
			if (root.key >= root.left.key and root.key >= root.right.key): # if root is greater than or equal to both children, check the childrens subtrees 
				return (self.heap_property_util(root.left) and self.heap_property_util(root.right))
			else:
				return False

	def complete_tree_util(self, root, index, node_count):
     # checks if binary tree is complete
     
		if root is None: 
			return True
		if index >= node_count: # if any index is >= total node count the tree isnt complete
			return False
		return (self.complete_tree_util(root.left, 2 * index + 1, node_count) and self.complete_tree_util(root.right, 2 * index + 2, node_count)) # recursively checks subtrees

	def check_if_heap(self):
     # checks if binary heap is heap
		node_count = self.count_nodes(self) 
		if (self.complete_tree_util(self, 0, node_count) and self.heap_property_util(self)): # if tree is complete and satisfies heap properties
			return True
		else:
			return False


if __name__ == '__main__':
	root = GFG(5)
	root.left = GFG(2)
	root.right = GFG(3)
	root.left.left = GFG(1)

	# Function call
	if root.check_if_heap():
		print("Given binary tree is a heap")
	else:
		print("Given binary tree is not a Heap")