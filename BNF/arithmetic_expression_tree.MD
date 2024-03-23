# Arithmetic Expression Tree

Arithmetic expression trees are a way to represent expressions through a binary tree structure, where each node is an operator or operand. 

**Components**
1. Node: Each node in the tree can be an operand (like numbers) or an operator (like +, -, *, /).
2. Leaf Nodes: The leaf nodes of the tree are always operands (numbers).
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

# Code

## Tree Constructor

```python
class TreeNode:
    """A node in the arithmetic expression tree."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
```

This class constructor will initialize nodes for the tree.

## Parse Expression

This function will parse an expression that involves addition or subtraction and use a global variable to keep track of number being processed. 

```python
def parse_expression():
    global current_spot
    node = parse_term()

    while current_spot in ("+", "-"): 
        operator = current_spot
        scan_token()
        right = parse_term()
        node = TreeNode(operator, node, right)

    return node
```

1. `global current_spot`: A global variable used to keep track of the number/operation that is currently being processed.
2. `node = parse_term()`: Parses the expression and returns a `TreeNode` expressing that term. This term becomes the initial node of the expression tree.
3. `while current_spot in ("+", "-")`: loops through expression when its addition or subtraction
    - `operator = current_spot`: Stores the operator (either + or -) in the current_spot variable
    - `scan_token()`: Updates current_spot to next spot in expression
    - `right = parse_term()`: Parses the next term in expression (becomes right node of Tree)
    - `node = TreeNode(operator, node, right)`: Creates a new TreeNode with the current operator as its value, the current node as its left child, and the new erm (right) as its right child. 
4. `return node`: Returns the root node of the constructed expression tree

## Parse Term

This function will parse a term that multiplication or division and use a global variable to keep track of number being processed. 

```python
def parse_term():
    global current_spot
    node = parse_factor()

    while current_spot in ("*", "/"):
        operator = current_spot
        scan_token()
        right = parse_factor()
        node = TreeNode(operator, node, right) 

    return node
```

1. `global current_spot`: A global variable used to keep track of the number/operation that is currently being processed.
2. `node = parse_factor()`: Parses a single factor and returns a `TreeNode` expressing that factor. This term becomes the initial node of the term.
3. `while current_spot in ("*", "/")`: loops through expression when its multiplication or division
    - `operator = current_spot`: Stores the operator (either * or /) in the current_spot variable
    - `scan_token()`: Updates current_spot to next spot in expression
    - `right = parse_term()`: Parses the next term in expression (becomes right node of Tree)
    - `node = TreeNode(operator, node, right)`: Creates a new TreeNode with the current operator as its value. The existing node becomes the left child of this new node, and the newly parsed factor (right) becomes the right child. This effectively builds a subtree of the expression tree, representing the multiplication or division operation just parsed.
4. `return node`: Returns the root node of the constructed subtree

## Parse Factor

This function will parse a factor. 

```python
def parse_factor():
    """Parse a factor, which could be an expression in parentheses or a literal."""
    global current_spot
    if current_spot == "(":
        scan_token()  # Skip '('
        node = parse_expression()
        if current_spot != ")":
            raise Exception("Expected ')'")
        scan_token()  # Skip ')'
    else:
        if not current_spot.isdigit():
            raise Exception("Expected number")
        node = TreeNode(current_spot)
        scan_token()

    return node
```

1. `global current_spot`: A global variable used to keep track of the number/operation that is currently being processed.
2. `if current_spot == "("`: Checks if the current token is an opening parenthesis (. If so, the code will treat the following tokens as a sub-expression until a closing parenthesis ) is encountered.
    - `scan_token()`: move past ()
    - `node = parse_expression()`: Parses the expression inside the ()
    - `if current_spot != ")"`: If the token isnt closing ()
       - `raise Exception("Expected ')'")`: Raise error
    - `scan_token()`: Moves past the closing parenthesis by updating current_spot to the next token, assuming the sub-expression was correctly closed
4. `else:if not current_spot.isdigit()`: Raises error if current spot is not ()
    - `node = TreeNode(current_spot)`: Creates a new TreeNode with the current token as its value. This assumes that current_spot is a digit (a number) and creates a leaf node in the expression tree representing this number.
    - `scan_token()`: updated spot
5. `return node`: Returns tree

## Update spot

This function is responsible for fetching the next token from an input string (which represents the arithmetic expression) and updating the global variable current_spot to reflect this token.

```python
def scan_token():
    """Fetch the next token from the input string."""
    global current_spot, arithmetic_expression_string
    arithmetic_expression_string = arithmetic_expression_string.lstrip()  # Strip leading whitespace
    if not arithmetic_expression_string:
        current_spot = None  # End of input
    else:
        current_spot = arithmetic_expression_string[0]
        if current_spot.isdigit():  # Handle multi-character numbers
            for i, char in enumerate(arithmetic_expression_string[1:], 1):
                if char.isdigit():
                    current_spot += char
                else:
                    break
            arithmetic_expression_string = arithmetic_expression_string[len(current_spot):]
        else:
            arithmetic_expression_string = arithmetic_expression_string[1:]
    return current_spot
```

1. `global current_spot, arithmetic_expression_string`: Declares current_spot and arithmetic_expression_string as global variables. current_spot is used to store the current token being processed, and arithmetic_expression_string contains the remaining part of the arithmetic expression that has not been parsed yet.
2. `arithmetic_expression_string = arithmetic_expression_string.lstrip()`: Strip leading whitespace`
3. `if not arithmetic_expression_string: current_spot = None`: Checks if arithmetic_expression_string is empty, indicating that we've reached the end of the input. If so, it sets current_spot to None to signal that there are no more tokens to process.
4. `else: current_spot = arithmetic_expression_string[0]`: If the input string is not empty, it sets current_spot to the first character of arithmetic_expression_string. This character could be a digit (part of a number), an operator, or a parenthesis.
5. `if current_spot.isdigit():`: Checks if current_spot is a digit. 
6. `for i, char in enumerate(arithmetic_expression_string[1:], 1):
                if char.isdigit():
                    current_spot += char
                else:
                    break`
If current_spot is a digit, it iterates through the subsequent characters in arithmetic_expression_string to check if they are also digits. It concatenates these digits to current_spot, forming a complete numeric token.
The loop breaks upon encountering a non-digit character, indicating the end of the numeric token.
7. `arithmetic_expression_string = arithmetic_expression_string[len(current_spot):]`: Updates arithmetic_expression_string by removing the part that has been processed as the current token. If the token is a number with multiple digits, it removes the entire number.
8. `else:arithmetic_expression_string = arithmetic_expression_string[1:]`: If the current token is not a digit (meaning it's an operator or a parenthesis), it simply removes the first character from arithmetic_expression_string.
9. `return current_spot`: Returns the current token (current_spot), which could be a number, an operator, or a parenthesis.
