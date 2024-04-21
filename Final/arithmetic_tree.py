def expression (expressionTree):    
    """ returns the expression tree of the expresion that is recognized"""
    """ <expression> ::= <term> + <expression> | <term> - <expression> | <term> """
    
    termtree;
    
    term (termtree); // returns the subtree of expression tree of the first term 
    
    if (token == "+"):
        """ mean you are in <expression> ::= <term> + <expression> """
        expressionTree2;
        gettoken(token);
        expression(expressionTree2);
        expressionTree.val = "+"; expressionTree.left=termtree; expressionTree.right = expressionTree2;
        
    else:
        if (token == "-"):
          """ mean you are in <expression> ::= <term> - <expression> """
        expressionTree2;
        gettoken(token);
        expression(expressionTree2);
        expressionTree.val = "-"; expressionTree.left=termtree; expressionTree.right = expressionTree2;
        else:
        """ mean you are in <expression> ::= <term> """
        expressionTree.termtree;
                

    