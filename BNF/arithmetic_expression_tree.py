class Lexer:
    """ Breaks down strings into tokens """
    def __init__(self, text):
        self.text = text.replace(' ', '')  # Remove whitespace
        self.index = 0  
        self.current_token = None  
        self.scan_token()  # Scan tokens immediately

    def scan_token(self):
        """ Updates token attribute"""
        if self.index >= len(self.text): # Reach end of index and reset token to none
            self.current_token = None
            return
        
        character= self.text[self.index] 
        
        """ If character is a digit, token reads all the digits"""
        if character.isdigit():
            start_index = self.index
            while self.index < len(self.text) and self.text[self.index].isdigit():
                self.index += 1
            self.current_token = self.text[start_index:self.index]
        else:
            """ If not a digit, move past """
            self.current_token = character
            self.index += 1

class TreeNode:
    """Superclass to instantiate nodes in the expression tree."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_expression(lexer):
    """Parse an expression that involves addition or subtraction."""
    node = parse_factor(lexer)

    while lexer.current_token in ("*", "/"): 
        operator = lexer.current_token
        lexer.scan_token()
        right = parse_factor(lexer)
        node = TreeNode(operator, node, right)

    return node

def parse_factor(lexer):
    """Parse a term that involves multiplication or division."""
    node = parse_term(lexer)

    while lexer.current_token in ("+", "-"):
        operator = lexer.current_token
        lexer.scan_token()
        right = parse_term(lexer)
        node = TreeNode(operator, node, right)

    return node

def parse_term(lexer):
    """Parse factors"""
    if lexer.current_token == "{":
        lexer.scan_token()  # Skip '('
        node = parse_expression(lexer)
        if lexer.current_token != "}":
            raise Exception("Expected '}'")
        lexer.scan_token()  # Skip ')'
    else:
        if not lexer.current_token.isdigit():
            raise Exception("Expected number")
        node = TreeNode(lexer.current_token)
        lexer.scan_token()

    return node

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

### Execute ###

expression = Lexer('{4+2}*{3-1}')
expression_tree = parse_expression(expression)
result = evaluate_tree(expression_tree)
print("Result of Evaluation:", result)

print("\nExpression Tree:")
print_tree(expression_tree)
