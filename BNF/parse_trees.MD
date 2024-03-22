# Parse Trees using BNF

Precedence: Certain operators have more precedence over others
    - `x + 5 * y` should be interpreted as `x + (5 * y)

Associativity: For certain operators, we process them in order
    - `7 - 5 + 1` is 3 

**Syntax**

Rules: Define legal expression
Non-Terminal: Grammar symbols
Terminal: Operators (+,-,*,/, ()) or identifiers
ID: One or more characters
    - `char {char}`
Integer: one or more digits
    - `digit {digit}

E -> T + E | T = E | T
T -> F * T | F / T | F
F -> ID | Integer | (E) - F

### Lexical Analysis

A 'lexer'/'tokenizer' will read the input and break it into tokens. 

## Classes

TreeNode // Superclass
    Add // Subclasses
    Subtract
    Multiply
    Divide
    Negate
    ID
    Integer


## Print a Tree

Each class recursively calls to implements a print method.

# Top Down Recursive Descent Parsing Algorithm

**Functions**
One function for each non-terminal grammar symbol, each will scan a bunch of tokens and return a pointer to the three it builds.

- parseE()
- parseT()
- parseF()

**Details**
At any moment, `nextToken` will contain the next UNSCANNED thing from the input. We will call `nextToken()` to advance and return null if error.

## Main

**Variables**
    nextToken
    resultTree

**Code**
scanToken()
resultTree = parseE()
if nextToken <> \n
    error
resultTree.print()
print(result.Tree.eval())

## Parse F 
F -> ID | Integer | (E) | - F

**Code**
if nextToken is ID
    return nextToken
else if nextToken is Integer
    return nextToken
else if nextToken is "("
    scanToken() // Scan past "("
    a = parseE()
    if (a == NULL)
        return NULL
    if nextToken is ")"
        scanToken()
        return a
    else 
        return NULL
else if nextToken is "-"
    scanToken()
    return new Neg(parseF())
else 
    return NULL

## Parse E
E -> T { + | - T}

parseE:
    a = parseT()
    while true
        if nextToken == "+"
            scanToken()
            b = parseT()
            a = newAdd(a,b)
        else if nextToken == "-"
            scanToken()
            b = parseT()
            a = newSubtract(a,b) // a is pointer to previous node, v is pointer to new term being processes
        else
            return a


**Example**

```go
<statments> -> <statement> | <statement><statements>
<statement> -> <assign>; | <if-statement>
<assign> -> id = id
<if-statement> -> if(<boolean_expression>)<statement> 
                | if(<boolean_expression>)<statement> else<statement>
<boolean_expression> -> id == id
```

**Derivation**

```go
<statments> => <statement><statements>
            => <assign>; <statments>
            => id = id; <statements>
            => id = id; <statement>
            => id = id; <if-statement>
            => id = id; if(<boolean_expression>)<statement> else<statement>
            => id = id; if (id == id) <statement> else <statement>
            => id = id; if(id == id) <assign;> else <statement>
            => id = id; if(id == id) id = id; else <statement>
            => id = id; if(id == id) id = id; else <assign>;
            => id = id; if(id == id) id = id; else id = id;
```

This final sentance is equal to the following code:

`threshold = userInput;
if(threshold == criticalValue)
    result = specialValue;
else
    result = userInput;`

**Parse Tree**
                                    <statements>
                                    /           \
                            <statement>         <statements>
                            /                      \
                        <assign>;                   <statement>
                        /                               \
                    id = id                             <if-statement>
                                                           \
                                if(<boolean_expression>)<statement> else<statement> 
                                       /                    /               \
                                    id == id            <assign>;           <assign>;
                                                            /                   \
                                                        id = id             id = id


# Ambiguous Grammer

Issue is the whitespace! Some languages account for it while others do not. 

`if(value == best)
    if(update == userUpdate)
        userBest = value;
    else
        groupBest = value;`

will be compiled differently than

`if(value == best)
    if(update == userUpdate)
        userBest = value;
else
    groupBest = value;`

# Unambiguous Grammer

Problem: if(<boolean_expression>)<statement> else<statement> 

There can be repeated <if-statement> nested in <statement>, leading to ambiguity.

Solution: Redefine an individual statement

```go
<statements> -> <statement> | <statement><statements>
<statement> -> <matched> | <unmatched>
<matched> -> <assign>; | <if(<boolean_expression>)<matched> else<matched>
<unmatched> -> if(<boolean_expression>) <statement> 
               | if(<boolean_expression>)<matched> else<unmatched>
<assign> -> id = id
<boolnea_expression> -> id == id
```

if(value==best)if(update == userUpdate) userBest = value; else groupBest= value;
     |                      |                   |                       |
<boolean_expression>    <boolean_expression>    <assign>            <assign>
                                                    |                   |
                                                <matched>           <matched>
                                    \               |                   /
                                                <matched>
                                                    |
                                                <statement>
        \                                        /
                    <unmatched>
                          |
                    <statement>
                          |
                    <statements>