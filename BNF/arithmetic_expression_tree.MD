# Arithmetic Expression Tree

Arithmetic expression trees are a way to represent expressions through a binary tree structure, where each node is an operator or operand. They're especially useful for evaluating and manipulating mathematical expressions programmatically.

**Components**
1. Node: Each node in the tree can be an operand (like numbers) or an operator (like +, -, *, /).
2. Leaf Nodes: The leaf nodes of the tree are always operands.
3. Internal Nodes: The internal nodes (not leaves) are operators that perform some operation on their child nodes.

**Structure**

1. Root: The root of the tree is an operator node. The expression represented by the tree is evaluated by starting from this node.
2. Subtrees: Each node can have zero, one, or two children. 
    - For binary operators like addition or multiplication, there will be two children. 
    - Unary operators like negation (-) will have one child. 
    - Operands (leaf nodes) have zero children.

**Evaluation**

1. Start at the root node.
2. If the current node is an operand, return its value.
3. If the current node is an operator, recursively evaluate its left and right children.
4. Apply the operator to the values obtained from the children.
