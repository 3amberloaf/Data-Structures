# Backus Naur Form

BNF is a notation technique used to express the syntax of programming languages, command/instruction sets, and communication protocols. It is a mathematical way to describe a language by using a set of derivative rules, each describing how a symbol can be replaced with a sequence of symbols. These symbols can be terminal or lexemes or non-terminal. The rules define how to form valid strings (sentances) in the language. 

**Represent**

1. <> means it can be expanded into something else
2. | vertical lines represent 'or'
3. LHS: Left hand side, always non-terminals
4. RHS: Right hand side, either a terminal or non-terminal
5. ::= means 'is defined as'
6. Terminal: actual symbols of the language that CANNOT be simplified
7. Non-terminals: placeholders for patterns of symbols

**LHS --> RHS Terminal Example**

A BNF specifcation is a set of production rules, written as:

```go
<digit> --> 0|1|2|3|4|5|6|7|8|9
```

This example says the rule states that 'digit' can be expanded into the number 0,1,2,3,4,5,6,7,8, or 9


**LHS --> RHS Non Terminal Recursive Example**


```go
<digit> -> 0|1|2|3|4|5|6|7|8|9 
<natural> -> <digit> | <digit><natural>  
```

This says that a natural number is either a digit OR a digit followed by a natural number. The first line is the base case, the second is the recursive. 

**LHS --> RHS Non Terminal Recursive Derivation Example**

A derivation starts with a given non-terminal, and expands it step by step. 
A left-most derivation is when you expand on the left first. 

```go
<natural> => <digit><natural> 
          => 9<natural>
          => 9<digit><natural>
          =>93<natural>
          =>93<digit>
          =>934
```

### Step-by-Step Explaination

1. <natural> => <digit><natural> 
    - Our starting base
2. <natural> => 9<natural>
    - Start expanding the non-terminals by arbitrarily choosing a number
3. <natural> => 9<digit><natural>
    - From the recursive example, we know that <natural> is either <digit> or <digit><natural> so we expand it again
4. <natural> => 93<natural>
    - Expand the non-terminal again
5. <natural> => 9<digit>
    - Here we choose the base case because <natural> is either <digit> or <digit><natural>
6. <natural> => 934
    - Final answer

Problem with this example is that we could have chose 0 as the first digit, which makes it incorrect. We can improve this by redefining <natural> and creating a new non-terminal called <digits>. 

```go
<natural> -> <digit> | <nonzero><digits>
<digits> -> <digit> | <digit><digits>
<digit> -> 0 | <nonzero>
<nonzero> -> 1|2|3|4|5|6|7|8|9 
```

### Step-by-Step Explaination

1. <natural> -> <digit> | <nonzero><digits>
    - Start with a digit (can be a number from 0-9) or a non-zero (if there will be a number with multiple digits, then the first number cannot be a 0)
2. <digits> -> <digit> | <digit><digits>
    - digits can either be a number from 0-9 or multiple numbers
3. <digit> -> 0 | <nonzero>
    - A digit can either be a 0 or a nonzero (number from 1-9)
4. <nonzero> -> 1|2|3|4|5|6|7|8|9 
    - A nonzero is any number from 1-9

