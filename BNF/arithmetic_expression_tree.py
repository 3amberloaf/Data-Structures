class TreeNode:
    """A node in the arithmetic expression tree."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_expression():
    """Parse an expression that involves addition or subtraction and use a global variable to keep track of number being processed"""
    global current_spot
    node = parse_term()

    while current_spot in ("+", "-"): 
        operator = current_spot
        get_next_token()
        right = parse_term()
        node = TreeNode(operator, node, right)

    return node

def parse_term():
    """Parse a term that involves multiplication or division."""
    global current_spot
    node = parse_factor()

    while current_spot in ("*", "/"):
        operator = current_spot
        get_next_token()
        right = parse_factor()
        node = TreeNode(operator, node, right) 

    return node

def parse_factor():
    """Parse a factor, which could be an expression in parentheses or a literal."""
    global current_spot
    if current_spot == "(":
        get_next_token()  # Skip '('
        node = parse_expression()
        if current_spot != ")":
            raise Exception("Expected ')'")
        get_next_token()  # Skip ')'
    else:
        if not current_spot.isdigit():
            raise Exception("Expected number")
        node = TreeNode(current_spot)
        get_next_token()

    return node

def get_next_token():
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

def evaluate_tree(node):
    """Evaluate the arithmetic expression represented by the tree."""
    if node.value.isdigit():
        return int(node.value)
    elif node.value == "+":
        return evaluate_tree(node.left) + evaluate_tree(node.right)
    elif node.value == "-":
        return evaluate_tree(node.left) - evaluate_tree(node.right)
    elif node.value == "*":
        return evaluate_tree(node.left) * evaluate_tree(node.right)
    elif node.value == "/":
        return evaluate_tree(node.left) / evaluate_tree(node.right)
    
def print_tree(node, prefix=""):
    """Prints the expression tree in a structured manner."""
    if node is not None:
        print_tree(node.right, prefix + "    ")
        print(prefix + f"-- {node.value}")
        print_tree(node.left, prefix + "    ")

def print_expression(node):
    """Prints the arithmetic expression represented by the tree."""
    if node is None:
        return ""
    if node.left is None and node.right is None:
        return node.value
    left_expr = print_expression(node.left)
    right_expr = print_expression(node.right)
    if node.value in "+-*/":
        return f"({left_expr} {node.value} {right_expr})"
    return node.value



# Main execution flow
arithmetic_expression_string = input("Enter an arithmetic expression: ").replace(' ', '')
current_spot = ""
get_next_token()
expression_tree = parse_expression()

# Evaluation
result = evaluate_tree(expression_tree)
print("Result of Evaluation:", result)

print("\nExpression Tree:")
print_tree(expression_tree)