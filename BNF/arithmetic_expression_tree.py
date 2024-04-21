class tokenizer:
    """ Superclass to break down strings into tokens """
    def __init__(self, string):
        self.string = string.replace(' ', '')  # Remove whitespace
        self.index = 0  
        self.current_token = None  
        self.scan_token()

    def scan_token(self):
        """ Updates token variable """
        if self.index >= len(self.string): # Reach end of index and reset token to none
            self.current_token = None
            return
        
        character = self.string[self.index] # Token will analyze characters in string
        
        """ If character is a digit, token reads all the digits before moving on"""
        if character.isdigit():
            start_index = self.index
            while self.index < len(self.string) and self.string[self.index].isdigit(): # while there are more characters that are digits to be processed  
                self.index += 1
            self.current_token = self.string[start_index:self.index]
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

def parse_expression(tokenizer):
    """Parse an expression that involves multipication or division."""
    """ <expression>  ::=  <factor>  * <expression>   |   <factor>  /  <expression>   |   <factor> """
    node = parse_factor(tokenizer)

    while tokenizer.current_token in ("*", "/"): 
        operator = tokenizer.current_token
        tokenizer.scan_token()
        right = parse_factor(tokenizer)
        node = TreeNode(operator, node, right)

    return node

def parse_factor(tokenizer):
    """Parse a term that involves addition or subtraction."""
    """ <factor>  :==  <term> + <factor>  |  <term> - <factor>  |  <term> """
    node = parse_term(tokenizer)

    while tokenizer.current_token in ("+", "-"):
        operator = tokenizer.current_token
        tokenizer.scan_token()
        right = parse_term(tokenizer)
        node = TreeNode(operator, node, right)

    return node

def parse_term(tokenizer):
    """Parse terms"""
    """ <term>  ::=  {  <expression>  }  |  <literal> """
    
    if tokenizer.current_token == "{":
        tokenizer.scan_token()  # Skip '{'
        node = parse_expression(tokenizer)
        if tokenizer.current_token != "}":
            raise Exception("Expected '}'")
        tokenizer.scan_token()  # Skip '}'
    else:
        if not tokenizer.current_token.isdigit():
            raise Exception("Expected number")
        node = TreeNode(tokenizer.current_token)
        tokenizer.scan_token()

    return node

def evaluate_tree(node):
    """ Evaluate the arithmetic expression """
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

expression = tokenizer('{8/4/2-6*8/3-5}')
expression_tree = parse_expression(expression)
result = evaluate_tree(expression_tree)
print("Result of Evaluation:", result)
print("\nExpression Tree:")
print_tree(expression_tree)
